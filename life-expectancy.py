with open("life-expectancy.csv", "r") as file:
    file.readline()
    years = []
    countries = []
    expectancies = []

    for line in file:
        line = line.strip()
        line = line.split(",")

        country = line[0]
        year = line[2]
        expectancy = line[3]

        countries.append(country)
        years.append(year)
        expectancies.append(expectancy)


year_of_interest = int(input("Please enter the year of interest: "))
print()
print(f"The overall max life expectancy is: {max(expectancies)} from {countries[expectancies.index(max(expectancies))]} in the year {years[expectancies.index(max(expectancies))]}.")
print(f"The overall max life expectancy is: {min(expectancies)} from {countries[expectancies.index(min(expectancies))]} in the year {years[expectancies.index(min(expectancies))]}.")
print()
print(f"From the year {year_of_interest}:")
year_of_interest_list = []
total = 0
for element in range(len(years)):
    if year_of_interest == float(years[element]):
        year_of_interest_list.append(expectancies[element])

for e in year_of_interest_list:
    total += float(e)
print(f"The average life expectancy across all countries was {round(total/len(year_of_interest_list),2)}")
print(f"The maximum life expectancy was in {countries[expectancies.index(max(year_of_interest_list))]} in the year {max(year_of_interest_list)}")
print(f"The maximum life expectancy was in {countries[expectancies.index(min(year_of_interest_list))]} in the year {min(year_of_interest_list)}")