from fastapi import FastAPI, APIRouter, Depends, UploadFile
from helper.config import get_settings, Setting
from controllers import DataController
import os

data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1", "data"],
    
)

@data_router.post("/upload/{project_id}")
async def upload_data(project_id: str, file: UploadFile,
                      app_setting: Setting = Depends(get_settings)):
    
    is_valid = DataController().validate_uploaded_file(file=file)
    return is_valid
