import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data)) # dataframes is the whole table
# print(type(data["temp"])) # series is a entire column/list

# data_dict = data.to_dict()
# print(data_dict)

temp_list = data["temp"].to_list()
# print(temp_list)

# TODO: Get avg temp from list of temps
# average = sum(temp_list) / len(temp_list)
# print(average)

# print(data["temp"].mean()) # Preferred way
# print(data["temp"].max())

# TODO: Get data in columns/ create data series
# main idea: if we input entire name of column we get column
# print(data["condition"])
# # OR
# print(data.condition) # pandas automatically converts column names to attributes

# TODO: Get data in row
# main idea: if we input row name by filtering we get ahold of row
# print(data[data["day"] == "Monday"])
# print(data[data.temp == data.temp.max()])# print row of data which had the highest temp

# TODO: Get condition for a particular day/row
# monday = data[data.day == "Monday"] # fetch row
# print(monday.condition) # fetch particular column in row
#
# monday_temp_F = monday.temp * 9/5 + 32
# print(monday_temp_F)

# TODO: Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")