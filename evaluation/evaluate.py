print('Importing libs...')

import pandas as pd

# Import local libraries
import sys
sys.path.append('.')

from TFIDF import TFIDF
from W2V import W2V

if __name__ == '__main__':
    
    print('Reading files...')
    faq = pd.read_csv('../data/interim/faq-text-separated.csv', keep_default_na=False)    
    test_questions = pd.read_csv('../data/test/test-questions.csv')
    features = ['Topic', 'Category', 'Department', 'question', 'answer']
    
    # Evaluate Word2Vec on questions
    w2v = W2V(faq, features, 'W2V')
    w2v.evaluate(test_questions, 'questions')
#     print(w2v.corpus.head())
#     print('-----')
#     [print(x) for x in w2v.clean_corpus[:5]]
   
    
    # Evaluate TFIDF on questions and Topics
#     tfidf = TFIDF(faq, features, 'TFIDF')
#     tfidf.evaluate(test_questions, 'questions')
    
#     test_topics = pd.read_excel('../../../Inquire Boulder request data- detailed open and closed - for research purposes.xlsx')
#     test_topics = test_topics[['Description', 'Topic']]
#     test_topics = test_topics.rename(index=str, columns={"Description": "test_question", "Topic": "match_topic"})
#     tfidf.evaluate(test_topics, 'topics')