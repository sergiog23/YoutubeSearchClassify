from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/', methods=['POST'])
def search():
    search = request.form.get('search')

if (__name__ == '__main__'):
    app.run(debug=True)
