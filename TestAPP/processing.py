
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import nltk
import pandas as pd
import math
import numpy
import csv
import re

class YoutubeVid:
    allData = pd.read_csv('USVideos.csv')
    stopWords = stopwords.words('english')
    regExToken = RegexpTokenizer(r'[a-zA-Z]+')
    index = allData.index
    columns = allData.columns
    processedDoc = [] 
    tok = []
    tokenized = []
    dictionary = []
    lower_tok = []
    Vector = []
    tok =allData['title']
    term = []
    pList = {}
    #print(tok)
    
    #print(range(len(tok)))
    def __init__(self):
        allData = self.allData
        regExToken = self.regExToken
        processedDoc = self.processedDoc
        Vector = self.Vector
        dictionary = self.dictionary
        pList = self.pList
        lower_tok =self.lower_tok

        for i in range(100):
            tokenized = regExToken.tokenize(allData['title'][i])
            for token in tokenized:
                token = token.lower()
                lower_tok.append(token)
                if token not in dictionary:
                    dictionary.append(token)
            processedDoc.append(lower_tok)

        for document in processedDoc:
            weight_vector = {}
            token = []
            documentFrequency = 0
            for token in document:
                if token not in weight_vector:
                    #calculate term frequency
                    termFrequency = document.count(token)/len(document)
                    documentFrequency = 10
                    lengthOfFinalDoc = len(processedDoc)
                    idf = math.log(lengthOfFinalDoc/documentFrequency)
                    curWeight = termFrequency*idf
                    weight_vector[token] = curWeight

            Vector.append(weight_vector)
        #print(Vector)
        
        for i in range(len(Vector)):
            document = Vector[i]
            for token in document:
                if token not in pList:
                    pList[token]= [] 
                pList[token].append([i, document[token]])
                pList[token] = sorted(pList[token], key=lambda x: x[1],reverse=True)

    def search(self,query):
        q= self.regExToken.tokenize(query)
        tok = []
        qWeight = {}
        tSum = {}

        for token in q:
            token = token.lower()
            tok.append(token)
        for term in tok:
            if term not in qWeight:
                termFrequency = tok.count(term)/len(tok)
                qWeight[term] = termFrequency

        for term in qWeight:
            if term in self.pList:
                for post in self.pList[term]:
                    document  = post[0]
                    if document not in tSum:
                        tSum[document] = 0
                    tSum[document] += post[1] * qWeight[term]
        tSum = sorted(tSum, key=tSum.get,reverse =True)
        print(tSum)
        return tSum


    
            


