from flask import Flask, render_template
from flask import request
from Search  import *
from SearchApps import * 

app = Flask(__name__)

result = []
yes = YoutubeSearchAlgorithm()
test = AppSearch()

@app.route('/')
def index():
    return render_template('home.html', data=yes.vidInfo, result=result, search=False)


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
        tfs = yes.tfi[i]
        tf.append(tfs)
    for i in documents:
        ids = yes.tf_IDF[i]
        idf.append(ids)

    return render_template('results.html', data=yes.vidInfo,userQuery=userQuery, result=documents, title=title, description=description,l=l,tf=tf,idf=idf, search=True)


if (__name__ == '__main__'):
    app.run(debug=True)
