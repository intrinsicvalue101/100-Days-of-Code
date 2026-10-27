import smtplib

EMAIL = ""
PASSWORD = ""

with smtplib.SMTP("smtp.gmail.com") as connection: # closes off connection automatically. similar to with open as
    connection.starttls() # way of securing connection to email server
    connection.login(user=EMAIL, password=PASSWORD)
    connection.sendmail(
        from_addr=EMAIL,
        to_addrs="",
        msg ="Subject:Hello\n\nThis is the body of my email."
    )


