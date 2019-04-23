# W2V class extends Evaluator class to evaluate accuracy of similarity via averaged Word2Vec vectors.

import string
import numpy as np
import pandas as pd
from sklearn.feature_extraction import stop_words
from sklearn.metrics.pairwise import cosine_similarity
from gensim.models import Word2Vec


# Import local libraries
import sys
sys.path.append('../src')

import processing
from Evaluator import Evaluator

class W2V(Evaluator):
    clean_corpus = ''
    model = ''
    
    def w2v_text_process(self, mess):
        """Returns list of the cleaned text in argument string mess, with stopwords, punctuation removed."""
        clean = [char if char not in string.punctuation else ' ' for char in mess]
        clean = ''.join(clean)
        clean = [word.lower() for word in clean.split() if word.lower() not in stop_words.ENGLISH_STOP_WORDS] 
        return clean
    
    # Create a feature vector for each sentence by averaging all word embeddings in that sentence
    def embedding_feats(self, list_of_lists, DIMENSION = 300):
        zero_vector = np.zeros(DIMENSION)
        feats = []
        for list_of_tokens in list_of_lists:
            feat_for_this = zero_vector
            count_for_this = 0
            for token in list_of_tokens:
                if token in self.model:
                    feat_for_this += self.model[token]
                    count_for_this += 1
            feats.append(feat_for_this/count_for_this) 
        return feats
    
    def vectorize(self):
        self.clean_corpus = [self.w2v_text_process(entry) for entry in self.corpus]
        
        #Build the model, by selecting the parameters. 
        self.model = Word2Vec(self.clean_corpus, size=300, window=5, min_count=1, workers=4)
        #Save the model
        self.model.save("../models/tempmodel.w2v")
        #Inspect the model by looking for the most similar words for a test word. 
        [print(x) for x in self.model.wv.most_similar('dogs', topn=5)]

        self.vectors = self.embedding_feats(self.clean_corpus)

    def max_similarity(self, query):
        """Returns (index, similarity value) of string argument q's most similar match in FAQ, determined by cosine similarity."""
        q = [self.w2v_text_process(query)]
        q = self.embedding_feats(q)

        sims = np.transpose(cosine_similarity(q, self.vectors))

        max_s = sims.max()
        max_i = np.argmax(sims)

        return max_i, max_s 


    