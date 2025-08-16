from fastapi import FastAPI, APIRouter, Depends, UploadFile, status
from fastapi.responses import JSONResponse
from helper.config import get_settings, Setting
from controllers import DataController, ProjectController
from models import ResponseSignal
import os
import aiofiles
import logging
logger = logging.getLogger("uvicorn.error")

data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1", "data"],
    
)

@data_router.post("/upload/{project_id}")
async def upload_data(project_id: str, file: UploadFile,
                      app_setting: Setting = Depends(get_settings)):
    
    is_valid, result_signal = DataController().validate_uploaded_file(file=file)
    
    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST, 
            content={
                "signal":result_signal
            }
        )
    
    project_dir_path = ProjectController().get_project_path(project_id=project_id)
    file_path = DataController().generate_unique_filename(
        orig_file_name=file.filename,
        project_id=project_id
    )
    try:
        async with aiofiles.open(file_path, "wb") as f:
            while chunk:= await file.read(app_setting.FILE_DEFAULT_CHUNK_SIZE):
                await f.write(chunk)
    except Exception as e:
        logger.error(f"error while uploading files {e}")
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "signal":ResponseSignal.FILE_UPLOAD_FAILED.value
            }
        )
    
    return JSONResponse(
        content={
            "signal":ResponseSignal.FILE_UPLOAD_SUCCESS.value
        }
    )
