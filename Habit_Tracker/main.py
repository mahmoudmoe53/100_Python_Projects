import requests
import os
from dotenv import load_dotenv
from datetime import datetime

GRAPH_ID = "graph1"

load_dotenv()
pixela_username = os.environ.get("PIXELA_USERNAME")
pixela_token = os.environ.get("PIXELA_TOKEN")

pixela_endpoint = "https://pixe.la/v1/users"

pixela_parameters = {
    "token":pixela_token,
    "username":pixela_username,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

pixela_response = requests.post(url=pixela_endpoint, json=pixela_parameters)

graph_endpoint = f"{pixela_endpoint}/{pixela_username}/graphs"

graph_parameters = {
    "id":GRAPH_ID,
    "name":"Hours Spent Coding",
    "unit":"Hours",
    "type":"int",
    "color":"shibafu"
}



headers = {
    "X-USER-TOKEN":pixela_token
}


today = datetime.now()
formatted_date = today.strftime("%Y%m%d")

post_pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

post_pixel_parameters = {
    "date":formatted_date,
    "quantity":"0"
}


update_pixel_parameters = {
    "quantity":input("How many hours did you spend coding today?")
}


update_pixel_response = requests.put(url=f"{post_pixel_endpoint}/{formatted_date}",
                                      json=update_pixel_parameters, headers=headers)

print(update_pixel_response.text)
