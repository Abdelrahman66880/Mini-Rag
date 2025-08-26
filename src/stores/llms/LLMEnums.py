from enum import Enum


class LLMEnums(Enum):
    OPENAI = "OPENAI"
    COHERE = "COHERE"
    
    
class OpenAIEnum(Enum):
    SYSTEM ="system"
    USER = "user"
    ASSISTANT = "assistant"
    
class CohereEnum(Enum):
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "CHATBOT"
    DOCUMENT = "search_document"
    QUERY = "search_query"
    
    
class DocumentTypeEnum(Enum):
    Document = "document"
    QUERY = "query"