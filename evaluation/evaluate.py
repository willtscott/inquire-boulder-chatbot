import pandas as pd

# Import local libraries
import sys
sys.path.append('.')

from TFIDF import TFIDF

if __name__ == '__main__':
    faq = pd.read_csv('../data/interim/faq-text-separated.csv', keep_default_na=False)
    
    test_questions = pd.read_csv('../data/test/test-questions.csv')
    
    test_topics = pd.read_excel('../../../Inquire Boulder request data- detailed open and closed - for research purposes.xlsx')
    test_topics = test_topics[['Description', 'Topic']]
    test_topics = test_topics.rename(index=str, columns={"Description": "test_question", "Topic": "match_topic"})

    results = pd.DataFrame()
    
    tfidf_questions = TFIDF(faq, 'questions')
    tfidf_topics = TFIDF(faq, 'topics')
    
    tfidf_questions.evaluate(test_questions)
    tfidf_topics.evaluate(test_topics)