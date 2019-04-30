print('Importing libs...')

import pandas as pd

# Import local libraries
import sys
sys.path.append('.')

from TFIDF import TFIDF
from W2V import W2V
from KDTREE import KDTREE

if __name__ == '__main__':
    
    print('-' * 80)
    print('Reading files...')
    
    faq = pd.read_csv('../data/interim/faq-text-separated.csv', keep_default_na=False)    
    test_questions = pd.read_csv('../data/test/test-questions.csv')
    features = ['Topic', 'Category', 'Department', 'question', 'answer']
    
    test_topics = pd.read_excel('../../../Inquire Boulder request data- detailed open and closed - for research purposes.xlsx')
    test_topics = test_topics[['Description', 'Topic']]
    test_topics = test_topics.rename(index=str, columns={"Description": "test_question", "Topic": "match_topic"})
    
    # Evaluate KDTree on questions
    kdtree = KDTREE(faq, features, 'KDTREE')
    kdtree.evaluate(test_questions, 'questions')    
    
    # Evaluate Word2Vec on questions
    w2v = W2V(faq, features, 'W2V')
    w2v.evaluate(test_questions, 'questions') 
    
#     w2v.evaluate(test_topics, 'topics')
    
    # Evaluate TFIDF on questions and Topics
    tfidf = TFIDF(faq, features, 'TFIDF')
    tfidf.evaluate(test_questions, 'questions')
   
    tfidf.evaluate(test_topics, 'topics')
    
