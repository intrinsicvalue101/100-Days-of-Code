import os
import requests
from datetime import datetime

# TODO 1: Get Exercise Stats with Natural Language Queries
WORKOUT_API = os.getenv("WORKOUT_KEY")
APP_ID = os.getenv("WORKOUT_APP_ID")
WORKOUT_ENDPOINT = os.environ.get("WORKOUT_ENDPOINT")

exercise_input = input("Tell me which exercises you did today: ")

headers = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": WORKOUT_API
}

parameters = {
    "query": exercise_input
}

response1 = requests.post(WORKOUT_ENDPOINT, headers=headers, json=parameters)
print(response1.status_code)
result = response1.json()

# relevant fields are duration_min, nf_calories, name
# calories = result["exercises"][0]["nf_calories"]
# exercise_type = result["exercises"][0]["name"]
# duration = result["exercises"][0]["duration_min"]

# TODO 2: Query Sheety to Update Google Sheets'
SHEETY_AUTH_TOKEN = os.environ.get("SHEETY_AUTH_TOKEN")
headers2 = {
    "Authorization": SHEETY_AUTH_TOKEN
}

todays_date = datetime.now().strftime("%d/%m/%Y")
current_time = datetime.now().strftime("%H:%M:%S")
# print(time)

sheety_endpoint = os.environ.get("SHEETY_ENDPOINT")
for exercise in result["exercises"]:
    sheet_inputs = {"workout":
    {
    "date": todays_date,
    "time": current_time,
    "exercise": exercise["name"].title(),
    "duration": exercise["duration_min"],
    "calories": exercise["nf_calories"]
    }
}
    sheet_response = requests.post(sheety_endpoint, headers=headers2, json=sheet_inputs)
    print(sheet_response.text)
