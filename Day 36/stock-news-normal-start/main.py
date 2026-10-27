import requests
from datetime import datetime
from twilio.rest import Client
import os

# alphavantage
STOCK_NAME = "MSFT"
STOCK_ENDPOINT = os.environ.get("ALPHAVANTAGE_ENDPOINT")
STOCK_API_KEY = os.environ.get("ALPHAVANTAGE_API_KEY")

# twilio
account_sid = os.environ.get("TWILIO_SID")
auth_token = os.environ.get("TWILIO_TOKEN")
client = Client(account_sid, auth_token)

# newsapi
COMPANY_NAME = "Microsoft"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY =  os.environ.get("NEWS_API_KEY")

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
# alphavantage
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "datatype": "json",
    "apikey": STOCK_API_KEY,
}

stock_query_response = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_data = stock_query_response.json()
print(stock_query_response.raise_for_status())
data_list = [value for (key, value) in stock_data.get("Time Series (Daily)").items()]
yesterday_data = data_list[1]
yesterday_closing_price = float(yesterday_data["4. close"])

# Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[2]
day_before_yesterday_closing_price = float(day_before_yesterday_data["4. close"])

# Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

# If percentage is greater than 5 then get the first 3 news pieces for the COMPANY_NAME
current_datetime = datetime.now().strftime("%Y-%m-%d")
# print(diff_percent)
diff_percent = round((difference / float(yesterday_closing_price)) * 100)
if diff_percent > 5: # Note: if there's no output, change 5 to a lower number -> 0.2
    parameters_2 = {
        "qInTitle": COMPANY_NAME,
        "from": current_datetime,
        "apikey": NEWS_API_KEY,
        "language": "en"
    }
    news_response = requests.get(NEWS_ENDPOINT, params=parameters_2)
    articles = news_response.json()["articles"]
    print(news_response.raise_for_status())

    # Create a new list of the first 3 article's headline and description using list comprehension.
    first_three_articles = articles[:3]
    article_titles_list = [item["title"] for item in first_three_articles]
    article_description_list = [item["description"] for item in first_three_articles]

    # Send each article as a separate message via Twilio.
    print(article_titles_list)
    for i in range(len(article_titles_list)):
        message = client.messages.create(
            body=f"{STOCK_NAME}: {up_down}{diff_percent}\nHeadline: {article_titles_list[i]}\nBrief: {article_description_list[i]} ",
            from_= os.environ.get("TWILIO_SENDERS_PHONE"),
            to= os.environ.get("TWILIO_RECEIVERS_PHONE")
        )
        print(message.status)


