import csv

customers = open("customers.csv", "r")
infile = csv.reader(customers, delimiter=",")
outfile = open("customer_country.csv", "w")
count = 0

for record in infile:
    outfile.write(f"{record[1]}, {record[2]}, {record[4]}")
    outfile.write("\n")
    count += 1

outfile.close()
customers.close()
print(count - 1)
