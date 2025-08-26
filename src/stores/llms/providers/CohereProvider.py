from ..LLMInterface import LLMInsterface
from ..LLMEnums import CohereEnum, DocumentTypeEnum
import cohere # type: ignore
import logging


class Cohereprovider(LLMInsterface):
    def __init__(self, api_key: str,
                        default_input_max_characters: int = 1000,
                        default_generation_max_output_tokens: int = 1000,
                        default_generation_temperature: float = 0.1):
        
        self.api_key = api_key
        self.default_input_max_characters = default_input_max_characters
        self.default_generation_max_output_tokens = default_generation_max_output_tokens
        self.default_generation_temperature = default_generation_temperature
        
        self.generation_model_id = None
        self.embedding_model_id = None
        self.embeddding_size = None
        
        
        self.client = cohere.client(
            api_key = self.api_key
        )
        
        self.logger = logging.getLogger(__name__)
        
    #used to change the model in run time
    def set_generation_model(self, model_id: str):
        self.generation_model_id = model_id
        
    def set_embedding_model(self, model_id: str, embeddding_size):
        self.embedding_model_id = model_id
        self.embeddding_size = embeddding_size
    
    def process_text(self, text:str):
        return text[:self.default_input_max_characters].strip()
    
    
    def generate_text(self, prompt: str,chat_history:list=[], max_output_token: int = None,
                      temperature : float = None):
        
        if not self.client:
            self.logger.error("OpenAI cleint is not set")
            return None
        
        if not self.generation_model_id:
            self.logger.error("Generation model is not set")
            return None
        
        max_output_token = max_output_token if max_output_token else self.default_generation_max_output_tokens
        temperature = temperature if temperature else self.default_generation_temperature
        
        response = self.client.chat(
            model = self.generation_model_id,
            chat_history = chat_history,
            message = self.process_text(prompt),
            max_tokens = max_output_token
        )
        
        if not response or not response.text:
            self.logger.error("Errror while generating text with Coher")
            return None
        return response.text
    
    
    def embed_text(self, text:str, document_type: str = None):
        if not self.client:
            self.logger.error("OpenAI cleint is not set")
            return None
        
        if not self.embedding_model_id:
            self.logger.error("Generation model is not set")
            return None
        
        input_type = CohereEnum.DOCUMENT.value
        if document_type == DocumentTypeEnum.QUERY.value:
            input_type = CohereEnum.QUERY.value
        
        response = self.client.embed(
            model = self.embedding_model_id,
            text = [self.process_text(text)],
            embedding_type=['float'],
            
            
        )
        
        if not response or not response.embeddings or not response.embeddings.float:
            self.logger.error("Error in embedding model")
            return None
        
        return response.embeddings.float[0]
    
    
    def construct_prompt(self, prompt: str, role: str):
        return {
            "role":role,
            "content": self.process_text(prompt)
        }
    