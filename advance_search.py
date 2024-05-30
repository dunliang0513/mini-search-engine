from txtai.embeddings import Embeddings
from utils import json_file_loader as loader
import os

# Implement advance searching using txtai library 
def create_embeddings_index():
    """
    This function creates an embeddings index using the txtai library.

    It loads data from a JSON file, extracts the text and URL from each entry, and creates an index of the text using the txtai library.
    The embeddings are then saved to a file for future use.

    Returns:
        tuple: a tuple containing the embeddings object and a list of URLs corresponding to each text entry in the embeddings index
    """
    
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

    embeddings.save("embeddings.tar.gz")

    return embeddings, urls
   

def advance_search_and_return_top_ten(query, embeddings, urls):
    """
    This function performs an advanced search on the embeddings index and returns the top ten results.

    It uses the txtai library to search the embeddings index for text entries that are semantically similar to the given query.
    It then returns the URLs corresponding to the top ten results, along with their similarity scores.

    Args:
        query (str): the search query
        embeddings (Embeddings): the embeddings object
        urls (list): a list of URLs corresponding to each text entry in the embeddings index

    Returns:
        list: a list of tuples, where each tuple contains a URL and a similarity score
    """
    
    results = embeddings.search(query, limit=10)

    urls_and_scores = [(urls[result[0]], result[1]) for result in results]

    return urls_and_scores


