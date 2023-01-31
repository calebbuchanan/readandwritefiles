import csv

infile = open("EmployeePay.csv", "r")
employee = csv.reader(infile, delimiter=",")
next(employee)


for record in employee:
    salary = float(record[3])
    bonus = float(record[4]) * float(record[3])
    total = bonus + salary

    print("First name: ", record[1])
    print("Last name: ", record[2])
    print("Salary: ", salary)
    print("Bonus: ", bonus)
    print("Total pay: ", total)
