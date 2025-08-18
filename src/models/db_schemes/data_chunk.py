# from pydantic import BaseModel, validator, Field
# from typing import Optional
# from bson.objectid import ObjectId

# class DataChunk(BaseModel):
#     _id: Optional[ObjectId]
#     chunk_text: str = Field(..., min_length=1)
#     chunk_metadata: dict
#     chunk_order: int = Field(..., gt=0)
#     chunk_project_id: ObjectId
    
#     class Config:
#         arbitraty_types_allowed = True

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
from bson import ObjectId


# # Custom validator for ObjectId
# class PyObjectId(ObjectId):
#     @classmethod
#     def __get_validators__(cls):
#         yield cls.validate

#     @classmethod
#     def validate(cls, v):
#         if not ObjectId.is_valid(v):
#             raise ValueError("Invalid ObjectId")
#         return ObjectId(v)


class DataChunk(BaseModel):
    id: Optional[ObjectId]
    chunk_text: str = Field(..., min_length=1)
    chunk_metadata: dict
    chunk_order: int = Field(..., gt=0)
    chunk_project_id: ObjectId

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

