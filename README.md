# AppDataMining
Datamining Term Project  

Link to project: [CLICK HERE FOR THE LIVE WEB APPLICATION](http://sergioguerrero.pythonanywhere.com/)
# Phase I Search
In this phase I implemented Search using Tf-idf to score and rank the rows in the document according to my query. 
# Phase II Classifier
In this phase I implemented a classifier using Naive Bayes to classify the description given by the user
# Phase III Image recognition 
In this phase I implement a an Image Captioning model that uses Visual Attention to generate captions. I then used that trained model to caption a subset of image on the FLICKR dataset and did TF-IDF on the captions to search for images.

## Instructions on how to run code
This webapp is currently hosted on pythonanywhere and can be used by going to the link at the top.  

To download this project and run on local machine:

1.Download zip file  \
2.Extract files\
3.On a terminal cd into AppDataMining\
4.cd into AppDataMining\
5.run python3 app.py \
6.This will run an give you a link to the webapp \
7.Ctrl-c on the link to open web app.\
This is the link to click if you are running on local host. \
**http://127.0.0.1:5000/** \
Note: You will need to have have some python libraries in order for you to run:\
NLTK, pandas,numpy,flask

Files:\
**Search.py**: In this file we declare the class AppDataMining where I implement Tf-idf and perform Search.\
**Classifier.py**: In this file I implement the Naive Bayes classifer\
**app.py**:In this file serves as the entry point to the web application we get the user's query and score it against the tf-idf scores.\
**ImageCaptioner.py** In this file we declare the Image class where I perform Search over the trained image data set that contains captioned images

