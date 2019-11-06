

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
for i in range(10):
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
                #print(dictionary)
    processedDoc.append(fword)

for document in processedDoc:
    
    weight_vector = {}

    for term in document:
        if term not in weight_vector:
            N = len(processedDoc)
            TF = document.count(term)/len(document)
            DF = sum (1 for document in processedDoc if term in document)
            Weight = TF * math.log10(N/DF+1)
    Vector.append(weight_vector)

for i in range(10):
    document = Vector[i]
    print("nseo")
    for token in document:
        print("cuales")
        if token not in pList:
            pList[token] = []
            print("no")
        pList[token].append([i,document[token]])
        pList[token] = sorted(pList[token],key = lambda x: x[1],reverse=True)
        print(pList)
        print("yes")

    
    
    

    


