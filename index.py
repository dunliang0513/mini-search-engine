import crawlers.techcrunch.crawler as techcrunch_crawler
from utils import reverted_index_builder, text_preprocessor, TFIDF_helper as helper, json_file_loader as loader
from utils import data_saver
import os
import json
from collections import Counter
import math


def get_corpus(dataset, stopwords_set):
    
    for url, text in dataset:
        if text != '':
            tokens = text_preprocessor.preprocess_text(text, stopwords_set)
            data_saver.save_data(url, text)
            print('URL: {}'.format(url))
            yield url, Counter(tokens)


def get_corpora(stopwords_set, visited_urls):
    techcrunch_dataset = techcrunch_crawler.crawl(visited_urls)
    # Example output:
    # Yields: ('https://techcrunch.com/2022/09/13/ashby-21-5-million-recruiting-
    # platform-startup-raises/', Counter({'ashby': 1, 'lands': 1, '21.5m': 1, 'to': 1, 'automate': 1, 'key': 1, 'aspects': 1, 'of': 1, 'recruiting...': 1}))
    yield from get_corpus(techcrunch_dataset, stopwords_set)



stopwords_file = os.path.join(os.getcwd(), 'english-stopwords-list.txt')
with open(stopwords_file, mode='r', encoding='utf-8') as f:
    stopwords_set = set(f.read().split())


index_db_file = os.path.join(os.getcwd(), 'database', 'inverted_index.json')
urls_file = os.path.join(os.getcwd(), 'database', 'urls.json')
visited_urls_file = os.path.join(os.getcwd(), 'database', 'visited_urls.json')
lengths_file = os.path.join(os.getcwd(), 'database', 'lengths.json')


visited_urls = set()
visited_urls = loader.load_json_file(visited_urls_file)


urls = []
urls = loader.load_json_file(urls_file)

        


corpora = get_corpora(stopwords_set, visited_urls)


# Build inverted index
reverted_index_builder.build_inverted_index(urls, corpora, index_db_file)
        
index_db = loader.load_json_file(index_db_file)

# # Caculate lengths for normalizing
num_docs = len(urls)
lengths = [0 for i in range(num_docs)]
for index in range(num_docs):
    # Re-construct doc vector from inverted index
    vector = []
    for term, value in index_db.items():
        df = value['doc_freq']
        postings_list = value['postings']


        if str(index) in postings_list.keys():
            weight = helper.compute_term_freq(postings_list[str(index)]) * helper.compute_inv_doc_freq(df, num_docs)
            vector.append(weight)

    lengths[index] = math.sqrt(sum((e ** 2 for e in vector)))


os.makedirs(os.path.dirname(visited_urls_file), exist_ok=True)


with open(visited_urls_file, mode='w', encoding='utf-8') as f:
    json.dump(list(visited_urls), f, ensure_ascii=False, indent=4)

with open(urls_file, mode='w', encoding='utf-8') as f:
    json.dump(urls, f, ensure_ascii=False, indent=4)

with open(lengths_file, mode='w', encoding='utf-8') as f:
    json.dump(lengths, f, ensure_ascii=False, indent=4)

print("Done building inverted index.")