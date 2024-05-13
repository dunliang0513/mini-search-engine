def build_inverted_index(url_list, corpora, index_db):
    for url, bag_of_word in corpora:
        url_list.append(url)
        index = len(url_list) - 1

        for term, freq in bag_of_word.items():
            if index_db.get('term', None) is None:
                index_db[term] = {}

            if index_db.get('doc_freq', None) is None:
                index_db[term]['doc_freq'] = 0

            if index_db.get('posting', None) is None:
                index_db[term]['posting'] = {}
            
            index_db[term]['doc_freq'] += 1
            index_db[term]['posting'][index] = freq

        index_db.sync()
    
    index_db.sync()