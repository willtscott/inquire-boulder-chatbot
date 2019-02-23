inquire-boulder-chatbot
==============================
A chatbot for the Inquire Boulder FAQ<br>
https://willtscott.github.io/inquire-boulder-chatbot/

# Dialogflow sample 

<iframe
    allow="microphone;"
    width="350"
    height="430"
    src="https://console.dialogflow.com/api-client/demo/embedded/fd95fdff-97f7-4f3a-8651-e8d4b3fbb88f">
</iframe>

# QnA Maker sample 

<iframe 
    src='https://webchat.botframework.com/embed/inquire-boulder-faq?s=K2GKDgFUiQI.cwA.2t4.AnAFP_nPafG7hHGRjVLMOBHh8PtuztseJCCyTEGxKrg' 
    style='min-width: 400px; width: 50%; min-height: 500px; align: middle;'>
</iframe>

Inquire Boulder:<br>
https://user.govoutreach.com/boulder/faq.php

Boulder Open Data Portal:<br>
https://bouldercolorado.gov/open-data/areas-of-inquiry

Related Projects:<br>
https://github.com/doc1000/email_sorting

Thanks to Nicolia Eldred-Skemp for help acquiring the Inquire Boulder FAQ text. 



Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
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
    └── tox.ini            <- tox file with settings for running tox; see tox.testrun.org


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
