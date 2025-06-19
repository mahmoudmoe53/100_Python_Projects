import requests
import os
from twilio.rest import Client

api_key = os.environ.get("API_KEYS")
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

parameters = {
    "lat":51.481583,
    "lon":-3.179090,
    "appid": api_key,
    "cnt": 4
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)

response.raise_for_status()

data = response.json()


rain = False

for i in range(4):
    weather = data["list"][i]["weather"][0]["id"]
    if weather < 700:
        rain = True

if rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="Bring an Umbrella! ☔",
        from_="whatsapp:+14155238886",
        to="whatsapp:+447776478193",
    )

    print(message.status)
else:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="Won't be needing an umbrella! 😎",
        from_="whatsapp:+14155238886",
        to="whatsapp:+447776478193",
    )

    print(message.status)





