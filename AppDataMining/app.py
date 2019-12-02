from flask import Flask, render_template
from flask import request
from Search  import *
from SearchApps import * 

app = Flask(__name__)

result = []
SearchObj = YoutubeSearchAlgorithm()
ClassifyObj = AppSearch()

@app.route('/')
def index():
    return render_template('home.html', data=SearchObj.vidInfo, result=result, search=False)


@app.route('/', methods=['POST'])
def search():
    ClassifyObjing = []
    documents = []
    userQuery = request.form.get('Search')
    result = ClassifyObj.search(userQuery)

    terms = userQuery.split()
    l = len(result)
    for i in range(l):
        documents.append(result[i])
    title = list(ClassifyObj.vidInfo['track_name'][documents])
    description = list(ClassifyObj.vidInfo['app_desc'][documents])
    tf =[]
    idf = []

    for i in documents:
        tfs = SearchObj.tfi[i]
        tf.append(tfs)
    for i in documents:
        ids = SearchObj.tf_IDF[i]
        idf.append(ids)

    return render_template('results.html', data=SearchObj.vidInfo,userQuery=userQuery, result=documents, title=title, description=description,l=l,tf=tf,idf=idf, search=True)


if (__name__ == '__main__'):
    app.run(debug=True)
