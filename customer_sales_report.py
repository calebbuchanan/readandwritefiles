import csv

newlist = []
prior_ID = None

sales = open("sales.csv", "r")
infile = csv.reader(sales, delimiter=",")
outfile = open("salesreport.csv", "w")
next(infile)

for custID in infile:
    current_custID = int(custID[0])
    if prior_ID != current_custID:
        if prior_ID is not None:
            newlist.append([current_custID, round(total, 2)])
        prior_ID = current_custID
        total = float(custID[3]) + float(custID[4]) + float(custID[5])
    else:
        total = float(custID[3]) + float(custID[4]) + float(custID[5])

outfile.write("Customer ID " + "   " + "Total Pay")
outfile.write("\n")


for row in newlist:
    outfile.write(str(row[0]) + "   " + str(row[1]))
    outfile.write("\n")

outfile.close()
