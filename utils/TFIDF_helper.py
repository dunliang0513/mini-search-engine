import math

def compute_term_freq(freq):
    return 1 + math.log10(freq)

def compute_inv_doc_freq(doc_freq, num_docs):
    return math.log10(num_docs / doc_freq)

def compute_tf_idf(term_freq, inv_doc_freq):
    return term_freq * inv_doc_freq