# turn debug mode on by export FLASK_DEBUG=1 to restart the server when we make changes
# run the app by flask run

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/") # decorator: a function that wraps another function and adds some additional functionality
def hello_world():
    return render_template("home.html")