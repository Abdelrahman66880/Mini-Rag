from enum import Enum
class ResponseSignal (Enum):
    FILE_VALIDATED_SUCCESS = "file_validate_successfully"
    FILE_TYPE_NOT_SUPPORTED = "file_type_not_supported"
    FILE_SIZE_EXCEEDED = "file_size_exceeded"
    FILE_UPLOAD_SUCCESS = "file_upload_success"
    FILE_UPLOAD_FAILED = "file_upload_failed"
    FILE_PROCESSED_SUCCESS = "file_processed_success"
    FILE_PROCESSED_FAILED = "file_processed_failed"
    PROCESSING_SUCCESS = "file_processing_success"