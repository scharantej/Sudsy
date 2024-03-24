
# Import necessary modules
from flask import Flask, render_template

# Create a Flask application
app = Flask(__name__)

# Define the routes
@app.route('/')
def index():
    """
    Renders the main landing page of the website.
    """
    return render_template('index.html')

@app.route('/about')
def about():
    """
    Renders the about page of the website.
    """
    return render_template('about.html')

@app.route('/contact')
def contact():
    """
    Renders the contact page of the website.
    """
    return render_template('contact.html')

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
