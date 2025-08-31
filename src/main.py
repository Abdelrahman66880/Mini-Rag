from fastapi import FastAPI, UploadFile
from routes import base
from routes import data
from routes import nlp
from helper.config import get_settings
from motor.motor_asyncio import AsyncIOMotorClient
from stores.vectordb.VectorProviderFactory import VectorProviderFactory
from stores.llms.LLMProviderFactory import LLMProviderFactory
from stores.llms.templates.template_parser import TemplateParser


app = FastAPI()
@app.on_event("startup")
async def startup_span():
    settings = get_settings()
    app.mongo_conn = AsyncIOMotorClient(settings.MONGODB_URL)
    app.db_client = app.mongo_conn[settings.MONGODB_DATABASE]
    
    llm_provider_factory = LLMProviderFactory(config=settings)
    vectordb_provider_factory = VectorProviderFactory(config=settings)
    
    
    #GENERATION CLIENT
    app.generation_client = llm_provider_factory.create(provider=settings.GENERATION_BACKEND)
    app.generation_client.set_generation_model(model_id = settings.GENERATION_MODEL_ID)
    
    
    #EMBEDDING CLIENT
    app.embedding_client = llm_provider_factory.create(provider=settings.EMBEDDING_BACKEND)
    app.embedding_client.set_embedding_model(model_id = settings.EMBEDDING_MODEL_ID,
                                             embedding_size=settings.EMBEDDING_MODEL_SIZE)
    
    
    #vector database client
    app.vectordb_client = vectordb_provider_factory.create(
        provider=settings.VECTOR_DB_BACKEND
    )
    app.vectordb_client.connect()
    
    app.template_parser = TemplateParser(
        language=settings.PRIMARY_LANG,
        default_language=settings.DEFAULT_LANG,

    )



@app.on_event("shutdown")
async def shutdown_span():
    app.mongo_conn.close()
    app.vectordb_client.disconnect()
    


# app.router.lifespan.on_startup().append(startup_db_client)
# app.router.lifespan.on_shutdown().append(shutdown_db_client)
app.on_event("startup")(startup_span)
app.on_event("shutdown")(shutdown_span)

app.include_router(base.base_router)
app.include_router(data.data_router)
app.include_router(nlp.nlp_router)
