
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import nltk
import pandas as pd
import math
import numpy

class YoutubeVid:
    allData = pd.read_csv('USVideos.csv')
    stopWords = stopwords.words('english')
    regExToken = RegexpTokenizer(r'[a-zA-Z]+')
    index = allData.index
    columns = allData.columns

    processedDoc = [] 
    tok = []

    tok = allData['title']
    for row in tok:
        tokenized = nltk.word_tokenize(tok['title'][row])

    wordDictA = dict.fromkeys(tokenized,0)
    for word in tokenized:
        wordDictA[word]+=1
    #pd.DataFrame([wordDictA])    

    def ComputeTf(wordDict, bow):
        tfDict = {}
        bowCount = len(bow)
        for word, count in wordDict.items():
            tfDict[word] = count/float(bowCount)
        return tfDict
    tf = ComputeTf(wordDictA, tokenized)
    print(tf)
 