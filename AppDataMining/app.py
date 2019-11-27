from flask import Flask, render_template
from flask import request
from SearchApps  import *
from classifier import *


app = Flask(__name__)

result = []
test = AppSearch()
classs = AppClassifer()

@app.route('/')
def index():
    return render_template('home.html', data=test.vidInfo, result=result, search=False)


@app.route('/', methods=['POST'])
def search():
    testing = []
    documents = []
    userQuery = request.form.get('Search')
    result = test.search(userQuery)

    terms = userQuery.split()

    l = len(result)
    for i in range(l):
        documents.append(result[i])
    title = list(test.vidInfo['track_name'][documents])
    description = list(test.vidInfo['app_desc'][documents])
    tf =[]
    idf = []

    for i in documents:
        tfs = test.tfi[i]
        tf.append(tfs)
    for i in documents:
        ids = test.tf_IDF[i]

        idf.append(ids)

    return render_template('results.html', data=test.vidInfo,userQuery=userQuery, result=documents, title=title, description=description,l=l,tf=tf,idf=idf, search=True)
@app.route('/', methods=['POST'])
def classify():
    userQuery = request.form.get('classify')
    categories = []
    percentage = []
    classification = classs.classify(classify) 
    for c in classification:
        categories.append(c)
        percentage.append(round(classification[c]*100,2))
    return render_template('resultsClass.html',data=classs.vidInfo,userQuery=userQuery,categories=categories,percentage=percentage,classification=classification,search=False)



if (__name__ == '__main__'):
    app.run(debug=True)
