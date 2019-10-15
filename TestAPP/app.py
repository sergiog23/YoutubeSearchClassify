from flask import Flask, render_template
from flask import request
from processing import YoutubeVid

app = Flask(__name__)

result = []
yes = YoutubeVid()


@app.route('/')
def index():
    return render_template('home.html',data = yes.allData,result =result, search= False)
    

@app.route('/',methods=['POST'])
def search():
    documents = []
    userQuery = request.form.get('Search')
    result =  yes.search(userQuery)
    l = len(result)
    for i in range(l):
        documents.append(result[i])
    print(result)
    title = list(yes.allData['title'][documents])

    return render_template('results.html',data= yes.allData, result = documents, title =title, search =True)

if (__name__ == '__main__'):
    app.run(debug=True)
