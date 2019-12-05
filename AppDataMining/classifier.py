
import math
import pandas as pd
import numpy
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from collections import defaultdict
from search import *

#Function to concatenate text
def link_text(categories, document, c):
    txt = []
    for i in range(len(document)):
        if c in categories[i]:
            txt.extend(document[i])
    return txt
# function to count the number of occurences in document 
def doc_count(document, c):
    document_in_c = 0
    for doc in document:
        if c in doc:
            document_in_c += 1
    return document_in_c
    
class AppClassifer:
    #Use pandas libary to read CSV file
    vidInfo = pd.read_csv('apps.csv')
    #Use nltk library to tokenize free text file to only include words only no special characters
    tokenizer = RegexpTokenizer(r'[a-zA-Z]+')
    # Use nltk stop words to remove common words like 'the' 'to' 'so'
    stops = stopwords.words('english')
    # use porter stemmer to reduce a word to its word stem
    stemmer = PorterStemmer()
    # create a list where we will the store the final document after it has been preprocessed
    final_document = []
    # create a dictionary of words that are found after processing
    vocabulary = []
    # create a list of all categories present in the app.csv that will serve as a Ground truth in classifier
    categories = []
    # create a dictionary that contains the prior probability 
    prior = {}
    condprob = defaultdict(dict)
    counts = []

    def __init__(self):
        vidInfo = self.vidInfo
        tokenizer = self.tokenizer
        stops = self.stops
        stemmer = self.stemmer
        final_document = self.final_document
        vocabulary = self.vocabulary
        categories = self.categories
        prior = self.prior
        condprob = self.condprob
        counts = self.counts

        for i in range(200):
            tokens = tokenizer.tokenize(vidInfo['track_name'][i])
            tokens += tokenizer.tokenize(vidInfo['app_desc'][i])
            final_tokens = []
            for token in tokens:
                token = token.lower()
                if token not in stops:
                    token = stemmer.stem(token)
                    final_tokens.append(token)
                    if token not in vocabulary:
                        vocabulary.append(token)
            final_document.append(final_tokens)

        total_document = len(final_document)
        total_term = len(vocabulary)
        # get the category for each row in processed document 
        ratings = vidInfo['prime_genre']

        for rating in ratings:
            if rating not in categories:
                categories.append(rating)

        for c in categories:
            document_in_c = doc_count(ratings, c)
            prior[c] = document_in_c/float(total_document)
            text_in_c = link_text(ratings, final_document, c)

            for term in vocabulary:
                Tct = text_in_c.count(term)
                counts.append(Tct)
                condprob[term][c] = (Tct + 1)/(len(text_in_c) + total_term)
    # I will Call this function from the app.py and it will process the users query 
    #Similar to what this class does to the data by tokenizeing it and removing stop words and stemming
    def classify(self, query):
        query_vocab = []
        terms = self.tokenizer.tokenize(query)
        for term in terms:
            term = term.lower()
            if term not in self.stops:
                term = self.stemmer.stem(term)
                query_vocab.append(term)

        score = {}
        for c in self.categories:
            score[c] = self.prior[c]
            for term in query_vocab:
                if term in self.condprob:
                    score[c] *= self.condprob[term][c]
                
        total_score = sum(score.values())
        classification = {}
        for c in sorted(score, key=score.get, reverse=True):
            classification[c] = score[c]/float(total_score)
        return classification
