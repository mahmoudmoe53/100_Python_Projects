import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

NUTRITIONIX_API_KEY = os.environ.get("NUTRITIONIX_API_KEY")
NUTRITIONIX_APP_ID = os.environ.get("NUTRITIONIX_APP_ID")
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = "https://api.sheety.co/f30a6a5c4535fc80adc15c5be476ce55/workoutTracking/workouts"

nutritionix_headers = {
    "x-app-key":NUTRITIONIX_API_KEY,
    "x-app-id":NUTRITIONIX_APP_ID
}

question = input("Tell me which exercise you did today?")

nutritionix_parameters = {
    "query":question
}

nutritionix_response = requests.post(url=NUTRITIONIX_ENDPOINT, headers=nutritionix_headers, json=nutritionix_parameters)
nutritionix_data = nutritionix_response.json()

sheety_headers = {
    "Authorization":SHEETY_TOKEN,
    "Content-Type": "application/json"
}

today = datetime.today()
date = today.strftime("%d/%m/%Y")
duration = list(nutritionix_data["exercises"])[0]["duration_min"]
calories = list(nutritionix_data["exercises"])[0]["nf_calories"]
exercise = list(nutritionix_data["exercises"])[0]["name"]
time = today.strftime("%H:%M:%S")

sheety_parameters = {
    "workout":{
    "date":date,
    "time":time,
    "exercise":exercise,
    "duration":duration,
    "calories":calories
        }
}

sheety_response = requests.post(url=SHEETY_ENDPOINT, headers=sheety_headers, json=sheety_parameters)




