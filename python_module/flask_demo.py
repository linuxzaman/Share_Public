from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return '<h1>Hello, world</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)