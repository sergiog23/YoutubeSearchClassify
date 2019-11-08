from flask import Flask, render_template
from flask import request
from UpdateSearchEngine import *

app = Flask(__name__)

result = []
yes = YoutubeSearchAlgorithm()


@app.route('/')
def index():
    return render_template('home.html', data=yes.vidInfo, result=result, search=False)


@app.route('/', methods=['POST'])
def search():
    documents = []
    userQuery = request.form.get('Search')
    result = yes.search(userQuery)

    l = len(result)
    for i in range(l):
        documents.append(result[i])
    title = list(yes.vidInfo['title'][documents])
    description = list(yes.vidInfo['description'][documents])
    tf =[]
    idf = []

    for i in documents:
        tfs = yes.tfi[i]
        tf.append(tfs)
        #print(tf)
    for i in documents:
        ids = yes.tf_IDF[i]
        idf.append(ids)

    return render_template('results.html', data=yes.vidInfo,userQuery=userQuery, result=documents, title=title, description=description,l=l,tf=tf,idf=idf, search=True)


if (__name__ == '__main__'):
    app.run(debug=True)
