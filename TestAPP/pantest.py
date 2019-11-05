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
yes = 'goP4Z5wyOlM,17.14.11,"Iraq-Iran earthquake: Deadly tremor hits border region - BBC News","BBC News",25,2017-11-12T21:16:40.000Z,"bbc"|"bbc news"|"news"|"iran"|"iran news"|"iraq"|"iraq news"|"earthquake"|"breaking news"|"Iraq-Iran earthquake",34785,308,26,413,https://i.ytimg.com/vi/goP4Z5wyOlM/default.jpg,False,False,False,"A strong 7.2-magnitude earthquake has rattled the northern Iraq-Iran border region, killing at least 10 people.\nThe quake struck in the evening local time south of the Iraqi town of Halabja at a depth of 33.9 km (21 miles), the US Geological Survey (USGS) said.\nAt least six people died in western Iran, state media said, with another four reported dead in Iraq.\n\n\nPlease subscribe HERE http://bit.ly/1rbfUog\n\nWorld In Pictures https://www.youtube.com/playlist?list=PLS3XGZxi7cBX37n4R0UGJN-TLiQOm7ZTP\nBig Hitters https://www.youtube.com/playlist?list=PLS3XGZxi7cBUME-LUrFkDwFmiEc3jwMXP\nJust Good News https://www.youtube.com/playlist?list=PLS3XGZxi7cBUsYo_P26cjihXLN-k3w246"'

tokenized = regExToken.tokenize(yes)
print(tokenized)