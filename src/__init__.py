#!/bin/python3

print('Hang on second while I wake up...\n')

import pandas as pd
import spacy

q_threshold = .8
a_threshold = .5

def max_sim(q, docs):
    """
    Take user query in form of spaCy document, find question that has the highest similarity,
    and return the associated answer from FAQ if the similarity is above threshold value.
    """
    max_i = 0
    max_s = 0
    ms = []
    for i, d in enumerate(docs):
        if d.similarity(q) > max_s:
            max_s = d.similarity(q)
            max_i = i
        if d.similarity(q) > .9:
            print(max_s, ': ', d)
    
    return max_i, max_s        
    
if __name__ == '__main__':    
    nlp = spacy.load('en_core_web_md')  # make sure to use larger model!
    print('spacy load')
    faq = pd.read_csv('../data/interim/faq-text-separated.csv', keep_default_na=False)
    q_docs = [nlp(entry) for entry in faq.question]
    print('qs')
    a_docs = [nlp(entry) for entry in faq.answer]
    print('as')
    
    query = nlp(input('Ask me a question about Boulder!\n').strip())

    while query.text != 'bye':        
        print('Let me look this up...\n')
        print('Here\'s what I found:\n')

        index, sim = max_sim(query, q_docs)

        if sim < q_threshold:
            index, sim = max_sim(query, a_docs)
            
        if sim < a_threshold:
            print("My apologies, I can't find a good answer for that.")
        else:
            print(q_docs[index], '\n')
            print(a_docs[index], '\n')
        
        query = nlp(input('Ask me another!\n').strip())
    else:
        print('Bye!')
        