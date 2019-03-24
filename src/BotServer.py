import os
import sys
import string
import numpy as np
import pandas as pd

import processing

import json
import dialogflow

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics.pairwise import cosine_similarity

from flask import Flask, redirect, url_for, request, render_template, jsonify

class BotServer:
    def __init__(self, file_path):
        """Initialize corpus, bag-of-words, and TFIDF from CSV file at argument file_path."""
        # Read in FAQ data 
        self.faq = pd.read_csv(file_path, keep_default_na=False)
        self.corpus = self.faq.question + ' ' + self.faq.answer
        
        # Create BOW tranformer based on faq.question + faq.answer
        self.bow_transformer = CountVectorizer(analyzer=processing.text_process).fit(self.corpus)
        # Tranform faq.question itself into BOW
        self.corpus_bow = self.bow_transformer.transform(self.corpus)

        # Create TFIDF transformer based on faq.question's BOW
        self.tfidf_transformer = TfidfTransformer().fit(self.corpus_bow)
        # Transform faq.question's BOW into TFIDF
        self.corpus_tfidf = self.tfidf_transformer.transform(self.corpus_bow)

    def most_similar_sklearn(self, query):
        """Returns (index, similarity value) of string argument query's most similar match in FAQ, determined by cosine similarity."""
        # Transform test question into BOW using BOW transformer
        query_bow = self.bow_transformer.transform([query])
        # Transform test question's BOW into TFIDF
        query_tfidf = self.tfidf_transformer.transform(query_bow)

        similarities = np.transpose(cosine_similarity(query_tfidf, self.corpus_tfidf))
        max_similarity = similarities.max()
        max_index = np.argmax(similarities)

        return max_index, max_similarity      

    def match_query(self, query):
        """Prints most similar match in FAQ to user query."""
        index, similarity = self.most_similar_sklearn(query)   
        return self.faq.answer.iloc[index]

    def detect_intent_texts(self, project_id, session_id, text, language_code):
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
    
    def bot_dialog(self, request):
        """Given the argument POST request, parse it according to json or form data, print the locally-determined Dialogflow API intent, and return a json response based on sklearn matching with the FAQ."""
        if request.is_json:
            req = request.get_json(force=True)
            message = req.get('queryResult').get('queryText')
        else:
            message = request.form['message']

        project_id = os.getenv('DIALOGFLOW_PROJECT_ID')
        fulfillment_text = self.detect_intent_texts(project_id, "unique", message, 'en')

        response_text = self.match_query(message)
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
