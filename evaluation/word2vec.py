# Training Custom Word2Vec Model

import string
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from gensim.models import Word2Vec
from sklearn.feature_extraction import stop_words

def w2v_text_process(mess):
    """Returns list of the cleaned text in argument string mess, with stopwords, punctuation removed and tokens lemmatized."""
    clean = [char if char not in string.punctuation else ' ' for char in mess]
    clean = ''.join(clean)
    clean = [word.lower() for word in clean.split() if word.lower() not in stop_words.ENGLISH_STOP_WORDS] 
    return clean

# Creating a feature vector by averaging all embeddings for all sentences
def embedding_feats(list_of_lists):
    DIMENSION = 300
    zero_vector = np.zeros(DIMENSION)
    feats = []
    for list_of_tokens in list_of_lists:
        feat_for_this = zero_vector
        count_for_this = 0
        for token in list_of_tokens:
            if token in our_model:
                feat_for_this += our_model[token]
                count_for_this += 1
        feats.append(feat_for_this/count_for_this) 
    return feats

def max_sim_w2v(tq):
    """Returns (index, similarity value) of string argument q's most similar match in FAQ, determined by cosine similarity."""
    query = [w2v_text_process(tq)]
    query = embedding_feats(query)
 
    sims = np.transpose(cosine_similarity(query, corpus_vectors))

    max_s = sims.max()
    max_i = np.argmax(sims)
    
    return max_i, max_s 

def cosine_respond_w2v(row):
    """Returns argument row with new info columns to match with questions in FAQ."""
    query = row.test_question.strip()

    index, sim = max_sim_w2v(query)

    row['sim_question'] = faq.question.iloc[index]
    row['max_similarity'] = round(sim, 2)
    row['success'] = row.sim_question == row.match_question
    row['info'] = faq.answer.iloc[index]
    return row   

if __name__ == '__main__':
    # Read in data files
    faq = pd.read_csv('../data/interim/faq-text-separated.csv', keep_default_na=False)
    test = pd.read_csv('../data/test/test-questions.csv')
    results = pd.DataFrame()

    # Create corpus by joining columns
    features = ['Topic', 'Category', 'Department', 'question', 'answer']
    corpus = ''
    for f in features:
        corpus += faq[f] + ' '

    corpus = [w2v_text_process(x) for x in corpus]
    
    #Build the model, by selecting the parameters. 
    our_model = Word2Vec(corpus, size=300, window=5, min_count=1, workers=4)
    #Save the model
    our_model.save("../models/tempmodel.w2v")
    #Inspect the model by looking for the most similar words for a test word. 
    [print(x) for x in our_model.wv.most_similar('dogs', topn=5)]
    
    corpus_vectors = embedding_feats(corpus)
    
    test = test.apply(cosine_respond_w2v, axis=1)
    results['w2v'] = test.success
    print(test[['test_question', 'success']])
    print('Successes: ', sum(results.w2v))
    