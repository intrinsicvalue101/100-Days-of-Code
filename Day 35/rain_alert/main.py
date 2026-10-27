import os
import requests

API_KEY = os.getenv("OPEN_WEATHER_API_KEY")
OPEN_WEATHER_ENDPOINT = os.getenv("OPEN_WEATHER_ENDPOINT")

MY_LAT = 29.424122
MY_LONG = -98.493629

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "cnt": 4,
}

response = requests.get(OPEN_WEATHER_ENDPOINT, params=parameters)
weather_data = response.json()
print(response.raise_for_status())

will_rain = False

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella!")

print(weather_data["list"][0]["weather"][0]["description"])
