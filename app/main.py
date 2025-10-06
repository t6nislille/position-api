import requests
from flask import Flask, jsonify
from config import AVIATIONSTACK_API_KEY, AVIATIONSTACK_BASE_URL


# create the Flask instance
app = Flask(__name__)


@app.route("/")
def home():
    return {"message": "Welcome to Position API"}


# start the development server
if __name__ == "__main__":
    app.run(debug=True)