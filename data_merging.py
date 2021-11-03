import csv

sorted_data = []
actual_data = []

with open("sorted_year_data.csv", "r") as f:
    reader = csv.reader(f)
    for i in reader:
        sorted_data.append(i)

with open("most_frustrated_project_made_by_swayam_sai_kar.csv", "r") as f:
    reader = csv.reader(f)
    for i in reader:
        actual_data.append(i)


header_sorted = sorted_data[0]
sorted_only_data = sorted_data[1:]


header_actual = actual_data[0]
actual_only_data = actual_data[1:]

header = header_actual+header_sorted
data = actual_only_data+sorted_only_data


with open("finaldata.csv", "a+") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)
