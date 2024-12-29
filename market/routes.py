from flask import render_template
from market import app
from market import Item

@app.route("/") # decorator: a function that wraps another function and adds some additional functionality
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/market")
def market():
    items = Item.query.all()
    print(items)
    return render_template("market.html", items=items)