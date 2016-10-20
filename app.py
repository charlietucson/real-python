# Import the Flask class from the flask package
from flask import Flask 

# create the application object
app = Flask(__name__)

# use decorators to link the funciton to url
@app.route("/")
def index():
	return "We are in Index function"


@app.route("/hello")

# define the view using a function, which returns a string
def hello_world():
	return "Hello World!"

# dynamic route
@app.route("/test/<search_query>")
def search(search_query):
	return search_query

# Flask converters
@app.route("/integer/<int:value>")
def int_type(value):
	print(value + 1)
	return "correct"

@app.route("/float/<float:value>")
def float_type(value):
	print(value+1)
	return "correct"

## pagina 63 ##########

# start the development server using the run() method
if __name__ == '__main__':
	app.run()