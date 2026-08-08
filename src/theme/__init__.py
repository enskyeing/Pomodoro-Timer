from .thememanager import ThemeManager
import json

try:
    with open("src/settings.json", "r") as f:
        settings = json.load(f)
        theme_name = settings["theme"]
        ThemeManager.load_theme(theme_name)
except FileNotFoundError:
    raise FileNotFoundError("Theme file not found. Please ensure the theme file exists in the 'src/assets/themes/' directory.")