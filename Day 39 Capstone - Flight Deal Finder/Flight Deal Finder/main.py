import json

from data_manager import DataManager
from datetime import datetime, timedelta
from flight_search import FlightSearch
import flight_data
import requests_cache
from pprint import pprint

# This file will need to use the DataManager, FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

requests_cache.install_cache(
    cache_name="flight_cache",
    urls_expire_after={
    "*sheety.co*": requests_cache.DO_NOT_CACHE,
    "*": 3600.
    }
)

# Set the Dates
# date_today = datetime.now().strftime("%d/%m/%Y") # arrival date
arrival_date = datetime(2026, 11, 25).date()
return_date = arrival_date + timedelta(weeks=4) # return date

origin_city_code = "LHR" # London Heathrow

def main():
    data_manager = DataManager()
    sheet_data = data_manager.get_destination_data()
    pprint(sheet_data)  # Print the sheet_data and verify that it includes the airport IATA codes for each city.
    destination_city_row = sheet_data[0] # CDG is first row

    flight_search = FlightSearch()
    flight_options  = flight_search.check_flights(origin_city_code=origin_city_code,
                                 destination_city_code=destination_city_row.get("iataCode"), # CDG
                                 outbound_date=arrival_date,
                                 return_date=return_date)

    cheapest_flight = flight_data.find_cheapest_flight(flight_options, return_date)
    print(cheapest_flight.price)
    print(cheapest_flight.origin_airport)
    print(cheapest_flight.destination_airport)
    print(cheapest_flight.out_date)
    print(cheapest_flight.return_date)

    # compare cheapest flights to available options
    if cheapest_flight.price < destination_city_row.get("lowestPrice"):
        pprint(f"Lower price flight found to {destination_city_row.get("City")}!")
        data_manager.update_lowest_price(destination_city_row.get("id"), cheapest_flight.price)


if __name__ == '__main__':
    main()