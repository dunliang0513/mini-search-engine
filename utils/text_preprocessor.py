import re
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import WhitespaceTokenizer
from autocorrect import Speller

def remove_stopwords(document, stopwords_list):
    tokenizer = WhitespaceTokenizer()
    tokens =[]
    for token in tokenizer.tokenize(document):
        if token not in stopwords_list and token.isalpha():
            # stemmed_token = PorterStemmer().stem(token)
            tokens.append(token)

    return ' '.join(tokens)


def normalize_text(document):
    # Normalize numbers and dates
    document = re.sub(r'\d+', 'NUM', document)
    # Add more normalization rules as needed
    return document

def spell_check_text(document):
    spell = Speller()
    corrected_text = [spell(word) for word in document.split()]
    return ' '.join(corrected_text)

def preprocess_text(document, stopwords_list):
    document = document.lower()
    document = normalize_text(document)
    document = spell_check_text(document)
    document = remove_stopwords(document, stopwords_list)
    document = document.split()
    return document
