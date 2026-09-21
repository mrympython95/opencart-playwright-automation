import json


def read_json_data(file_path: str):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)