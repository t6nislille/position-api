import requests
from config import AVIATIONSTACK_API_KEY, AVIATIONSTACK_BASE_URL


params = {
    "access_key": AVIATIONSTACK_API_KEY
}

response = requests.get(f"{AVIATIONSTACK_BASE_URL}/flights", params=params)

print(response.status_code)