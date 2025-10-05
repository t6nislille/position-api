import requests
from flask import Flask
from config import AVIATIONSTACK_API_KEY, AVIATIONSTACK_BASE_URL


# create the Flask instance
app = Flask(__name__)

params = {
    "access_key": AVIATIONSTACK_API_KEY
}

response = requests.get(f"{AVIATIONSTACK_BASE_URL}/flights", params=params)

print("Status Code:", response.status_code)
print("Response:", response.json())