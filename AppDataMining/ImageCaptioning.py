import math
import pandas as pd
import numpy
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from collections import defaultdict 
import os 

class Image:
    # Read data from CSV files
    imageInfo = pd.read_csv("images.csv")
    tokenizer = RegexpTokenizer(r'[a-zA-Z]+')
    # Use nltk stop words to remove common words like 'the' 'to' 'so'
    stops = stopwords.words('english')
    # use porter stemmer to reduce a word to its word stem
    stemmer = PorterStemmer()
    final_document = []
    tfi = []
    tf_IDF = []
    weight_vectors = []
    posting_lists = {}
    vocabulary = []

    def __init__(self):
        imageInfo = self.imageInfo
        tokenizer = self.tokenizer
        stops = self.stops
        final_document = self.final_document
        stemmer = self.stemmer
        weight_vectors = self.weight_vectors
        posting_lists = self.posting_lists
        vocabulary = self.vocabulary
        tfi = self.tfi
        tf_IDF = self.tf_IDF

        for i in range(200):
            tokens = tokenizer.tokenize(imageInfo['caption'][i])
            final_tokens = []
            for token in tokens:
                token = token.lower()
                if token not in stops:
                    token = stemmer.stem(token)
                    final_tokens.append(token)
                    if token not in vocabulary:
                        vocabulary.append(token)
            final_document.append(final_tokens)
        for document in final_document:
            weight_vector = {}
            for term in document:
                if term not in weight_vector:
                    tf = document.count(term)/len(document)
                    df = sum(1 for document in final_document if term in document)
                    n = len(final_document)
                    tfi.append(tf)
                    weight = tf * math.log10(n/df)
                    tf_IDF.append(weight)

                    weight_vector[term] = weight
            weight_vectors.append(weight_vector)
        for i in range(len(weight_vectors)):
            document = weight_vectors[i]
            for token in document:
                if token not in posting_lists:
                    posting_lists[token] = []
                posting_lists[token].append([i, document[token]])
                posting_lists[token] = sorted(
                    posting_lists[token], key=lambda x: x[1], reverse=True)

    def search(self, query):
        q = self.tokenizer.tokenize(query)
        tokens = []
        query_weight = {}

        for t in q:
            t = t.lower()
            if t not in self.stops:
                t = self.stemmer.stem(t)
                tokens.append(t)

        for term in tokens:
            if term not in query_weight:
                tf = tokens.count(term) / len(tokens)
                query_weight[term] = tf

        ans = {}
        for term in query_weight:
            if term in self.posting_lists:
                for post in self.posting_lists[term]:
                    document = post[0]
                    if document not in ans:
                        ans[document] = 0
                    ans[document] += post[1] * query_weight[term]
        ans = sorted(ans, key=ans.get, reverse=True)
        print(ans)
        return ans
yes = Image()
yes.search('soccer')





