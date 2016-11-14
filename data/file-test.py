# read file countries.txt
f = open("countries.txt", "r")
countries = []

for line in f:
    # removes newline at the end of each line from text file
    line = line.strip()
    # prints each line in countries.txt
    print(line)
    # creates list of countries
    countries.append(line)

print (countries)

# loops through and prints countries that start with "P"
counter = 0
for country in countries:
    if country[0] == "P":
        print(country)
        counter += 1
print ("There are {} countries that start with P".format(counter))

# loops through and prints countries that contain 'ar'
counter = 0
for country in countries:
    if "ar" in country:
        print(country)
        counter += 1
print ("There are {} countries that contain 'ar'".format(counter))


f.close()
