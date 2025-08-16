from helper.config import Setting, get_settings

class BaseController:
    def __init__(self):
        self.app_setting = get_settings()