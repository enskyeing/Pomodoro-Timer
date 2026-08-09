import json


class SettingsController:
    
    settings_file: str = "settings.json"
    default_settings: dict = {
        "work_duration": 25,
        "break_duration": 5,
        "theme": "retro"
    }
    settings: dict = {}

    @classmethod
    def load_settings(cls):
        try:
            with open(cls.settings_file, "r") as f:
                cls.settings = json.load(f)
        except FileNotFoundError:
            cls.settings = cls.default_settings
            cls.save_settings()

    @classmethod
    def save_settings(cls):
        with open(cls.settings_file, "w") as f:
            json.dump(cls.settings, f)

    @classmethod
    def update_settings(cls, work_duration=None, break_duration=None, theme=None):
        if work_duration is not None:
            cls.settings["work_duration"] = work_duration
        if break_duration is not None:
            cls.settings["break_duration"] = break_duration
        if theme is not None:
            cls.settings["theme"] = theme

        cls.save_settings()
