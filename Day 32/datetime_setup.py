import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week= now.weekday()
# print(type(now))
# print(day_of_week)

date_of_birth = dt.datetime(year= 2007, month=1, day=18)
print(date_of_birth)
