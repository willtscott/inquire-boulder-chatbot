# Evaluator class provides base class for evaluating various approaches to query and topic matching in FAQ
import pandas as pd

# Import local libraries
import sys
sys.path.append('../src')
import processing

class Evaluator:
    name = ''
    faq = ''
    features = ''
    corpus = ''
    vectors = ''
    
    def __init__(self, faq_df, feature_list, label=''):
        """Initialize object with FAQ DataFrame and optional naming label, building corpus, vectorizer, and vectors."""
        self.name = 'Evaluator' + '.' + label
        self.faq = faq_df
        
        # Create corpus by joining columns
        self.features = feature_list
        self.corpus = ''
        for f in self.features:
            self.corpus += self.faq[f] + ' '
            
        self.vectors = self.vectorize()
            
        print('Built:', self.name)
        
    def vectorize(self):
        print('Define vectorize() function for each extended class.')
        
    def max_similarity(self, query):
        print('Define max_similarity() function for each extended class.')

    def respond(self, row):
        """Returns argument row with new columns added containing attempted match in FAQ."""
        query = row.test_question.strip()

        index, sim = self.max_similarity(query)

        if 'match_question' in row.keys():
            row['sim_question'] = self.faq.question.iloc[index]
            row['question_success'] = row.sim_question == row.match_question

        if 'match_topic' in row.keys():
            row['sim_topic'] = self.faq.Topic.iloc[index]
            row['topic_success'] = row.sim_topic == row.match_topic

        row['max_similarity'] = round(sim, 2)
#         row['info'] = faq.answer.iloc[index]    
        return row 

    def evaluate(self, test_set, label = ''):
        """Given test DataFrame and optional naming label, evaluate and print match success rate, 
        returning results DataFrame with column of True/False values for each question's match success."""
        results = pd.DataFrame()
        eval_name = self.name + ' ' +  label

        t = test_set.apply(self.respond, axis=1)
        
        if 'topic_success' in t.columns:
            results[eval_name] = t.topic_success
        elif 'question_success' in t.columns:
            results[eval_name] = t.question_success
        
        print('Tested:', eval_name)        
        print('  Successes: ', sum(results[eval_name]), '/', len(results), '=', 
              round(sum(results[eval_name]) / len(results), 4) * 100, '%')
        
        print(t[['match_question', 'sim_question']])

        return results