import numpy as np
import pandas as pd
# import dialogflow

import processing

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics.pairwise import cosine_similarity

from flask import render_template, jsonify


class BotServer:
    def __init__(self, file_path):
        """
        Initialize corpus, bag-of-words, and TFIDF from CSV file at argument
        file_path.
        """
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

    def tfidf_similarity(self, query):
        """
        Returns (index, similarity value) of string argument query's most similar
        match in FAQ, determined by cosine similarity.
        """
        # Transform test question into BOW using BOW transformer
        query_bow = self.bow_transformer.transform([query])
        # Transform test question's BOW into TFIDF
        query_tfidf = self.tfidf_transformer.transform(query_bow)

        # Calculate cosine similarity and return maximum value with accompanying index
        similarities = np.transpose(cosine_similarity(query_tfidf, self.corpus_tfidf))
        max_similarity = similarities.max()
        max_index = np.argmax(similarities)

        return max_index, max_similarity

    def match_query(self, query):
        """
        Prints most similar match in FAQ to user query, adding text concerning
        service requests if relevant.
        """
        index, similarity = self.tfidf_similarity(query)

        response = self.faq.answer.iloc[index]
        key_word = 'service request'

        if key_word in response.lower() or key_word in query.lower():
            response += '\n\n'
            response += 'If you would like to submit a service request, please visit '
            response += 'https://user.govoutreach.com/boulder/faq.php?cmd=shell'
            response += ' or call 303-441-3388.'

        return response

    def bot_dialog(self, request):
        """
        Given the argument POST request, parse it according to json or form data,
        print the locally-determined Dialogflow API intent, and return a json
        response based on sklearn matching within the FAQ.
        """
        if request.is_json:
            req = request.get_json(force=True)
            message = req.get('queryResult').get('queryText')
        else:
            message = request.form['message']

        response_text = self.match_query(message)

        # Return json file as webhook response or render html template locally
        if request.is_json:
            return jsonify({
                "fulfillmentText": response_text,
                "fulfillmentMessages": [{
                      "text": {
                        "text": [response_text]
                      }
                }],
                "source": "<Text response>"
                })
        else:
            return render_template('index.html', query=message, answer=response_text)
