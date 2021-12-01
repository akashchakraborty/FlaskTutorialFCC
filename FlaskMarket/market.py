from flask import  Flask, render_template		# importing the Flask instance from the entire Flask package
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)           # Initialize the instance of the flask with the given argument
								# __name__ refers to the local python file I am working with
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'


db = SQLAlchemy(app)			# initializing the class



class Item(db.Model):
	id = db.Column(db.Integer(),primary_key=True)
	name = db.Column(db.String(length=30), nullable=False, unique=True)
	price = db.Column(db.Integer(),nullable=False)
	barcode = db.Column(db.String(length=12),nullable=False,unique=True)
	description = db.Column(db.String(length=1024),nullable=False)

	def __repr__(self):
		return f'Item {self.name}'



# @app.route('/')					# The decorator which specifies the url we are going to navigate to

# def hello_world():
	# return "<h1>Hello World, But Bigger Version !!! </h1>"

@app.route('/about') 			# thus the function can give changes to http://127.0.0.1:5000/about
def about():
	return "<h2>Hello, welcome to the about part of this app</h2>"


@app.route('/about/<username>') # dynamic routing instead of hardcoding the route
def about_page(username):
	return "<h1>About Page of {}".format(username)

@app.route('/')	
@app.route('/home')
def home_page():
	return render_template('home.html')
	
@app.route('/market')
def market_page():
	items = Item.query.all()
	return render_template('market.html',items=items)
