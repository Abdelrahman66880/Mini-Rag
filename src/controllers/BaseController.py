from helper.config import Setting, get_settings
import os
import random
import string

class BaseController:
    def __init__(self):
        self.app_setting = get_settings()
        self.base_dir = os.path.dirname(os.path.dirname(__file__))
        self.file_dir = os.path.join(
            self.base_dir,
            "assets/files"
        )
        
        self.database_dir = os.path.join(
            self.base_dir,
            "assets/database"
        )
    
    def generate_random_string(self, lenght : int = 10):
        return "".join(random.choices(string.ascii_lowercase + string.digits, k=lenght))
    
    def get_database_path(self, db_name: str):
        database_path = os.path.join(
            self.database_dir, db_name
        )
        if not os.path.exists(database_path):
            os.mkdir(database_path)
        return database_path