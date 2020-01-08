from flask import Flask

app = Flask(__name__)

# localhost:5000
@app.route('/')
def hello_world():
    return 'Hello, World!'