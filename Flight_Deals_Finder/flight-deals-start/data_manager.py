import requests
import os
from dotenv import load_dotenv

load_dotenv()

SHEETY_ENDPOINT = "https://api.sheety.co/f30a6a5c4535fc80adc15c5be476ce55/flightDeals/prices"

class DataManager:
    def __init__(self):
        self.__sheety_token = os.environ.get("SHEETY_TOKEN")
        self.__headers = {
            "Authorization":self.__sheety_token,
            "Content-Type": "application/json"
        }
        self.destination_data = {}


    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDPOINT, headers=self.__headers)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data


    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_ENDPOINT}/{city['id']}", headers=self.__headers, json=new_data)
        return

