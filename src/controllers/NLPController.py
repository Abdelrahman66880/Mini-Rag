from .BaseController import BaseController
from models.db_schemes import Project
from models.db_schemes import DataChunk
from stores.llms.LLMEnums import DocumentTypeEnum
import json
from typing import List

class NLPController(BaseController):
    def __init__(self, vectordb_client, generation_client, embedding_client, template_parser):
        super().__init__()
        self.vectordb_client = vectordb_client
        self.generation_client = generation_client
        self.embedding_client = embedding_client
        self.template_parser = template_parser
    
    def create_collection_name(self, project_id: str):
        return f"collection_{project_id}".strip()
    
    def reset_vector_db_collection(self, project: Project):
        collection_name = self.create_collection_name(project_id=project.project_id)
        return self.vectordb_client.delete_collection(collection_name=collection_name)
    
    async def get_vector_db_collection_info(self, project: Project):
        collection_name = self.create_collection_name(project_id=project.project_id)
        collection_info = await self.vectordb_client.get_collection_info(collection_name=collection_name)
        return json.loads(
            json.dumps(collection_info, default=lambda x: x.__dict__)
        )
    
    async def index_into_vector_db(self, project: Project, chunks: List[DataChunk],chunks_ids: List[int] ,do_reset: bool = False):
        collection_name = self.create_collection_name(project_id=project.project_id)
        
        #MANAGE ITEM
        texts = [c.chunk_text for c in chunks]
        metadata = [c.chunk_metadata for c in chunks]
        vectors = [
            self.embedding_client.embed_text(text= text, document_type=DocumentTypeEnum.Document.value)
            for text in texts
        ]
        
        
        # CREATE THE COLLECTION IF NOT EXIST
        _ = self.vectordb_client.create_collection(
            collection_name=collection_name,
            embedding_size=self.embedding_client.embedding_size,
            do_reset=do_reset
        )
        
        #INSERT INTO THE VECTOR DB
        collection = self.vectordb_client[collection_name]
        # _ = self.vectordb_client.insert_many(
        #     collection_name=collection_name,
        #     texts=texts,
        #     metadata=metadata,
        #     vectors=vectors,
        #     record_ids=chunks_ids
        # )
        result = await collection.insert_many(chunks)
        
        return True

    def search_vector_db_collection(self, project: Project, text: str, limit: int = 10):
        collection_name = self.create_collection_name(project_id=project.project_id)
        
        vector = self.embedding_client.embed_text(
            text=text,
            document_type = DocumentTypeEnum.QUERY.value 
        )
        
        if not vector or len(vector) == 0:
            return False
        
        results = self.vectordb_client.search_by_vector(
            collection_name=collection_name,
            vector=vector,
            limit=limit
        )
        
        if not results:
            return False
        
        return results
    
    
    def answer_rag_question(self, project: Project, query: str, limit: int = 10):
        retrieved_documents = self.search_vector_db_collection(
            project=project,
            text=query,
            limit=limit
        )
    
        if not retrieved_documents or len(retrieved_documents) == 0:
            return None

        
        ###============================================================
        #=================Construct The System Prompt==================
        
        system_prompt = self.template_parser.get("rag", "system_prompt")
        document_prompts = "\n".join([
            self.template_parser.get("rag", "document_parser", {
                "doc_num": idx,
                "chucnk_text": doc.text,
            })
            for idx, doc in enumerate(retrieved_documents)
        ])
        
        footer_prompt = self.template_parser.get("rag", "footer_prompt")
        
        chat_history = [
            self.generation_client.construct_prompt(
                prompt=system_prompt,
                role=self.generation_client.enums.SYSTEM.value,
            )
        ]
        
        full_prompt = "\n\n".join([document_prompts, footer_prompt])
        
        answer = self.generation_client.generate_text(
            prompt=full_prompt,
            chat_history=chat_history
        )
        
        return answer, full_prompt, chat_history