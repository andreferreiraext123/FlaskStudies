from flask import Flask # From module import the class flask(with all the functions)

app = Flask(__name__) # Initial instance of flask class

@app.route("/") # Showing the route main
def hello_world():
    return "<h1> Hello wdasdaso211ld </h1>"
