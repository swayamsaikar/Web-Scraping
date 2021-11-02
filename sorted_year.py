import csv

df = []

with open("most_frustrated_project_made_by_swayam_sai_kar.csv", "r") as f:
    reader = csv.reader(f)
    for i in reader:
        df.append(i)


header = df[0]
data = df[1:]

# sorting the year_data into descending order and merging it with our actual file
data.sort(key=lambda planet_data: planet_data[-1], reverse=True)


with open("final_sorted_year_data.csv", "a+") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)
