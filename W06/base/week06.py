
import csv
file_name = "life-expectancy.csv"
data = []

with open(file_name, "r") as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row/ salta el encabezado del archivo csv
    for row in reader:
        data.append(row)
# 2. Find the year and country with the lowest life expectancy in the dataset

lowest_life_expectancy = float(data[0][3])
lowest_life_expectancy_year = data[0][2]
lowest_life_expectancy_country = data[0][1]

for row in data:
    life_expectancy = float(row[3])
    if life_expectancy < lowest_life_expectancy:
        lowest_life_expectancy = life_expectancy
        lowest_life_expectancy_year = row[2]
        lowest_life_expectancy_country = row[0]
# 3. Find the year and country with the highest life expectancy in the dataset

highest_life_expectancy = float(data[0][3])
highest_life_expectancy_year = data[0][2]
highest_life_expectancy_country = data[0][1]

for row in data:
    life_expectancy = float(row[3])
    if life_expectancy > highest_life_expectancy:
        highest_life_expectancy = life_expectancy
        highest_life_expectancy_year = row[2]
        highest_life_expectancy_country = row[1]
# 4. Allow the user to input a year and find a average life expectancy for that year

year = input("Enter a year: ")
total_expectancy = 0
count = 0

for row in data:
    if row[0] == year:
        total_expectancy += float(row[3])
        count += 1
if count > 0:
    average_expectancy = total_expectancy/count
    print("Average expectancy for year", year, ":", average_expectancy)
else:
    print("No data available for the entered year.")
# Find  the contrie with the minimun and maximub life expectancies for the entered year

min_expectancy_contry = 0
max_expectancy_contry = 0

for row in data:
    if row[0] == year:
        life_expectancy = float(row[3])
        if life_expectancy == lowest_life_expectancy:
            min_expectancy_contry = row[1]
        if life_expectancy == highest_life_expectancy:
            max_expectancy_contry = row[1]
# Print the results

print("Year and contry with the lowest life expectancy:",
      lowest_life_expectancy, "-", lowest_life_expectancy_country)
print("Year and contry with the highest life expectancy:",
      highest_life_expectancy, "-", highest_life_expectancy_country)
print("Contry with the minimun life expectnacy for year:",
      year, "-", min_expectancy_contry)
print("Contry with the maximun life expectnacy for year:",
      year, "-", max_expectancy_contry)
