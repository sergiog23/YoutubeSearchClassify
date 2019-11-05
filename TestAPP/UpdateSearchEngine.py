

from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import nltk
import pandas as pd
import math
import numpy
import csv
import re


allData = pd.read_csv('USVideos.csv')
regExToken = RegexpTokenizer(r'[a-zA-Z]+')
processedDoc = [] 
tok = []
tokenized = []
dictionary = []
curDoc = []

stem= PorterStemmer()
Vector = []
term = []
pList = {}
stop_words = set(stopwords.words('english'))


# We need to tokenize the data set and lower it 
for i in range(100):
    curDoc = allData.iloc[i]['title']
    curDoc = curDoc+ allData.iloc[i]['description']
    tokenized = regExToken.tokenize(curDoc)
        tokenized = tokenized.tolower()
    for token in tokenized:
        if token not in dictionary:
            dictionary.append(token)
for document in tokenized:
    weight_vector = {}

    for token in document:
        if token not in weight_vector:
            TF = document.count(token)/len(document)
            DF = sum (1 for document in processedDoc if token in document)
    
    
    

    


