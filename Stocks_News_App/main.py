from twilio.rest import Client
import requests
import os
from dotenv import load_dotenv


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

load_dotenv()
stocks_api_key = os.environ.get("STOCKS_API_KEY")
news_api_key = os.environ.get("NEWS_API_KEY")

stocks_parameters = {
    "apikey":stocks_api_key,
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,

}
stocks_response = requests.get(STOCK_ENDPOINT, params=stocks_parameters)

stocks_data = stocks_response.json()["Time Series (Daily)"]
stocks_data_list = [value for (key, value) in stocks_data.items()]

yesterday_data = stocks_data_list[0]
yesterday_closing_price = yesterday_data["4. close"]


day_before_yesterday_data = stocks_data_list[1]
day_before_yesterday_data_closing_price = day_before_yesterday_data["4. close"]

stock_difference = float(yesterday_closing_price) - float(day_before_yesterday_data_closing_price)

percentage_difference = int((stock_difference / float(yesterday_closing_price)) * 100)
up_down = None

if percentage_difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"



news_parameters = {
    "apiKey": news_api_key,
    "qInTitle":COMPANY_NAME
}

news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)

news_data = news_response.json()["articles"]

three_articles = news_data[0:3]

formatted_articles = [f"Headline: {news_data['title']}.\nBrief {news_data['description']}" for news_data in three_articles]


account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
client = Client(account_sid, auth_token)

for article in formatted_articles:
    message = client.messages.create(
        body=f'{COMPANY_NAME}: {up_down}{abs(percentage_difference)} \n{formatted_articles}',
        from_="whatsapp:+14155238886",
        to="whatsapp:+447776478193",
    )

    print(message.status)



"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

