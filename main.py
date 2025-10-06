from flask import Flask


# create the Flask instance
app = Flask(__name__)


@app.route("/")
def home():
    return {"message": "Welcome to Position API"}


# start the development server
if __name__ == "__main__":
    app.run(debug=True)