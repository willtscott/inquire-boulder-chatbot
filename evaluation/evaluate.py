import pandas as pd

# Import local libraries
import sys
sys.path.append('.')

from TFIDF import TFIDF

if __name__ == '__main__':
    faq = pd.read_csv('../data/interim/faq-text-separated.csv', keep_default_na=False)
    results = pd.DataFrame()
    
    test_questions = pd.read_csv('../data/test/test-questions.csv')
    tfidf = TFIDF(faq)
    tfidf.evaluate(test_questions, 'questions')
    
    test_topics = pd.read_excel('../../../Inquire Boulder request data- detailed open and closed - for research purposes.xlsx')
    test_topics = test_topics[['Description', 'Topic']]
    test_topics = test_topics.rename(index=str, columns={"Description": "test_question", "Topic": "match_topic"})
    tfidf.evaluate(test_topics, 'topics')