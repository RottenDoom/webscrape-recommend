from bs4 import BeautifulSoup
import requests

url = "https://myanimelist.net/"

# ask for requests
result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

# print(doc.prettify())

# write the file into target.html
with open("target.html", "w", encoding="utf-8") as file:
    file.write(doc.prettify())