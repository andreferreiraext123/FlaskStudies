from flask import Flask, render_template # From module import the class flask(with all the functions)

app = Flask(__name__) # Initial instance of flask class

@app.route('/') # Showing the route main (root route)
@app.route('/homePage')
def home_page():
    return render_template('index.html')

@app.route('/market')
def market_page():
    items = [
        {'id': 1, 'name': 'Phone', 'barcode': '312312312', 'Price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode': '33333333', 'Price': 230},
        {'id': 3, 'name': 'Headset', 'barcode': '32132111', 'Price': 100}
    ]
    return render_template('market.html', items=items)