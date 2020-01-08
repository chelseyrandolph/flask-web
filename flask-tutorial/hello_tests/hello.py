#https://flask.palletsprojects.com/en/1.0.x/quickstart/#a-minimal-application
from flask import Flask
from flask import render_template
app = Flask(__name__)

# set FLASK_APP=hello.py
# python -m flask run
# Chrome --> localhost:5000

# localhost:5000
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('test_page.html', name=name)


# localhost:5000/about
@app.route('/about/')
def about():
    return 'The about page'

# localhost:5000/projects
@app.route('/projects/')
def projects():
    return 'The projects page'