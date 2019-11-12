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
    testing = []
    documents = []
    userQuery = request.form.get('Search')
    result = yes.search(userQuery)

    terms = userQuery.split()

    for x in terms:
        testing = x.lower()
        testing = re.sub(r'[^a-z0-9]'.'',testing,documents)
    replace = re.compile(re.escape(term),re.IGNORECASE)
    


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
    for i in documents:
        ids = yes.tf_IDF[i]
        idf.append(ids)

    return render_template('results.html', data=yes.vidInfo,userQuery=userQuery, result=documents, title=title, description=description,l=l,tf=tf,idf=idf, search=True)


if (__name__ == '__main__'):
    app.run(debug=True)
