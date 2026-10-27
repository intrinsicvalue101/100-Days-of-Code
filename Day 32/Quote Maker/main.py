import smtplib
import datetime as dt
import random

EMAIL = ""
PASSWORD = ""

now = dt.datetime.now()
day_of_week= now.weekday()
if day_of_week == 0: # Monday
    with open ("quotes.txt", "r") as file:
        quote_list = file.readlines()
        random_quote = random.choice(quote_list)
        print(random_quote)

    with smtplib.SMTP("smtp.gmail.com") as connection: # closes off connection automatically. similar to with open as
        connection.starttls() # way of securing connection to email server
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg =f"Subject:Monday Motivation\n\n{random_quote}"
        )

