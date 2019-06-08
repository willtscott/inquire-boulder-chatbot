inquire-boulder-chatbot
==============================
A chatbot for the Inquire Boulder FAQ<br>
Interactive Web Demo: https://willtscott.github.io/inquire-boulder-chatbot/

Keywords: Python, scikit-learn, NLTK, spaCy, GenSim, Doc2Vec, Flask, Docker, Google Cloud Products, Dialogflow

This project is written in Python using Jupyter Notebooks for exploration and prototyping and Flask and Docker for deployment on Google Cloud Products. I used NLTK and spaCy for NLP (including tokenizing and lemmatization) and scikit-learn for vectorization and similarity matching with Bag-of-Words (BOW), Term Frequency-Inverse Document Frequency (TFIDF), and cosine similarity. The cloud service connects with a Dialogflow agent via webhooks, which provides the public interface.

The goal is to provide a working, better-than-baseline chatbot that is publicly accessible and can be flexibly scaled up and/or iterated with different datasets.

The process is explained in further detail by my article:
https://towardsdatascience.com/faq-chatbot-mvp-871ab7db94cc

The text dataset for the FAQ was obtained from a webmaster at the City of Boulder. Thanks goes to Nicolia Eldred-Skemp for help acquiring this data. 

Other Links:<br>

Inquire Boulder:<br>
https://user.govoutreach.com/boulder/faq.php

Boulder Open Data Portal:<br>
https://bouldercolorado.gov/open-data/areas-of-inquiry

Related Project by Doster Esh:<br>
https://github.com/doc1000/email_sorting


Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── test           <- Handmade dataset for testing accuracy.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, ca nonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    |
    ├── evaluation         <- Scripts to automate model evaluation
    |
    ├── index.html         <- Github.io project page 
    |
    ├── lib                <- External tools library
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks for EDA and prototyping
    |   
    ├── planning           <- Project goals and journal
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │
    ├── scripts            <- Scripts to automate text cleaning and test set creation
    │   ├── deployment     <- Scripts for containerization and cloud deployment   
    │    
    ├── vizualization       <- Images for EDA and masks to generate images
    │
    └── test_environment.py <- tests correct version of python

--------

Project organization based on the cookiecutter data science project template.
https://drivendata.github.io/cookiecutter-data-science/
