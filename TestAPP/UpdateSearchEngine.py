
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import math
import pandas as pd
import numpy


class YoutubeSearchAlgorithm:

    vidInfo = pd.read_csv('USvideos.csv')
    tokenizer = RegexpTokenizer(r'[a-zA-Z]+')
    stops = stopwords.words('english')
    stemmer = PorterStemmer()
    tfi = []
    final_document = []
    weight_vectors = []
    posting_lists = {}
    vocabulary = []

    def __init__(self):
        vidInfo = self.vidInfo
        tokenizer = self.tokenizer
        stops = self.stops
        stemmer = self.stemmer
        final_document = self.final_document
        weight_vectors = self.weight_vectors
        posting_lists = self.posting_lists
        vocabulary = self.vocabulary
        tfi = self.tfi

        for i in range(165):
            tokens = tokenizer.tokenize(vidInfo['title'][i])
            tokens += tokenizer.tokenize(vidInfo['description'][i])

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
                    weight_vector[term] = weight
            weight_vectors.append(weight_vector)

     # construct posting lists
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
        return ans
