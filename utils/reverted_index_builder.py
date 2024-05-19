import json
from collections import defaultdict



def build_inverted_index(url_list, crawl_generator, index_file):
    index_db = defaultdict(lambda: {'doc_freq': 0, 'postings': {}})


    for url, bag_of_words in crawl_generator:
        # Preprocess the text (e.g., tokenize, remove stopwords, stem)
        url_list.append(url)
        index = len(url_list) - 1


        
        

        # Update the inverted index
        for term, freq in bag_of_words.items():
            index_file[term]['doc_freq'] += 1
            index_file[term]['postings'][index] = freq

        index += 1

    # Write the inverted index to the JSON file
    with open(index_file, 'w', encoding='utf-8') as f:
        json.dump(index_db, f, ensure_ascii=False, indent=2)
