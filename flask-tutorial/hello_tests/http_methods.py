from flask import request, Flask

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])

def do_the_login():
    return 'Logging in'

def show_the_login_form():
    return 'Username:\nPassword:'

def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()