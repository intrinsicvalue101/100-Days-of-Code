# 1. You fetch raw flight data from an API.
#
# 2. find_cheapest_flight() searches that raw data for the cheapest flight.
#
# 3. Once found, find_cheapest_flight() uses the values to build and return a FlightData object.

#This class is responsible for structuring the flight data.
class FlightData:
    # Storing flight parameters inside object attribute
    def __init__(self, price, origin_airport, destination_airport, out_date, return_date):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date

# This function searches the flight options and constructs a FlightData object
def find_cheapest_flight(flight_options, return_date):
    flight_options = flight_options
    combined_list = flight_options.get("best_flights") + flight_options.get("other_flights")

    prices = []

    for flight in combined_list:
        prices.append(flight["price"])

    # Finding the lowest price integer from the list of flights
    lowest_price = min(prices)
    for dict in combined_list:
        if dict.get("price") == lowest_price:
            # print(dict)

            # Extracting individual flight values from dictionary structure
            origin_airport = dict.get("flights")[0].get("departure_airport").get("id")
            destination_airport = dict.get("flights")[0].get("arrival_airport").get("id")
            arrival_time = dict.get("flights")[0].get("departure_airport").get("time")
            arrival_time_formatted = arrival_time.split(" ")[0]

            print("\n" + "*"*5 + "Best Flight" + "*"*5)
            print(f"Origin airport: {origin_airport}")
            print(f"Destination airport: {destination_airport}")
            print(f"Out date: {arrival_time_formatted}")
            print(f"Return date: {return_date}")

            # Creating and returning a new FlightData instance with the extracted values
            return FlightData(lowest_price, origin_airport, destination_airport, arrival_time_formatted, return_date)