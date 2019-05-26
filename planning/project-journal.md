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
    - Used this tutorial: https://cloud.google.com/kubernetes-engine/docs/tutorials/hello-app
    - Used these commands:
        ---set up---
        docker build -t willtscott/inquire-boulder-bot:v1 .
        docker push willtscott/inquire-boulder-bot:v1
        docker run --rm -p 8080:8080 willtscott/inquire-boulder-bot:v1
        ---deploy---
        gcloud config set compute/zone us-central1-b
        gcloud container clusters create bot-cluster --num-nodes=1
        kubectl run bot-web --image=willtscott/inquire-boulder-bot:v1 --port 8080
        kubectl expose deployment bot-web --type=LoadBalancer --port 80 --target-port 8080
        kubectl get service
        echo "***Update webhook URL in Dialogflow Fulfilment section with: URL + '/dialog'"
        ---deploy new version---
        docker build -t willtscott/inquire-boulder-bot:v2 .
        docker push willtscott/inquire-boulder-bot:v2
        kubectl set image deployment/bot-web bot-web=willtscott/inquire-boulder-bot:v2
        ---clean up---
        kubectl delete deployment bot-web --namespace=default
        kubectl delete service bot-web
        gcloud config set compute/zone us-central1-b
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
Day 2
* Blog post published by TDS!
* Readme summary
Day 3
* Did Python and SQL practice
* Redeployed bot on GCP to try to provide better responses to people checking it out through the blog post.
Day 4
* Python and SQL practice
* Bot used ~$3 over 24hrs with a few queries from randos
Day 5
* Bot used about $3 more today
* Realized that hand-cleaned dataset needs to be updated in Dialogflow KnowledgeBase as well

# Week 11
Day 2
* Cleaning up sandbox and creating testing pipeline
Day 3
* Adding more testing to sandbox for mulitnomial naive-bayes - SmartRegs questions mishandled in dataset are breaking this.
Day 5
* Seems that GCP services are costing a steady $3/day, that's about $1100/year.
* Worked on bot accuracy: detect_intent function is failing due to authentication reasons. Eject API?

# Week 12
Day 1
* Office hours: 
    Should I apply to jr roles or shoot higher? Both
    Contact WilderAI? done
    Feedback from Prodigy? none
    cold-contact senior members? both
    Perhaps use averaged Word2Vec instead of TFIDF for chatbot...
Day 3
* Determined that Dialogflow API can indeed be eliminated currently
Day 4
* Finished hand-cleaning dataset up to entry 251 (end), although it is far from perfect for chatbot application.
Day 6
* Redefined q-n-a pair separation function and used new results to find errors in dataset, so revisited hand-cleaning.

# Week 13
Day 1
* Attended Databricks Unified Analytics workshop - Takeaway: Faster/Better than plain Spark w/ tools to bring engineering and ML together.
* Updated test set with stripped strings and started experimenting with ngrams in CountVectorizer
Day 3
* Updating text processing notebooks into script sequence
Day 4
* Continued updating of script sequence from processing notebook
* GCP credit: $222.40 with 258 days remaining. Loss of $26 in last 10 days = $2.60/day
* Successfully redeployed new version of bot, minus Dialogflow API, with new commands. Reset service running on one cluster.

# Week 14 
Day 1
* Office Hours w/ SM
* Testing out IBM Watson integration - interface not friendly, but seems pretty powerful already.
* GCP credit: $216.27 with 255 days remaining, averaging $6 over 3 days = $2/day = cheaper without Dialogflow API!?
Day 2
* Met with AC from Onehot Labs
* Downloaded Word2Vec model pretrained on Google News
Day 3
* Attended CWA talk about Effects of AI on Business and Labor
* Attempted to run pretrained Word2Vec - model loading took 1hr17min...........
* Attempting to check similarity in loaded model also overloaded processing
Day 4
* GCP credit at $211.70 with 253 days remaining. Loss of $11 in 5 days = $2+/day
* Testing Word2Vec on custom trained model - works, but not great success (1/20)
* Pretrained W2V took only 13 min this time.... - Using it still locks system. Researched W2V models on Kaggle.
* Working on improving lemmas with POS and 
Day 5
* Applied Google x2, Section
* SQL, Python practice
* Implemented POS lemmas, alternate processing strategies, and custom count vectorizor in sandbox
Day 6
* Incorporated new functionality to test Topic matching on large proprietary set. 
* Working on new automated evaluation scripts, classes.

# Week 15
Day 1
* Office Hours w/ SM 
* Improving modularity of automated evaluation in the chatbot
* Making/following up on connections
* Job research - Keyvalues.com
* Javascript practice
Day 2
* Watson practice (Assistant = lots of manual labor)
Day 3 
* Networking - Twitter and Uber are hiring
* Idea: Split project into 2 repos, 1 offline for research and evaluation, 1 online working model 
Day 4
* Applications
Day 5
* Applications
* Webinar - unwalled Medium article
* Abstracted Evaluator base class, updated TFIDF class
* Building word2vec class into auto evaluation - not getting same results as before (?)

# Week 16
Day 1
* Fixed W2V auto-evaluation
* Added KDTree auto-evaluation
Day 2
* Dialogflow console: Convert each qna pair to intent? (not working on Google's end....)
* Watson research
* Watson class mentoring
* CfB Brigade meetup - mixer with civic data folks next week?
Day 3
* ACRONAME meeting
* BIC job fair
Day 4
* Applications, connections
* Python practice
* H20.ai/Oracle Data Cloud presentation
Day 5
* Python practice
* ACRONAME interview
* $189.06 credit and 238 days remaining on GCP. Loss of $22.64 in 15 days = $1.51/day

# Week 17
Day 1
* Created build and deployment scripts for Docker-GCP (in week16 branch)
* Added basic functionality to submit service requests when relevant (in week16 branch)

# Week 18
Day 1
* Explored Dialogflow Console options - nothing conclusive determined. Unhelpful response 
  from support request.

# Week 19
Day 1
* Updated build and deployment scripts
* Linted src/ with flake8

# Week 20
Day 1
* Updated index.html page with added info
* Used build script to push new container version (v3 = 554MB, 50MB larger than v2, same size as v1)
* On GCP: $151.16 credit and 213 days remaining, $1.50/day
* Created bucket for cloud scripts on Google cloud storage and copied them to Cloud shell
* Attempted to update deployment with new version - no change? 
* TODO: Try taking down current version, putting it back up, and then updating with new version.
Day 2
* Took down current version, put up new version. Fixed a few errors in scripts along the way. 
* Service not actually running: Container doesn't seem to be active! 
* TO TRY: Rebuild/deploy with GCP container registry - This doesn't seem necessary but could be beneficial. 
    docker build -t gcr.io/${PROJECT_ID}/hello-app:v1 .
    gcloud auth configure-docker
    docker push gcr.io/${PROJECT_ID}/hello-app:v1
    kubectl run hello-web --image=gcr.io/${PROJECT_ID}/hello-app:v1 --port 8080
* Bot service v3 returning auth error: Try adding diaglogflow back in (requirements and import)
Day 3
* Looked into v3 auth issues: Dialogflow was being imported - possible cause?
* Linted scripts and evaluation dirs
* Google Cloud Run could be a simpler and cheaper way to run this service
Day 4
* AUTHENTICATION SOLVED - Putting version numbers into requirements.txt caused docker build to fail quietly, therefore build was never pushed to registry and previous (broken) version of tag was deployed. Removed version numbers from requirements.txt file.

