from flask import Flask, render_template # From module import the class flask(with all the functions)

app = Flask(__name__) # Initial instance of flask class

@app.route('/') # Showing the route main
def home_page():
    return render_template('index.html')