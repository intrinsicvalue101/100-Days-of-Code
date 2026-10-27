# TODO 1 w no imported libraries
# data = []
# with open("weather_data.csv") as weather_info:
#     for line in weather_info:
#         data.append(line.strip())

# TODO 2 w csv library
# import csv # import csv library
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file) #takes the file and reads/outputs data
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# TODO 3 w external pandas library to handle csv data, the GOTO method for all python devs
import pandas

data = pandas.read_csv("weather_data.csv")
# print(data)
print(data["temp"])