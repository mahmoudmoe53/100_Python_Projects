import requests
from pprint import pprint
import os
from dotenv import load_dotenv
from data_manager import DataManager
from flight_search import FlightSearch


data_manager = DataManager()

sheet_data = data_manager.get_destination_data()

flight_search = FlightSearch()

if sheet_data[0]["iataCode"] == '':
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])

data_manager.destination_data = sheet_data
data_manager.update_destination_codes()

for row in sheet_data:
    city = row["iataCode"]
    flight_search.get_prices(city)


