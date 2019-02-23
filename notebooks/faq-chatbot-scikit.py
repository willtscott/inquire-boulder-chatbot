#!/bin/python3

print('\tHang on while I wake up...\n')

import sys
import string
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction import stop_words
from sklearn.metrics.pairwise import cosine_similarity

q_threshold = .9
a_threshold = .6

def text_process(mess):
    """Returns list of the cleaned text in argument mess, with stopwords, punctuation removed and tokens lemmatized."""
    # Check characters to see if they are in punctuation
    nopunc = [char if char not in string.punctuation else ' ' for char in mess]

    # Join the characters again to form the string.
    nopunc = ''.join(nopunc)
    # Lemmatize???    
    # Now just remove any stopwords
    return [word.lower() for word in nopunc.split() if word.lower() not in stop_words.ENGLISH_STOP_WORDS]

def max_sim_skl(tq):
    """Returns (index, similarity value) of string argument q's most similar match in FAQ, determined by cosine similarity."""
    # Transform test question into BOW using BOW transformer (based on faq.question) 
    tq_bow = bow_transformer.transform([tq])
    # Transform test question's BOW into TFIDF
    tq_tfidf = tfidf_transformer.transform(tq_bow)
    
    sims = np.transpose(cosine_similarity(tq_tfidf, c_tfidf))
    max_s = sims.max()
    max_i = np.argmax(sims)
    
    return max_i, max_s      

def respond(row):
    """Returns argument row with added columns to match questions in FAQ."""
    query = row.test_question.strip()

    index, sim = max_sim_skl(query)

    row['sim_question'] = faq.question.iloc[index]
#     row['answer'] = faq.answer.iloc[index]
    row['max_similarity'] = round(sim, 2)
    row['success'] = row.sim_question == row.match_question
    return row   

def test_bot():
    """Apply set of test questions to similarity function and print results."""
    test = pd.read_csv('../data/interim/test-questions.csv')
    pred = test.apply(respond, axis=1) 
    pred.apply(print, axis=1)
    
def user_query():
    """Prints most similar match in FAQ to user query."""
    tq = input('\tAsk me something about Boulder.\n').strip()
    while(tq is not 'bye'):
        
        index, sim = max_sim_skl(tq)   

        print('max_similarity:', round(sim, 2))
        
        print('sim_question:', faq.question.iloc[index])
        print('answer:', faq.answer.iloc[index])
    
        tq = input('\n\tAsk me another.\n').strip()
    
if __name__ == '__main__':    
    # Read in FAQ data 
    faq = pd.read_csv('../data/interim/faq-text-separated.csv', keep_default_na=False)
    
    corpus = faq.question + ' ' + faq.answer
    
    # Create BOW tranformer based on faq.question
    bow_transformer = CountVectorizer(analyzer=text_process).fit(corpus)
    # Tranform faq.question itself into BOW
    c_bow = bow_transformer.transform(corpus)

    # Create TFIDF transformer based on faq.question's BOW
    tfidf_transformer = TfidfTransformer().fit(c_bow)
    # Transform faq.question's BOW into TFIDF
    c_tfidf = tfidf_transformer.transform(c_bow)
    
    if len(sys.argv) < 2:
        print("Usage: faq-chatbot-scikit.py [option]\n\tOptions:\n\ttest\t Tests bot using predefined test questions.\n\tuser\tAllows bot to respond to user input.")
    elif sys.argv[1] == 'test':
        test_bot()
    elif sys.argv[1] == 'user':
        user_query()
    else:
        print("Usage: faq-chatbot-scikit.py [option]\n\tOptions:\n\ttest\t Tests bot using predefined test questions.\n\tuser\tAllows bot to respond to user input.")
    
        