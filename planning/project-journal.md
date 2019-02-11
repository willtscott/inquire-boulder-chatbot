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

# Week 5
## Web-Service Cont. and Doc2Vec
Plan:
    a) continue working on dialogflow, flask, and interfacing with google cloud
    b) train a doc2vec model on answers - test by giving questions.
    c) train a doc2vec model on q&a - test by giving questions.
        - compare with all previous approaches you tried, on the test set.
    d) be able to explain 
        * what is doc2vec? 
            - An extension of the word2vec algorithm to sentences/paragraphs/documents that adds a unique document vector to the collection of word vectors and is trained simultaneously as the word vectors, resulting in a numeric representation of the document.
        * how is it useful here? 
            - The document vector provides a way to determine context of each word in the document. Doc2Vec also saves memory by representing documents as a single vector rather than a collection of vectors for each of its words. This creates a dense matrix instead of sparse ones. 
        * what is the difference between KNN and Doc2vec? 
            - In Doc2Vec the model is trained on words' inclusion with each other in the same document, which later recognizes when the words are used in the similar/different contexts.
    e) what other scenarios are use cases for doc2vec based modeling approach?
        * Web search, 

* Worked on resume, resume templates...
* Connecting flask/ngrok/local NLP with Dialogflow - figured out correct request/JSON formats for fulfillment responses.
* Added QnA Maker and Dialogflow bots to [Github project page.](https://willtscott.github.io/inquire-boulder-chatbot/)
* Looked into using Dialogflow API instead of fulfillments. Google Firebase may be the missing link?
* Summary of different Flask configurations: 
    1. All Local Option: Flask runs a localhost server that renders index.html template at '/', routes to '/dialog' after form submission, where dialog() func takes form data, matches with FAQ, and displays answer in browser.
        *** Dialogflow is aware of queries made this way and puts them in History in Console. How???
    2. Public Internet Option: Ngrok runs a public internet page to my localhost where anyone can access the form submission or /dialog page. Dialogflow uses the /dialog page to send a webhook request json and receive a response json to/from my local python program.
        A. Dialogflow fulfillment webhooks
        B. Dialogflow API
    3. Cloud Service Option: Use Docker image with all requirements and project code to run chat bot as web service with no local component. 
* Gensim Doc2Vec: Completed initial tutorial to apply to FAQ. Completed second tutorial.
* Built basic homemade gridsearch to test different parameters and differences b/w no stemming/stemmming/lemmatization
    - Initial results are not good; highest num of successess so far is 5, and even that model is not reliable
To Do:
* Docker image on Google Cloud
* Dialogflow API without web console

# Week 6
## Return to Web Service with Docker
Day 1
* Completed suggested Docker tutorials and learned basics
* Began working on Docker container for chat bot
* Worked on Hacker Rank, 1 hour
* Worked on Resume, 1 hour
Day 2
* 


