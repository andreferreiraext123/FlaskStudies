from flask import Flask, render_template # From module import the class flask(with all the functions)

app = Flask(__name__) # Initial instance of flask class

@app.route('/') # Showing the route main (root route)
@app.route('/homePage')
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = [
        {'ID': 1, 'Name': 'Phone', 'Barcode': '312312312', 'Price': 500},
        {'ID': 2, 'Name': 'Laptop', 'Barcode': '33333333', 'Price': 230},
        {'ID': 3, 'Name': 'Headset', 'Barcode': '32132111', 'Price': 100}
    ]
    return render_template('market.html', items=items)