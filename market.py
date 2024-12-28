# turn debug mode on by export FLASK_DEBUG=1 to restart the server when we make changes
# run the app by flask run

from flask import Flask

app = Flask(__name__)

@app.route("/") # decorator: a function that wraps another function and adds some additional functionality
def hello_world():
    return "<h2>Hello, World!</h2>"

@app.route("/about")
def about():
    return "<h2>About</h2>"

@app.route("/profile/<username>")
def profile(username):
    return f"<h2>Profile for {username}</h2>"