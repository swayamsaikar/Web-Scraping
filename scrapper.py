import pandas as pd
import requests
from bs4 import BeautifulSoup

r = requests.get(
    "https://en.wikipedia.org/wiki/List_of_brown_dwarfs")

# creating the soup
soup = BeautifulSoup(r.content, 'html.parser')


planet_row_data_list = []

# getting the table of values out of 4 tables
fourth_table = soup.find_all(
    'table', class_="wikitable")[0]

tbody_tag = fourth_table.find_all('tbody')

for tr in tbody_tag:
    for td in tr:
        # appending every group of text as [] because [] <- represents each row
        planet_row_data_list.append([str(td.text).strip()])


# the first element of this planet_row_data_list is the header so we have to remove that
planet_row_data_list.pop(0)

# just removed the empty string array ex -> [""]
without_empty_strings_list = [
    string for string in planet_row_data_list if string != [""]]


# now we ll create different arrays for different values
star = []
Constellation = []
Right_ascension = []
Discovery_year = []

# now we will filter the list by removing the \n and splitting it by " " and making each value a separate element in the list
filtered_planet_list = []
for eachrow in without_empty_strings_list:

    for i in eachrow:
        if "\n" in i:
            p = i.replace("\n", "")
            p = p.split(" ")
            filtered_planet_list.append(p)


# now we ll loop through filtered_planet_list and :-
'''
every array inside this filtered_planet_list is a row
so i ll loop through filtered_planet_list and all of the respective values to their respective lists
ex -> ["piscum","pisces","0 deg","2006"] <- a row. so here the first element of this list is the star and the second element is constellation
👆 like this i ll append it
'''
for row in filtered_planet_list:
    star.append(row[0])
    Constellation.append(row[1])
    Right_ascension.append(row[2])
    year = f"{row[-1][-4]}{row[-1][-3]}{row[-1][-2]}{row[-1][-1]}"
    Discovery_year.append(year)


# now its time to convert it to a csv
d = {
    'stars': star,
    'Constellations': Constellation,
    'Right_ascension': Right_ascension,
    'Discovery_year': Discovery_year
}

# creating a dataframe
df = pd.DataFrame(data=d)

# converting it to csv
df.to_csv("most_frustrated_project_made_by_swayam_sai_kar.csv")
