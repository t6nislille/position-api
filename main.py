from flask import Flask
from app.routes.flights import flights_bp
from flask_swagger_ui import get_swaggerui_blueprint


# create the Flask instance
app = Flask(__name__)

# attach flights blueprint to main 
app.register_blueprint(flights_bp, url_prefix="/flights")


@app.route("/")
def home():
    return {"message": "Welcome to Position API"}


# start the development server
if __name__ == "__main__":
    app.run(debug=True)