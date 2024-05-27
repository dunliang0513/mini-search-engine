import sys
import os
import math
from utils import text_preprocessor, TFIDF_helper as helper, json_file_loader as loader
from collections import Counter


def search_and_return_top_twenty(query):
    # Load data from files
    db_file = os.path.join(os.getcwd(), 'database', 'inverted_index.json')
    urls_file = os.path.join(os.getcwd(), 'database', 'urls.json')
    lengths_file = os.path.join(os.getcwd(), 'database', 'lengths.json')
    stopwords_file = os.path.join(os.getcwd(), 'english-stopwords-list.txt')

    with open(stopwords_file, mode='r', encoding='utf-8') as f:
        stopwords_set = set(f.read().split())

    urls = loader.load_json_file(urls_file)
    lengths = loader.load_json_file(lengths_file)

    # Load inverted index
    index_db = loader.load_json_file(db_file)

    # Construct vocabulary from inverted index
    vocabulary = set(index_db.keys())
    num_docs = len(urls)

    # Preprocess query
    tokens = text_preprocessor.preprocess_text(query, stopwords_set)
    tokens = [token for token in tokens if token in vocabulary]

    # Calculate weights for query
    query_bow = Counter(tokens)
    query_weights = {}

    for term, freq in query_bow.items():
        df = index_db[term]['doc_freq']
        query_weights[term] = helper.compute_inv_doc_freq(df, num_docs) * helper.compute_term_freq(freq)

    # Normalize query weights
    query_length = math.sqrt(sum((e ** 2 for e in query_weights.values())))
    for term, value in query_weights.items():
        query_weights[term] = value / query_length

    # Calculate scores
    scores = [[i, 0] for i in range(num_docs)]
    for term, query_weight in query_weights.items():
        df = index_db[term]['doc_freq']
        postings_list = index_db[term]['postings']
        for docId, freq in postings_list.items():
            docId = int(docId)
            doc_weight = helper.compute_inv_doc_freq(df, num_docs) * helper.compute_term_freq(freq)
            scores[docId][1] += query_weight * doc_weight / lengths[docId]

    # Ranking
    # Sort scores and display results
    scores.sort(key=lambda e: e[1], reverse=True)

    top_twenty_scores = []
    all_zero = True

    for index, score in scores[:20]:
        if score == 0:
            break
        top_twenty_scores.append((urls[index], score))
        all_zero = False

    if all_zero:
        return "No matches found"
    else:
        return top_twenty_scores