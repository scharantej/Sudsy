
# Import necessary modules
from flask import Flask, render_template, request, redirect, url_for, flash

# Initialize the Flask application
app = Flask(__name__)

# Define the products list
products = [
    {"name": "Lavender Soap", "description": "A calming and relaxing soap with a delicate lavender scent.", "price": 5.99},
    {"name": "Eucalyptus Soap", "description": "A refreshing and invigorating soap with a strong eucalyptus aroma.", "price": 6.99},
    {"name": "Honey Oatmeal Soap", "description": "A gentle and moisturizing soap with a sweet honey and oatmeal scent.", "price": 7.99},
    {"name": "Tea Tree Oil Soap", "description": "An antibacterial and antifungal soap with a strong tea tree oil scent.", "price": 8.99},
    {"name": "Rosehip Soap", "description": "A nourishing and anti-aging soap with a delicate rosehip scent.", "price": 9.99}
]

# Define the shopping cart
cart = []

# Define the routes
@app.route('/')
def index():
    return render_template('index.html', products=products, cart=cart)

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    product_name = request.form.get('product_name')
    quantity = request.form.get('quantity')

    # Add the product to the cart
    cart.append({'name': product_name, 'quantity': int(quantity)})

    # Flash a success message
    flash('Product added to cart.')

    # Redirect to the index page
    return redirect(url_for('index'))

@app.route('/cart')
def cart():
    return render_template('cart.html', cart=cart)

@app.route('/checkout')
def checkout():
    # Redirect to the index page
    return redirect(url_for('index'))

@app.route('/thankyou')
def thankyou():
    # Clear the cart
    cart.clear()

    # Flash a thank you message
    flash('Thank you for your purchase.')

    # Redirect to the index page
    return redirect(url_for('index'))

# Run the application
if __name__ == '__main__':
    app.secret_key = 'supersecretkey'
    app.run(debug=True)
