## Project Plan

**Project duration:** Jan 5 - March 5 2018  

**General steps:**
- Basics: Project setup, Getting to know the data set, NLP libraries, chatbot APIs etc.
- Strong Baseline: Building a strong baseline based on user question similarity to existing FAQs/Answers
- Web-service: Setting up a UI/Rest API building on the baseline, hosting on AWS/Google Cloud or wherever, Docker if needed. 
- Improving the baseline: using better similarity measures, chatbot APIs etc and further experimentation
- Wrapping up: code cleaning, documentation, possibly a blog post. Communication to City of Boulder team etc.

**Tentative Timeline:**
- Basics: Week 1
- Strong baseline: Week 2-3
- Web-service: Week 4
- Improving the baseline: Week 5,6
- Wrapping up: Week 7,8

**Useful Resources for different steps:**
- Basics:  
    1. [Cookie cutter data science project](https://drivendata.github.io/cookiecutter-data-science/) - only as a reference for project organization. Not a strict template.  
    2. Potential Python NLP Libraries to explore: NLTK, Spacy, Gensim Textacy, AllenNLP (preferably in that order, just to understand what are the different NLP functions they support)
    3. Chatbot APIs (E.g., Microsoft's)
  
- Strong baseline: 
    1. Ideas to understand: Cosine similarity, Semantic similarity, Nearest neighbors 

- Web service:
    1. Python libraries: Flask, Bottle, Django etc (There are many. I vote for Flask, but it is good to know about one or two other options, just in case some interview question comes up)
    2. Basics of using one of: AWS, Google cloud or other options to host python based web-services
    3. Docker images and their use 
    
 - Improving the baseline:
    1. Chatbot APIs, what functions do they provide, what they cannot do, where it fits our purpose (Can fill this later, as we know more)
    
 - Wrapping up:
    1. Code organization, Linting the code (e.g., pylint library) etc (Will add relevant notes/guidelines later)
 
