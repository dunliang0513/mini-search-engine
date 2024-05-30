import json
from collections import defaultdict
import utils.json_file_loader as loader


def build_inverted_index(url_list, crawl_generator, index_file):
    """
    This function builds an inverted index from a list of URLs and a generator that produces bags of words for each URL.

    An inverted index is a data structure used to make full text search more efficient. It's a dictionary where each key is a term found in the document collection, each value is a dictionary which contains a document frequency value and a postings list of documents where the term appears.

    Args:
        url_list (list): A list of URLs to be indexed.
        crawl_generator (generator): A generator that yields a tuple for each URL. The first element of the tuple is the URL, and the second element is a bag of words for the URL.
        index_file (str): The path to the JSON file where the inverted index should be saved.

    Returns:
        None. The function writes the inverted index to a JSON file.
    """
    
    index_db = defaultdict(lambda: {'doc_freq': 0, 'postings': {}})

    index_db.update(loader.load_json_file(index_file))

    for url, bag_of_words in crawl_generator:
        # Preprocess the text (e.g., tokenize, remove stopwords, stem)
        url_list.append(url)
        index = len(url_list) - 1

        # Update the inverted index
        for term, freq in bag_of_words.items():
            index_db[term]['doc_freq'] += 1
            index_db[term]['postings'][index] = freq

        index += 1

    # Write the inverted index to the JSON file
    with open(index_file, 'w', encoding='utf-8') as f:
        json.dump(index_db, f, ensure_ascii=False, indent=2)
