# AppDataMining
Datamining Term Project  

Link to project: [APP](http://sergiog23.pythonanywhere.com/)
# Phase I Search
In this phase I implemented Search using Tf-idf to score and rank the rows in the document according to my query. 
# Phase II Classifier
In this phase I implemented a classifier using Naive Bayes to classify the description given by the user
# Phase III Image recognition 


## Instructions on how to run code
This webapp is currently hosted on pythonanywhere and can be used by going to the link at the top.  

To download this project and run on local machine:

1.Download zip file  \
2.Extract files\
3.On a terminal cd into AppDataMining\
4.cd into AppDataMining\
5.run python3 app.py \
6.This will run an give you a link to the webapp \
7.Ctrl-c on the link to open web app.

Note: You will need to have have some python libraries in order for you to run:\
NLTK, pandas,numpy,flask

Files:\
**Search.py**: In this file we declare the class AppDataMining where I implement Tf-idf and perform Search.\
**Classifier.py**: In this file I implement the Naive Bayes classifer\
**app.py**:In this file serves as the entry point to the web application we get the user's query and score it against the tf-idf scores.
