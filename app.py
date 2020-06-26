# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from datetime import datetime


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', time = datetime.now())

@app.route('/password5', methods = ["GET", "POST"])
def password():
    password1 = request.form["password"]
    print(password1)
    if password1 == "p@ssword123":
        return render_template('results.html', time = datetime.now())
    else:
        return render_template('index.html', time = datetime.now())

@app.route('/index3')
def index3():
    return render_template('index3.html', time = datetime.now())
@app.route('/password6', methods = ["GET", "POST"])
def password6():
    password7 = request.form["password"]
    print(password7)
    if password7 == "eikooc":
        return render_template('results3.html', time = datetime.now())
    else:
        return render_template('index3.html', time = datetime.now())

@app.route('/index2')
def index2():
    return render_template('index2.html', time = datetime.now())

@app.route('/password2', methods = ["GET", "POST"])
def password2():
    password3 = request.form["password"]
    print(password3)
    if password3 == "123456789":
        return render_template('results2.html', time = datetime.now())
    else:
        return render_template('index2.html', time = datetime.now())



@app.route('/password')
def password5():
    return render_template('password.html', time = datetime.now())

