import json


class ThemeManager:

    theme: dict = {}
    _theme_path: str = ""

    @classmethod
    def load_theme(cls, theme_name: str):
        cls._theme_path = f"src/assets/themes/{theme_name}.json"
        with open(cls._theme_path, "r") as f:
            cls.theme = json.load(f)

    