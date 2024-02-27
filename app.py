# app.py
from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the root URL ("/") that returns an HTML page with a styled greeting
@app.route('/')
def hello():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Flask Hello World</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f0f0f0;
                text-align: center;
                padding: 100px;
            }
            h1 {
                color: #333;
            }
        </style>
    </head>
    <body>
        <h1>Hello, World!</h1>
    </body>
    </html>
    """

# Start the Flask web server if this script is executed directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
