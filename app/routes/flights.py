from flask import Blueprint, jsonify
from app.services.flight_service import flight_from_TLL


# define endpoint
flights_bp = Blueprint("flights",__name__)