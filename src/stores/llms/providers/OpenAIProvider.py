from LLMInterface import LLMInterface
from openai import OpenAI # type: ignore
from stores.LLMEnums import OpenAIEnum
import logging


class OpenAIprovider(LLMInterface):
    def __init__(self, api_key: str, api_url: str = None, 
                        default_input_max_characters: int = 1000,
                        default_generation_max_output_tokens: int = 1000,
                        default_generation_temperature: float = 0.1):
        
        self.api_key = api_key
        self.api_url = api_url
        self.default_input_max_characters = default_input_max_characters
        self.default_generation_max_output_tokens = default_generation_max_output_tokens
        self.default_generation_temperature = default_generation_temperature
        
        self.generation_model_id = None
        self.embedding_model_id = None
        self.embeddding_size = None
        
        self.client = OpenAI(
            api_key = self.api_key,
            api_url = self.api_url,
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
        chat_history.append(
            self.construct_prompt(prompt=prompt, role=OpenAIEnum.USER.value)
        )
        
        respone = self.client.chat.completions.create(
            model = self.generation_model_id,
            messages = chat_history,
            max_tokens = max_output_token,
            temperature = temperature
        )
        
        if not respone or not respone.choices or len(respone.choices) == 0 or not respone.choices[0].message:
            self.logger.error("Error while generating text with OpenAI")
            return None
        return respone.choices[0].message["content"]
        
        
    
    def embed_text(self, text:str, document_type: str = None):
        if not self.client:
            self.logger.error("OpenAI cleint is not set")
            return None
        if not self.embedding_model_id:
            self.logger.error("Embedding model with OpenAI is not set")
            return None
        
        respone = self.client.embeddings.create(
            input = text,
            model = self.embedding_model_id,
        )
        
        if not respone or len(respone.data) == 0 or respone.data[0].embedding:
            self.logger.error("Error while embedding text with OpenAI")
            return None
        return respone.data[0].embedding
    
    
    def construct_prompt(self, prompt: str, role: str):
        return {
            "role":role,
            "content": self.process_text(prompt)
        }
    
    
        