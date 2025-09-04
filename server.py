from flask import Flask

app = Flask(__name__)

def a(x):
    return int(x)+1



@app.route('/')
def index():
    return 'hello'

@app.route('/read/<id>/')
def read(id):

    return str(a(id))

app.run(port=5001,debug=True)