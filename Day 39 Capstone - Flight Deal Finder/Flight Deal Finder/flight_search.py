import os

import requests
from dotenv import load_dotenv

class FlightSearch:
    def __init__(self):
        self._api_key = os.environ["SERP_API_KEY"]
        self._api_endpoint = os.environ["SERP_FLIGHTS_ENDPOINT"]
        self._engine = "google flights"


    # This class is responsible for talking to the Flight Search API.
    def check_flights(self, origin_city_code, destination_city_code, outbound_date, return_date):

        # type = 1  # 1 - round trip
        # adults = 1  # number of people
        # currency = "USD"  # currency of returned prices

        parameters = {
            "api_key": self._api_key,
            "engine": self._engine,
            "departure_id": origin_city_code,
            "arrival_id": destination_city_code,
            "outbound_date": outbound_date,
            "return_date": return_date,
            "type": 1,
            "adults": 1,
            "currency": "USD",
        }

        response = requests.get(url=self._api_endpoint, params=parameters)
        flight_options_data = response.json()

        return flight_options_data

