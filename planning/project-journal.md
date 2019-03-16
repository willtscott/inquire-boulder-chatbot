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
        *** Dialogflow is aware of queries made this way and puts them in History in Console. How? API.
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
* Successfully built working Docker container and respository for flask-dialogflow-bot sample: 
    - docker run -p 4000:80 willtscott/online-test:first
    - localhost:4000
* Following tutorial to serve app via Kubernetes cluster: https://cloud.google.com/kubernetes-engine/docs/tutorials/hello-app 
* Worked on Hacker Rank, 1 hr
* Worked on Resume, many hours
Day 3
* Researched resume format and mistakes, updated resume a little. 
* Ran sample Docker container->public repository->container cluster->deployed app->internet app->scaled app->new version
* Ran flask-bot container->repository->cluster->deployed?->but no internet????
* Met with Jeremie to discuss resume, branding, and application strategies
Day 4
* Researching flask->docker->cloud->web pipeline to determine the path of least resistance and work out current issues.
    - Continuing with this series to see it through: https://docs.docker.com/get-started/part6/
        - No success. This tutorial doesnt use cloud services.
    - This one didn't get me any closer: https://medium.com/analytics-vidhya/how-to-deploy-machine-learning-models-using-flask-docker-and-google-cloud-platform-gcp-6e7bf1b339d5
* Decided I'm probably overthinking this for now and that I don't need the cluster->swarm steps as long as my container runs and deploys the app to the web.

# Week 7
## GCP and Project Cleanup 
Day 1
* Getting sample bot back online through Docker and GCP
* Saw an interesting option in Docker Hub to link to Github account and rebuild container automatically on git push
* If I use webhooks instead of Dialogflow API then I don't have to include API in app, reducing container size.
* Is Dialogflow API key json file in Docker container visible to others? Container is public.
* My web preview of the sample bot running on GCP through Docker only available to my google account. Needs simple deployment!
* Several more tutorials later.... 
    - I think this is all the parts I need: Python -> Flask -> Docker -> GCP App Engine 
    - yaml file doesn't need to specify ports?    
Day 2
* Finally got the bot deployed!!! 
    - Used this tutorial:https://cloud.google.com/kubernetes-engine/docs/tutorials/hello-app
    - Used these commands:
        ---set up---
        docker build -t willtscott/inquire-boulder-bot:v1 .
        docker push willtscott/inquire-boulder-bot:v1
        docker run --rm -p 8080:8080 willtscott/inquire-boulder-bot:v1
        ---deploy---
        gcloud config set compute/zone us-central1-b
        gcloud container clusters create bot-cluster --num-nodes=2
        kubectl run bot-web --image=willtscott/inquire-boulder-bot:v1 --port 8080
        kubectl expose deployment bot-web --type=LoadBalancer --port 80 --target-port 8080
        kubectl get service
        *update webhook URL in Dialogflow Fulfilment section
        ---clean up---
        kubectl delete deployment bot-web --namespace=default
        kubectl delete service bot-web
        gcloud container clusters delete bot-cluster 
        docker image ls -a
        docker image rm [IMAGE_ID]
        *** Delete docker images ***
    - All ports are 8080. The previous issues must have had to do with the port defined in python, Docker, yaml file, and command line not matching. Possibly could be cleaned up further by removing port expose in Docker file and ports in yaml file.
    - I believe yaml file is not currently used as I'm running and exposing the serice throught CL. Here's a link about how to use service files: https://medium.com/google-cloud/deploy-python-application-to-google-cloud-with-docker-and-kubernetes-db33ee9fbed3
    - In the future I will probably need to add gunicorn instead of relying solely on flask
    - Ideally, an App Engine address would be better, and maybe lots cheaper on resources.
* What is the difference between using webhook or Dialogflow API? Both needed or just one?
Day 3
* Began cleaning and reorganizing Flask app
    - Created text processing function library
    - Created BotServer class library
* Next step: Get Dialogflow webhooks working with GCP app server, or use API if possible
    - Big question: How to decide whether to use Dialogflow knowledge base or custom ML?
