from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import pandas as pd
import math
import numpy


class YoutubeSearch:
    df = pd.read_csv('USvideos.csv')
    regExToken = RegexpTokenizer(r'[a-zA-Z]+')
    stopWords = stopwords.words('english')

    processedDoc = []
    weightVector = []
    stemmer = PorterStemmer()
    postList = []
    def __init__(self):		
        df = self.df
        regExToken = self.regExToken
        stopWords = self.stopWords
        weightVector = self.weightVector
        stemmer = self.stemmer
        postList = self.postList
        for i in len(df):
            tok = regExToken.tokenize(df['title'][i])
            tok = tok + regExToken.tokenize(df['channel_title'][i])
            tok = tok + regExToken.tokenize(df['description'][i])
            print(tok)
            stemmedTokens = []
            for t in tok:
                tok = tok.lower()
                if tok not in stopWords:
                    tok = stemmer.stem(tok)
                    stemmedTokens.append(tok)
            processedDoc.append(stemmedTokens)
  
        for document in processedDoc:
            weightVectorr = {}
            for term in document:
                if term not in weightVector:
                    tf = document.count(term)/len(document)
                    df = sum(1 for document in processedDoc if term in document)
                    n = len(processedDoc)
                    weight = tf * math.log10(n/df)
                    weightVectorr[term] = weight
            weightVector.append(weightVectorr)

        for i in range(len(weightVector)):
            document = weightVector[i]

            for t in document:
                if t not in postList:
                    postList[t] = []
                postList[t].append([i, document[t]])
                postList[t] = sorted(postList[t], key=lambda x: x[1], reverse=True)
        print(processedDoc)
        
    def search(self, query):
        q = self.regExToken.tokenize(query)
        tokens = []
        query_weight = {}
        for t in q: 
            t = t.lower()
            if t not in self.stopWords:
                t = self.stemmer.stem(t)
                tokens.append(t)
        for term in tokens:
            if term not in query_weight:
                tf = tokens.count(term)/len(tokens)
                query_weight[term] = tf
        ans = {}
        for term in query_weight:
            if term in self.postList:
                for post in self.postList[term]:
                    document = post[0]
                    if document not in ans:
                        ans[document] = 0 
                    ans[document] += post[1] * query_weight[term]
        ans = sorted(ans, key=ans.get, reverse=True)
        print(ans)
        return ans
    
