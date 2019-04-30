# KDTREE class extends Evaluator class to evaluate accuracy of Term Frequency, Inverse Document Frequency using KD Tree data structure

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.neighbors import KDTree

# Import local libraries
import sys
sys.path.append('../src')

import processing
from Evaluator import Evaluator

class KDTREE(Evaluator):
    bow_transformer = ''
    tfidf_transformer = ''
    tree = ''
    
    def vectorize(self):
        """Returns vectors of transformed corpus, using Bag of Words and Term Frequency/Inverse Document Frequency."""
        # Create BOW tranformer based on corpus
        self.bow_transformer = CountVectorizer(analyzer=processing.text_process).fit(self.corpus)
        # Tranform corpus itself into BOW
        corpus_bow = self.bow_transformer.transform(self.corpus)

        # Create TFIDF transformer based on corpus's BOW
        self.tfidf_transformer = TfidfTransformer().fit(corpus_bow)
        # Transform corpus BOW into TFIDF   
        tfidf = self.tfidf_transformer.transform(corpus_bow)
        
        # Put corpus TFIDF into KD tree
        self.tree = KDTree(tfidf.toarray(), metric='euclidean')

        return tfidf
    
    def max_similarity(self, q):
        """Returns (index, similarity value) of string argument q's most similar match in FAQ, determined by nearest neighbor in KDTree of TFIDF vectors."""
        # Transform test question into BOW using BOW transformer 
        tq_bow = self.bow_transformer.transform([q])
        # Transform test question's BOW into TFIDF
        tq_tfidf = self.tfidf_transformer.transform(tq_bow)

        # k=2 nearest neighbors where k1 = identity
        nearest_dist, nearest_ind = self.tree.query(tq_tfidf.toarray(), k=2)  
        
        return nearest_ind[0][0], nearest_dist[0][0]
    

    