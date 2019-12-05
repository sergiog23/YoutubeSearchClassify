from flask import Flask, render_template
from flask import request
from search  import *
from classifier import *
from ImageCaptioning import *


app = Flask(__name__)

result = []
searchObj = AppSearch()
classifyObj = AppClassifer()
imageObj = Image()

@app.route('/')
def index():
    return render_template('home.html',data=searchObj.vidInfo,result=result, search=False,classify=False,Image=False)


@app.route('/', methods=['POST','GET'])
def Compute():
    documents = []
    searchQuery = request.form.get('Search')
    if(searchQuery is not None):

        result = searchObj.search(searchQuery)
        l = len(result)
        for i in range(l):
            documents.append(result[i])
        title = list(searchObj.vidInfo['track_name'][documents])
        description = list(searchObj.vidInfo['app_desc'][documents])
        tf =[]
        idf = []

        for i in documents:
            tfs = searchObj.tfi[i]
            tf.append(tfs)
        for i in documents:
            ids = searchObj.tf_IDF[i]
            idf.append(ids)
        return render_template('results.html', data=searchObj.vidInfo,userQuery=searchQuery, result=documents, title=title, description=description,l=l,tf=tf,idf=idf, search=True,classify = False)

    classifyQuery = request.form.get('Classify')
    if(classifyQuery is not None):
        print(classifyQuery)
        categories = []
        percentage = []
        priors = []
        classification = classifyObj.classify(classifyQuery) 
        classCounts = classifyObj.counts
        priors.append(classCounts)
        for c in classification:
            categories.append(c)
            percentage.append(round((classification[c]*100),2))
            
        return render_template('resultsClass.html',data=classifyObj.vidInfo,classifyQuery=classifyQuery,categories=categories,percentage=percentage,classification=classification,search=False,classify=True,priors=priors)

    ImageQuery = request.form.get('Image')
    if( ImageQuery is not None):
        documentsImage = []
        print(ImageQuery)
        result = imageObj.search(ImageQuery)
        l = len(result)
        for i in range(l):
            documentsImage.append(result[i])
        caption = list(imageObj.imageInfo['caption'][documentsImage])
        url = list(imageObj.imageInfo['url'][documentsImage])

        def path(path):
            return '<img src="'+path + '" width = "100">'
    
        tf =[]
        idf = []

        for i in documentsImage:
            tfs = imageObj.tfi[i]
            tf.append(tfs)
            ids = imageObj.tf_IDF[i]
            idf.append(ids)
        return render_template('imageResults.html', data=imageObj.imageInfo,userQuery=ImageQuery,url=url, result=documentsImage,caption=caption,l=l,tf=tf,idf=idf,Image=True,image=path)


if (__name__ == '__main__'):
    app.run(debug=True)
