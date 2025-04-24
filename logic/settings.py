import json
import os
from pathlib import Path

SETTINGS_PATH = Path.home() / (
    ".config/pdf_keyword_tool/settings.json"
    if os.name != "nt"
    else os.path.expandvars("%APPDATA%/pdf_keyword_tool/settings.json")
)


def load_settings():
    if SETTINGS_PATH.exists():
        with open(SETTINGS_PATH, "r") as f:
            return json.load(f)
    return {}


def save_settings(settings):
    SETTINGS_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(SETTINGS_PATH, "w") as f:
        json.dump(settings, f, indent=2)
