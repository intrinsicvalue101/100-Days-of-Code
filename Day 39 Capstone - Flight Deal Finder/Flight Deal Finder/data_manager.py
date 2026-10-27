import os
import requests
# from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

# Load environment variables from .env file
# load_dotenv("")

SHEETY_PRICES_ENDPOINT = os.environ.get("SHEETY_PRICES_ENDPOINT")
SHEETY_FLIGHT_AUTH_TOKEN = os.environ.get("SHEETY_FLIGHT_AUTH_TOKEN")

class DataManager:

    def __init__(self):
        self._api_endpoint = os.environ["SHEETY_FLIGHTS_ENDPOINT"]
        self._auth = {"Authorization": SHEETY_FLIGHT_AUTH_TOKEN}
        self.destination_data = {}

        # self._api_token = os.environ["SHEETY_API_TOKEN"]
        # self._user = os.getenv("SHEETY_USERNAME")
        # self._password = os.getenv("SHEETY_PASSWORD")
        # self._authorization = HTTPBasicAuth(self._user, self._password)

    def get_destination_data(self):
        # 2. Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=self._api_endpoint, headers=self._auth)
        # print(response.text)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_lowest_price(self, row_id, new_price):
        sheet_inputs = {"price":
            {
                "Lowest Price": new_price,
            }
        }
        response = requests.post(url=f"{self._api_endpoint}/{row_id}", headers=self._auth, json=sheet_inputs)

        if response.status_code != 200:
            print(f"update_lowest_price() response code: {response.status_code}")
        else:
            return response.text



