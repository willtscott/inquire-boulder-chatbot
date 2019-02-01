# Week 1
## Data Exploration and Library, NLP Research
* Acquired FAQ text data from Nicolia at the City of Boulder and began processing and cleaning.
* Organized the project with cookiecutter.
* Wrote a regex to separate questiosns from answers in the data set.
* Created a basic functional FAQ chatbot using Microsoft's QnA Maker. 
* Researched NLP libraries NLTK, spaCy and started EDA notebook.
* Acquired FAQ request log from Nicolia at City of Boulder. 

# Week 2
## Simple Baseline and Library, NLP Research
* Coded baseline chatbot for command-line in Python, using spaCy's built-in functions for cleaning and matching.
* Researched similarity functions for NLP problems, such as cosine and semantic.
* Looked into Gensim and AllenNLP libraries, and also more spaCy.

# Week 3
## Strong Baseline and NLP Similarity Research
* Hand-cleaned FAQ dataset up to index 55
* Compiled test set of 20 questions invented or pulled from historic FAQ request log and paired them with questions from the FAQ.
* Researched cosine similarity and KDTree implementations, looked into soft cosine which seems promising
* Implemented my own text processing and similarity functions using scikit-learn and NLTK libraries.
    - Removed punction and stopwords, create bag-of-words and then TFIDF vectors.
    - Added lemmatization with NLTK and experienced significant improvement in similarity matching.
* Coded new baseline chatbot for command-line in Python, using cosine similarity.
* Compared new cosine similarity and KDTree nearest-neighbor approaches to previous spaCy and QnA Maker results, finding that cosine and nearest neighbors performed much better than spaCy and slightly better than QnA Maker.

# Week 4
## Web-Service
* Started project journal :)
* Added one-liner dosctrings to some previous functions.
* Created Google Dialogflow account to experiment with built-in ML and to join with Flask.
* Researched and worked a few tutorial excercises for Flask.
* Read this article and thought about using FAQ Department->Category->Topic to match context.
    - https://chatbotsmagazine.com/why-you-cant-just-convert-faqs-into-a-chatbot-1-1-92205141d008
* Set up super-basic working browser chatbot with Flask and scikit-learn approach
* 