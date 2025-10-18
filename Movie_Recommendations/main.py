import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)

website_data = response.text

soup = BeautifulSoup(website_data, "html.parser")

print(soup.prettify())