* Tested Dialogflow's default ML against test_questions
    - Results: 4 successes 
    - 256 characters is the max input length. Can I increase it?
* Fixed a false validation in the test_questions set. 
    - TODO: Rerun sandbox notebook to update accuracy tests!
Day 4
* Discovered error in flask app:
    - Execution not working: 'main.py not found' (Fixed by turning off development mode, but why occured?)
    - When successfully executed, google authentification is not working correctly
* Turned off and deleted GCP services to save credit
* Sent a follow-up email to careers@ada.support
* Submitted early pull request
Day 5
* Working on flask bug
# Week 8 
## Debugging, Drafting Blog, Revising Resume
Day 1
* Discovered .flaskenv file with environmental variables had been lost in the cleanup. Reinstated from github, but is needed?
    - This turned out to be the issue. 
* Tried out theory that authentication was failing due to no connection b/w app and google, but ngrok version didn't work either, so this is probably not the problem. Best ngrok tutorial: https://www.pragnakalp.com/dialogflow-fulfillment-webhook-tutorial/
* Found it! Lost the env var GOOGLE_APPLICATION_CREDENTIALS="[FULL_PATH]/Inquire-Boulder-FAQ-8ed88c62ebc8.json"
    - How to set local path?
    - Used Dockerfile ENV command to set env var with local path
Day 2
* Emailed Gordon Gibson, ML lead at Ada Toronto.
Day 3
* Worked on blog draft, decided to pursue descriptive narrative rather than instructional directions
Day 4
* Tested sample bot deployment on GCP again and it worked. Added a few more commands to the execution order to clean up.
* Worked on blog draft.
* Received email reply from Gordon Gibson, passing on hiring but offering to meet for lunch in Toronto.
Day 5
* Worked on resume
* Replied to Gordon's email - asked for feedback on application. 
# Week 9
## Applying, Interview Prep, Blog Post
Day 1
* Worked on resume
* Applied to Backcountry with Cover Letter: http://jobs.jobvite.com/backcountry/job/oYIh9fwQ
Day 2
* Received feedback from Gordon Gibson of Ada, received recommendation to apply at Prodigy Games from Sowmya, asked Edouard if he has contacts there.
* Tested Google Cloud service bot with Dialogflow webhook fulfillment - works! Just have to update webhook URL in Dialogflow Fulfilment section after deployment on Google Cloud.
* Hand-cleaned data set through entry 165. There's quite a bit of incompatible content in here. Could be a biggish job for future maintenance.
Day 3    
* New job leads: Mozilla from Rocio Ng, Edouard knows someone at Prodigy Games....(Hassan)
* Cranked Knowledge Results Preference in Dialogflow all the way up to ensure Boulder answers are preferred.
* Updated project dataset with newer hand-cleaned version (added 19 questions.) Newly hand-cleaned set has potential to 
* Applied to Prodigy Games: https://jobs.lever.co/prodigygame/74bb6b78-9f77-462f-bb87-a18d0e2de031
Day 4
* Worked on Hacker Rank for a bit.
* Worked on blog post.
Day 5
* Finished up blog draft.
# Week 10
## Blog Post, Interview Prep
Day 1
* Submitted blog post to Towards Data Science after adding pics and conclusion paragraph
* Received resume advice from Ronnie
Day 2
* Blog post published by TDS!
* Readme summary
Day 3
* Received email from Prodigy Games and scheduled call for 2:15 the next day.
* Did Python and SQL practice
* Redeployed bot on GCP to try to provide better responses to people checking it out through the blog post.
Day 4
* Python and SQL practice
* Interview prep
* Phone interview with Prodigy Games - OK, I think. Waiting on coding challenge.
* Bot used ~$3 over 24hrs with a few queries from randos
Day 5
* Practiced SQL
* Took Prodigy coding challenge 
* Bot used about $3 more today
* Realized that hand-cleaned dataset needs to be updated in Dialogflow KnowledgeBase as well



