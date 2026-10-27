import requests
import os
from datetime import datetime, timedelta

USERNAME = os.environ.get("PIXELA_USERNAME")
PIXELA_TOKEN = os.environ.get("PIXELA_TOKEN") # TODO: figure out what this is
PIXELA_ENDPOINT = os.environ.get("PIXELA_ENDPOINT")

user_params = {
    "token": PIXELA_TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# 1. create user/setup new account
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

# 2. create new graph endpoint
graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_config = {
    "id": "graph3",
    "name": "Time Spent Coding Graph",
    "unit": "minute",
    "type": "float",
    "color": "ajisai"
}

headers = { # used for advanced authentication. ensures apikey isn't visible in server logs
    "X-USER-TOKEN": PIXELA_TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# 3. post a value to the graph
today = datetime.now().strftime('%Y%m%d')
yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y%m%d')

pixel_data = {
    "date": today,
    "quantity": "30"
}

# POST
# response = requests.post(url=f"{graph_endpoint}/{graph_config["id"]}", json=pixel_data, headers=headers)
# print(response.text)

new_pixel_data1 = {
    "date": yesterday,
    "quantity": "30"
}

new_pixel_data2 = {
    "date": yesterday,
    "quantity": "60"
}

# PUT
# update_endpoint = requests.put(url=f"{graph_endpoint}/{graph_config["id"]}/{yesterday}", json=new_pixel_data1, headers=headers)
# print(update_endpoint.text)

# DELETE
update_endpoint2 = requests.delete(url=f"{graph_endpoint}/{graph_config["id"]}/{yesterday}", headers=headers)
print(update_endpoint2.text)