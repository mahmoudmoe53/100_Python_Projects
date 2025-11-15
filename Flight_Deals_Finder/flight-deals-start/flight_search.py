import requests
import os
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

END_POINT = "https://test.api.amadeus.com/v1"

class FlightSearch:
    def __init__(self):
        self.__api_key = os.environ.get("AMADEUS_API_KEY")
        self.__password = os.environ.get("AMADEUS_SECRET")
        self.__token = self.__get_new_token()

    def get_destination_code(self, city_name):
        headers = {
            "Authorization":f"Bearer {self.__token}"
        }

        params = {
            "keyword":city_name,
            "max": 2,
            "include":"AIRPORTS"
        }

        response = requests.get(f"{END_POINT}/reference-data/locations/cities", params=params, headers=headers)

        data = response.json()

        return data["data"][0]["iataCode"]


    def __get_new_token(self):
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        body = {
            "grant_type": 'client_credentials',
            "client_id": self.__api_key,
            "client_secret": self.__password
        }
        response = requests.post(url=f"{END_POINT}/security/oauth2/token", data=body, headers=headers)

        data = response.json()
        return data["access_token"]



    def get_prices(self, iata_code):
        headers = {
            "Authorization": f"Bearer {self.__token}"
        }

        params = {
            "originLocationCode":"LON",
            "destinationLocationCode":iata_code,
            "departureDate":"2025-12-15",
            "adults":1,
            "nonStop": "true"
        }


        response = requests.get(url="https://test.api.amadeus.com/v2/shopping/flight-offers", headers=headers, params=params)

        data = response.json()

        pprint(data)


