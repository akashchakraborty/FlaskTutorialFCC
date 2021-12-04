from market import app
from flask import render_template
from market.models import Item


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
