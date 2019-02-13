#!/bin/python3
print('\tHang on while I wake up...\n')

import os
import sys
import string
import numpy as np
import pandas as pd

import json
import dialogflow

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction import stop_words
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem import WordNetLemmatizer

from flask import Flask, redirect, url_for, request, render_template, jsonify

wordnet_lemmatizer = WordNetLemmatizer()

app = Flask(__name__)

def lem(words):
    """Returns list of lemmas from arugment list of words."""
    lem_sentence=[]
    for word in words:
        lem_sentence.append(wordnet_lemmatizer.lemmatize(word))
    return lem_sentence

def text_process(mess):
    """Returns list of the cleaned text in argument mess, with stopwords, punctuation removed and tokens lemmatized."""
    clean = [char if char not in string.punctuation else ' ' for char in mess]
    clean = ''.join(clean)
    clean = [word.lower() for word in clean.split() if word.lower() not in stop_words.ENGLISH_STOP_WORDS] 
    clean = lem(clean)
    
    return clean

def max_sim_skl(tq):
    """Returns (index, similarity value) of string argument q's most similar match in FAQ, determined by cosine similarity."""
    # Transform test question into BOW using BOW transformer
    tq_bow = bow_transformer.transform([tq])
    # Transform test question's BOW into TFIDF
    tq_tfidf = tfidf_transformer.transform(tq_bow)
    
    sims = np.transpose(cosine_similarity(tq_tfidf, c_tfidf))
    max_s = sims.max()
    max_i = np.argmax(sims)
    
    return max_i, max_s      
    
def match_query(tq):
    """Prints most similar match in FAQ to user query."""
    index, sim = max_sim_skl(tq)   
    return faq.answer.iloc[index]

# Read in FAQ data 
path = os.path.dirname(os.path.abspath(__file__))

faq = pd.read_csv('faq-text-separated.csv', keep_default_na=False)

corpus = faq.question + ' ' + faq.answer

# Create BOW tranformer based on faq.question + faq.answer
bow_transformer = CountVectorizer(analyzer=text_process).fit(corpus)
# Tranform faq.question itself into BOW
c_bow = bow_transformer.transform(corpus)

# Create TFIDF transformer based on faq.question's BOW
tfidf_transformer = TfidfTransformer().fit(c_bow)
# Transform faq.question's BOW into TFIDF
c_tfidf = tfidf_transformer.transform(c_bow)

@app.route('/')
def index():
    """This route at the home page renders the index.html template with blank variables."""
    return render_template('index.html', query = '', answer = '')

@app.route('/dialog', methods = ['POST'])
def dialog():
    """This route uses the POST method to request user input, parses it according to json or form data, prints the locally-determined Dialogflow API intent, and returns a json response based on skl matching with the FAQ."""
    if request.is_json:
        req = request.get_json(force=True)
        message = req.get('queryResult').get('queryText')
        print('*' * 20)
    else:
        message = request.form['message']
    
    project_id = os.getenv('DIALOGFLOW_PROJECT_ID')
    fulfillment_text = detect_intent_texts(project_id, "unique", message, 'en')
    
    response_text = match_query(message)
    print("LOCAL_MATCH: " + response_text)
    
    if request.is_json:
        return jsonify({
            "fulfillmentText": response_text,
            "fulfillmentMessages": [
            {
              "text": {
                "text": [response_text]
              }
            }
            ],
            "source": "<Text response>"
            })
    else:
        return render_template('index.html', query = message, answer = response_text)

def detect_intent_texts(project_id, session_id, text, language_code):
    """Given parameters of the Dialogflow project ID, session ID, user entry text, and language code ('en' for English), returns a fulfillment text based on detected intent from Dialogflow API."""
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)

    if text:
        text_input = dialogflow.types.TextInput(
            text=text, language_code=language_code)
        query_input = dialogflow.types.QueryInput(text=text_input)
        response = session_client.detect_intent(
            session=session, query_input=query_input)
        print('=' * 20)
        print('Query text: {}'.format(response.query_result.query_text))
        print('Detected intent: {} (confidence: {})\n'.format(
            response.query_result.intent.display_name,
            response.query_result.intent_detection_confidence))
        print('Fulfillment text: {}\n'.format(
            response.query_result.fulfillment_text))

        return response.query_result.fulfillment_text
    
if __name__ == '__main__':    
    app.run(host='0.0.0.0', port=80, debug = True)
    
