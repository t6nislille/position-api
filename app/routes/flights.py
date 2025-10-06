from flask import Blueprint, jsonify
from app.services.flight_service import flight_from_airport


# define endpoint
flights_bp = Blueprint("flights",__name__)

# define route
@flights_bp.route("/<string:dep_iata>", methods=["GET"])
def get_flight(dep_iata):
    data = flight_from_airport(dep_iata)
    return jsonify(data)