import requests
from datetime import datetime

MY_LAT = 51.459141

MY_LNG = -3.179169

iss_response = requests.get("http://api.open-notify.org/iss-now.json")

iss_data = iss_response.json()

iss_latitude = iss_data["iss_position"]["latitude"]
iss_longitude = iss_data["iss_position"]["longitude"]

iss_coor = (iss_latitude, iss_longitude)


my_location_parameters = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "format": "json"
}

headers = {
    "User-Agent": "MyApp/1.0 (myemail@example.com)"
}


my_location_response = requests.get("https://nominatim.openstreetmap.org/reverse",
                                    params=my_location_parameters, headers=headers)

my_location_data = my_location_response.json()["address"]["city"]


sunrise_parameters = {
    "lat":MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}

sunrise_response = requests.get("https://api.sunrise-sunset.org/json", params=sunrise_parameters)

sunrise_response.raise_for_status()

sunrise_data = sunrise_response.json()

sunrise = sunrise_data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = sunrise_data["results"]["sunset"].split("T")[1].split(":")[0]

time_now = datetime.now().hour


print(f"Your currently located in {my_location_data} and the time is {time_now}:00.\n"
      f"The International Space Stations current co-ordinates are {iss_coor} and will be visible from {sunset}:00 "
      f"till {sunrise}:00! ")



