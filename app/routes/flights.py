from flask import Blueprint, jsonify
from app.services.flight_service import flight_from_TLL


# define endpoint
flights_bp = Blueprint("flights",__name__)

# define route
@flights_bp.route("/TLL_IATA", methods=["GET"])
def get_flight(TLL_IATA):
    data = flight_from_TLL(TLL_IATA)
    return jsonify(data)