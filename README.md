inquire-boulder-chatbot
==============================
A chatbot for the Inquire Boulder FAQ<br>
https://willtscott.github.io/inquire-boulder-chatbot/


<iframe
    allow="microphone;"
    width="500"
    height="430"
    style="padding: 50px;"
    src="https://console.dialogflow.com/api-client/demo/embedded/inquire-boulder-faq">
</iframe>

Keywords: Python, scikit-learn, NLTK, spaCy, GenSim, Doc2Vec, Flask, Docker, Google Cloud Products, Dialogflow

This project is written in Python using Jupyter Notebooks for exploration and prototyping and Flask and Docker for deployment on Google Cloud Products. I used NLTK and spaCy for NLP (including tokenizing and lemmatization) and scikit-learn for vectorization and similarity matching with Bag-of-Words (BOW), Term Frequency-Inverse Document Frequency (TFIDF), and cosine similarity. The Flask app uses the Dialogflow API to connect with a Dialogflow agent via webhooks, which provides the public interface.

The goal is to provide a working, better-than-baseline chatbot that is publicly accessible and can be flexibly scaled up and/or iterated with different datasets.

The text dataset for the FAQ was obtained from a webmaster at the City of Boulder. Thanks goes to Nicolia Eldred-Skemp for help acquiring this data. 

The process is explained in further detail by my blog post here:
https://medium.com/p/faq-chatbot-mvp-871ab7db94cc?source=email-566e6f2dac22--writer.postDistributed&sk=a5f7b76973a08ca2ee44d5ac09aaf8e8

Other Links:<br>

Inquire Boulder:<br>
https://user.govoutreach.com/boulder/faq.php

Boulder Open Data Portal:<br>
https://bouldercolorado.gov/open-data/areas-of-inquiry

Related Project:<br>
https://github.com/doc1000/email_sorting




Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── test           <- Handmade dataset for testing accuracy.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, ca nonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── test_environment.py <- tests correct version of python


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
