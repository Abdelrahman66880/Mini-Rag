from fastapi import FastAPI, APIRouter, Depends, UploadFile
from helper.config import get_settings, Setting
import os

data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1", "data"],
    
)

@data_router.post("/upload/{project_id}")
async def upload_data(project_id: str, file: UploadFile,
                      app_setting: Setting):
    pass
