from flask import  Flask, render_template		# importing the Flask instance from the entire Flask package
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)           # Initialize the instance of the flask with the given argument
								# __name__ refers to the local python file I am working with
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)			# initializing the class

from market import routes