from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello'

@app.route('/read/<id>/')
def read(id):
    return f'read {id}'

app.run(port=5001,debug=True)