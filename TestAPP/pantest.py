# TF_IDF calculations 

# Function to compute Term frequency
# function logic from 

def computeTF( wordDict, bow)
    tfDict = {}
    bowCount = len(bow)
    for word, count in wordDict.items():
        tfDict[word] = count/float(bowCount)
    return tfDict
    
# Function to compute IDF 
def computeIDF(docList)
    import math 
    idfDict = {}
    
    N = len(docList)

    idfDict = dict.fromkeys(docList[0].keys(),0)
    for doc in docList:
        for word, val in doc.items():
            if val > 0
                idfDict[word] += 1
    for word, val in idfDict.items():
        idfDict[word] = math.log10(N/float(val))
    
    return idfDict

# function to compute TF-IDF 

def computeTFIDF(tfBow, idfs ):
    tfidf = {}
    for word, val in tfBbow.items():
        tfidf[word] = val*idfs[word]
    return tfidf