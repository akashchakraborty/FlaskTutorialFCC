from flask import  Flask, render_template		# importing the Flask instance from the entire Flask package

app = Flask(__name__)           # Initialize the instance of the flask with the given argument
								# __name__ refers to the local python file I am working with

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
	items = [
    {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
    {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
    {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    ]
	return render_template('market.html',items=items)
