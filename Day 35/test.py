import pandas as pd

# print(series_from_list)

data = ["james,10,sf","bonnie,50,ny","james,50,la"]
rows = []

for item in data:
    split_strings = item.split(",")
    rows.append({"name": split_strings[0], "time": split_strings[1], "state": split_strings[2]})

df = pd.DataFrame(rows)
# print(df)

for name,item in zip(df["name"],df["name"].value_counts()):
    if item > 1:
        print(f"Name: {name}")
        print(f"Occurences: {item}")


