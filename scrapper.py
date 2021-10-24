import requests
from bs4 import BeautifulSoup

r = requests.get(
    "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars")

# creating the soup
soup = BeautifulSoup(r.content, 'html.parser')

# getting all the <td>
td = soup.find_all("td")
values = []

# looping through the array of td and appending the stripped text to values list
for i in td:
    values.append(str(i.text).strip())


headers = ["V Mag", "Proper name", "Bayer designation",
           "Distance", "Spectral class", "Mass", "Radius", "Luminosity"]

print(values)
