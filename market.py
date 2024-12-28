# turn debug mode on by export FLASK_DEBUG=1 to restart the server when we make changes
# run the app by flask run

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer, nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)
    rating = db.Column(db.Float, nullable=False, default=0.0)

    def __repr__(self):
        return f"Item {self.name}"

@app.route("/") # decorator: a function that wraps another function and adds some additional functionality
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/market")
def market():
    items = Item.query.all()
    return render_template("market.html", items=items)

