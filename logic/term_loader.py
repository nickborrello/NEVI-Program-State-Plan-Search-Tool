import json
import os
import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and PyInstaller """
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

def load_terms(json_path):
    full_path = resource_path(json_path)
    with open(full_path, "r") as f:
        return json.load(f)
