# Preprocess raw text Excel file into CSV using spaCy to tokenize sentences

import numpy as np
import pandas as pd
import string
import unicodedata
import spacy

def preprocess(entry):
    '''
    Normalize string argument entry, remove new line characters, add space after '?' chars, and return entry with trailing space.
    '''
    entry = entry.replace('\n', ' ')
    entry = unicodedata.normalize("NFKD", entry)
    entry = entry.replace('?', '? ')
    return entry + ' '

def sentence_tokenize(entry):
    '''
    Tokenize string argument entry into sentences using spaCy, then join sentences with double new lines and return as string.
    '''
    doc = nlp(entry)
    sentences = list(doc.sents)
    sentences = '\n\n'.join([(s.text) for s in sentences])
    return sentences




if __name__ == '__main__':
    
    spacy_model = 'en_core_web_sm'
    print('Loading spaCy model', spacy_model, '...')
    nlp = spacy.load(spacy_model)
    print('-Done.')

    raw = pd.read_excel("../data/raw/inquire-boulder-faq-text/inquire-boulder-active-faqs-2019-01-02.xls.xlsx")

    faq = raw.drop(labels=('Active'), axis=1).dropna()

    faq.FAQ = faq.FAQ.apply(preprocess)

    faq.FAQ = faq.FAQ.apply(sentence_tokenize)

    faq.to_csv('../data/interim/faq-text-preprocessed.csv', index=False)

    # The next step is hand-cleaning dataset to remove irregular formatting errors

