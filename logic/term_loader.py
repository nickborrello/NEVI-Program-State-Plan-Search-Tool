import json

def load_terms(json_path):
    with open(json_path, "r") as f:
        return json.load(f)

