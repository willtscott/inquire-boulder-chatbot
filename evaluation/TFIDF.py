import string
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.neighbors import KDTree

# Import local libraries
import sys
sys.path.append('../src')
import processing

class TFIDF:
    def __init__(self, faq_df, name=''):
        self.name = 'TFIDF ' + name
        self.faq = faq_df
        
        # Create corpus by joining columns
        self.features = ['Topic', 'Category', 'Department', 'question', 'answer']
        self.corpus = ''
        for f in self.features:
            self.corpus += self.faq[f] + ' '

        # Create BOW tranformer based on faq.question + faq.answer
        self.bow_transformer = CountVectorizer(analyzer=processing.text_process).fit(self.corpus)
        # Tranform faq.question itself into BOW
        self.corpus_bow = self.bow_transformer.transform(self.corpus)

        # Create TFIDF transformer based on faq.question's BOW
        self.tfidf_transformer = TfidfTransformer().fit(self.corpus_bow)
        # Transform faq.question's BOW into TFIDF
        self.corpus_tfidf = self.tfidf_transformer.transform(self.corpus_bow)
        
        print('Built', self.name)


    def max_cosine_similarity(self, query):
        """Returns (index, similarity value) of string argument q's most similar match in FAQ, determined by cosine similarity."""
        # Transform test question into BOW using BOW transformer (based on faq.question) 
        query_bow = self.bow_transformer.transform([query])
        # Transform test question's BOW into TFIDF
        query_tfidf = self.tfidf_transformer.transform(query_bow)

        sims = np.transpose(cosine_similarity(query_tfidf, self.corpus_tfidf))

        max_similarity = sims.max()
        max_index = np.argmax(sims)

        return max_index, max_similarity

    def respond(self, row):
        """Returns argument row with added columns to match questions in FAQ."""
        """Returns argument row with added columns to match questions in FAQ."""
        query = row.test_question.strip()

        index, sim = self.max_cosine_similarity(query)

        if 'match_question' in row.keys():
            row['sim_question'] = self.faq.question.iloc[index]
            row['question_success'] = row.sim_question == row.match_question

        if 'match_topic' in row.keys():
            row['sim_topic'] = self.faq.Topic.iloc[index]
            row['topic_success'] = row.sim_topic == row.match_topic

        row['max_similarity'] = round(sim, 2)
#         row['info'] = faq.answer.iloc[index]    
        return row   

    def evaluate(self, test):
        results = pd.DataFrame()

        t = test.apply(self.respond, axis=1)
        
        if 'topic_success' in t.columns:
            results[self.name] = t.topic_success
        elif 'question_success' in t.columns:
            results[self.name] = t.question_success
        
        print('Tested', self.name)        
        print('  Successes: ', sum(results[self.name]), '/', len(results), '=', 
              round(sum(results[self.name]) / len(results), 4) * 100, '%')

        return results