#!/bin/python3

print('\tHang on while I wake up...\n')

import pandas as pd
import spacy

q_threshold = .9
a_threshold = .6

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
#         if d.similarity(q) > .9:
#             print('\t', max_s, ': ', d)
    
    return max_i, max_s        

def test_bot(row):
    query = nlp(row.test_question.strip())

    index, sim = max_sim(query, q_docs)

    row['guess'] = str(sim) + ': ' + str(q_docs[index])
    row['info'] = a_docs[index]
    
    print(row.test_question)
    print('----')
    print(row.guess)
    print('\n\n')
    
if __name__ == '__main__':    
    # Read in FAQ data to spaCy documents
    nlp = spacy.load('en_core_web_md')  # make sure to use larger model!
    faq = pd.read_csv('../data/interim/faq-text-separated.csv', keep_default_na=False)
    test = pd.read_csv('../data/interim/test-questions.csv', keep_default_na=False)
    
    q_docs = [nlp(entry) for entry in faq.question]
    a_docs = [nlp(entry) for entry in faq.answer]
    
    test.apply(test_bot, axis=1)
    
#     query = nlp(input('\tAsk me a question about Boulder!\n').strip())

#     while query.text != 'bye':        
#         print('\tLet me look this up...\n')

#         index, sim = max_sim(query, q_docs)

#         print('\tHighest Similarity Value: ', sim, '\n')
        
#         if sim < q_threshold:
#             index, sim = max_sim(query, a_docs)
            
#         if sim < a_threshold:
#             print("\tMy apologies, I can't find a good answer for that.")
#         else:
#             print('\t', str(q_docs[index]).strip(), '\n')
#             print('\t', str(a_docs[index]).strip(), '\n')
        
        
#         query = nlp(input('\tAsk me another!\n').strip())
#     else:
#         print('\tBye for now!')
        