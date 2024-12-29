# this __init__.py file indicates that this directory is a package
# It is mandatory in older versions of Python but optional in newer versions
# It is used to initialize the package
# Defining what is exposed when importing the package.

# turn debug mode on by export FLASK_DEBUG=1 to restart the server when we make changes
# run the app by flask run

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)

from .models import Item

# Create the database tables within application context
with app.app_context():
    db.create_all()

from . import routes

from market import app, db, Item

# with app.app_context():
#     # Create test items
#     item1 = Item(
#         name="iPhone 13",
#         price=699,
#         barcode="1234567890123",
#         description="Latest iPhone model",
#         rating=4.5
#     )
    
#     item2 = Item(
#         name="MacBook Pro",
#         price=1299,
#         barcode="9876543210987",
#         description="Powerful laptop for professionals",
#         rating=4.8
#     )
    
#     # Add items to the session and commit
#     db.session.add(item1)
#     db.session.add(item2)
#     db.session.commit()
