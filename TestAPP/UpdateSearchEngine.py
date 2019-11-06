

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
fword = []

stem= PorterStemmer()
Vector = []
term = []
pList = {}
lower_tok = []
stop_words = set(stopwords.words('english'))


# We need to tokenize the data set and lower it 
for i in range(100):
    curDoc = allData.iloc[i]['title']
    curDoc = curDoc+ allData.iloc[i]['description']
    tokenized = regExToken.tokenize(curDoc)
    
    for token in tokenized:
        tokenized = token.lower()
        if token not in stop_words:
            token = stem.stem(token)
            fword.append(token)

            if token not in dictionary:
                dictionary.append(token)
                print(dictionary)
    processedDoc.append(fword)
    print(processedDoc)
for document in tokenized:
    weight_vector = {}

    for token in document:
        if token not in weight_vector:
            TF = document.count(token)/len(document)
            DF = sum (1 for document in processedDoc if token in document)
            #print(DF)
    
    
    

    


