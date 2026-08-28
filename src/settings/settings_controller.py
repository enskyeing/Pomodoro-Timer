import json


class SettingsController:
    def __init__(self):
        self.settings_file = "src/settings/settings.json"
        self.default_settings = {
            "work_duration": 25,
            "break_duration": 5,
            "theme": "retro"
        }
        self.settings = {}

    def _load(self):
        try:
            with open(self.settings_file, "r") as f:
                self.settings = json.load(f)
        except FileNotFoundError:
            self.settings = self.default_settings
            self.save()

    def save(self):
        with open(self.settings_file, "w") as f:
            json.dump(self.settings, f, indent=4)
        
        self._load()

    def update(self, work_duration=None, break_duration=None, theme=None):
        if work_duration is not None and len(work_duration) > 0:
            self._check_duration(work_duration)
            self.settings["work_duration"] = int(work_duration)
        if break_duration is not None and len(break_duration) > 0:
            self._check_duration(break_duration)
            self.settings["break_duration"] = int(break_duration)
        if theme is not None and theme != self.settings["theme"]:
            self.settings["theme"] = theme

        self.save()

    def _check_duration(self, duration):
        try:
            duration_int = int(duration)
            if duration_int <= 0:
                raise ValueError("Duration must be a positive integer.")
            return True
        except ValueError:
            raise ValueError("Duration must be an integer.")

