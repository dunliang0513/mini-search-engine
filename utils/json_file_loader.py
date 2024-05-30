import os
import json

def load_json_file(file_path):
    data = []
    if os.path.isfile(file_path):
        with open(file_path, 'r') as f:
            if os.stat(file_path).st_size != 0:
                data = json.load(f)
    return data