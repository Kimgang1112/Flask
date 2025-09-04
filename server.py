from flask import Flask

app = Flask(__name__)

def a(x):
    return int(x)+1



@app.route('/')
def index():
    return '''
    <h1>안녕하세요</h1>
    저는 김강입니다.

    '''

@app.route('/read/<id>/')
def read(id):

    return str(a(id))

app.run(port=5001,debug=True)