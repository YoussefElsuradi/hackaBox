# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/password', methods = ["GET", "POST"])
def password():
    password1 = request.form["password"]
    print(password1)
    if password1 == "p@ssword123":
        return render_template('results.html')
    else:
        return render_template('index.html')
