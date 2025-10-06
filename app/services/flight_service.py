import requests
from config import AVIATIONSTACK_API_KEY, AVIATIONSTACK_BASE_URL

# get flights from Tallinn Airport(TLL)
def flight_from_TLL(TLL_IATA: str):
    params = {
        "access_key": AVIATIONSTACK_API_KEY,
        "dep_iata": TLL_IATA
    }

    response = requests.get(f"{AVIATIONSTACK_BASE_URL}/flights", params=params)

    data = response.json()
    return data
