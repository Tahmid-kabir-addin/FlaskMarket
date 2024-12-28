# turn debug mode on by export FLASK_DEBUG=1 to restart the server when we make changes
# run the app by flask run

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/") # decorator: a function that wraps another function and adds some additional functionality
@app.route("/home")
def hello_world():
    return render_template("home.html")

@app.route("/market")
def market():
    items = [{"id": 1, "name": "ChatGpt 4.0", "price": 20, "description": "ChatGpt 4.0 is a new chatbot that can answer any question you have.", "barcode": "1234567890", "rating": 4.5},
             {"id": 2, "name": "Claude 3.5", "price": 10, "description": "Claude 3.5 is a new chatbot that can answer any question you have.", "barcode": "1234567890", "rating": 4.7},
             {"id": 3, "name": "Gemini 1.5", "price": 30, "description": "Gemini 1.5 is a new chatbot that can answer any question you have.", "barcode": "1234567890", "rating": 4.2}]
    return render_template("market.html", items=items)

