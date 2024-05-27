from txtai.embeddings import Embeddings
from utils import json_file_loader as loader
import os

def create_embeddings_index():
    embeddings = Embeddings({
        "path": "sentence-transformers/all-MiniLM-L6-v2"
    })

    data = []
    data_file = os.path.join(os.getcwd(), 'database', 'data.json')
    data = loader.load_json_file(data_file)

    texts = [entry["text"] for entry in data]
    urls = [entry["URL"] for entry in data]

    txtai_data = []

    i = 0

    for text in texts:
        txtai_data.append((i, text, None))
        i += 1

    embeddings.index(txtai_data)

    return embeddings, urls

def advance_search_and_return_top_ten(query, embeddings, urls):
    results = embeddings.search(query, limit=10)

    urls_and_scores = [(urls[result[0]], result[1]) for result in results]

    return urls_and_scores
