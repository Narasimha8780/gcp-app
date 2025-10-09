# app.py
from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Flask Hello World</title>
        <style>
            body { font-family: Arial, sans-serif; background-color: #f0f0f0; text-align: center; padding: 100px; }
            h1 { color: #333; }
        </style>
    </head>
    <body>
        <h1>Hello, World! branch-push-test-is-successful-for-local-test-instant-trigger</h1>
    </body>
    </html>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 9090))
    app.run(host="0.0.0.0", port=port)
