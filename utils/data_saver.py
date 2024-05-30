import json
import os
from utils import json_file_loader as loader

data = []

data_file = os.path.join(os.getcwd(), 'database', 'data.json')
data = loader.load_json_file(data_file)

def save_data(url, text):
    data.append({'URL': url, 'text': text})
    with open(data_file, mode='w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
