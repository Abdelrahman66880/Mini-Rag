from typing import Optional
from pydantic import BaseModel, Field, validator
from bson.objectid import ObjectId

class Project(BaseModel):
    _id: Optional[ObjectId]
    project_id: str = Field(..., min_length=1)

    @validator("project_id")
    def validate_project_id(cls, value):
        if not value.isalnum():
            raise ValueError("Project_id Must Be alphanumeric")
        return value
    
    class Config:
        arbitraty_types_allowed = True
        
# from typing import Optional
# from pydantic import BaseModel, Field, validator
# from bson import ObjectId

# class Project(BaseModel):
#     _id: Optional[ObjectId] = None  # MongoDB generates this automatically
#     project_id: str = Field(..., min_length=1)

#     @validator("project_id")
#     def validate_project_id(cls, value):
#         if not value.isalnum():
#             raise ValueError("project_id must be alphanumeric")
#         return value
    
#     class Config:
#         arbitrary_types_allowed = True
