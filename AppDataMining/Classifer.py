

from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import nltk
import pandas as pd
import math
import numpy
import csv
import re
from Search.py import *



allData = pd.read_csv('YoutubeVideos.csv')
regExToken = RegexpTokenizer(r'[a-zA-Z]+')
index = allData.index
columns = allData.columns
processedDoc = [] 
tok = []
tokenized = []
dictionary = []
lower_tok = []
stem= PorterStemmer()
Vector = []
term = []
pList = {}
stop_words = set(stopwords.words('english'))
    

# loop through 100 records in USVideos CSV
for i in range(10):
    # create a list that tokenized the titles of all the records 
    tokenized = regExToken.tokenize(allData['title'][i])
    tokenized = tokenized + regExToken.tokenize(allData['description'][i])
    print(tokenized)
    for token in tokenized:
        token = token.lower()
        lower_tok.append(token)
        if token not in dictionary:
            dictionary.append(token)
    processedDoc.append(lower_tok)


for document in processedDoc:
    weight_vector = {}

    for token in document:
        if token not in weight_vector:
            #calculate term frequency
            termFrequency = document.count(token)/len(document)
            lengthOfFinalDoc = len(processedDoc)
            DF = sum( 1 for document in processedDoc if token in document)
            #print(DF)
            idf = math.log(lengthOfFinalDoc/DF+1)
            curWeight = termFrequency*idf
            weight_vector[token] = curWeight
            (weight_vector)
    Vector.append(weight_vector)
   # print(Vector)
        
for i in range(len(Vector)):
    document = Vector[i]
    for token in document:
            if token not in pList:
                pList[token]= [] 
            pList[token].append([i, document[token]])
            pList[token] = sorted(pList[token], key=lambda x: x[1],reverse=True)
            #print(pList)
query = 'we are getting married married married'
q= regExToken.tokenize(query)
#print(q)
tokens= []
weight = {}
ans = {}
for t in q:
    t = t.lower()
    #if t not in stop_words:
     #   t = stem.stem(t)
    tokens.append(t)

#print(tokens)
for term in tokens:
    #print(term)
    if term not in weight:
            tf = tokens.count(term)/len(tokens)
           # print(tf)
            weight[term] = tf
            #print(weight)
for term in weight:
    if term in pList:
      print(term)
      for p in pList[term]:
        document = p[0]
        if document not in ans:
              ans[document] = 0
        ans[document] += p[1] * weight[term]
        #print(ans)
ans = sorted(ans, key = ans.get,reverse=True)
#print(ans)
    

