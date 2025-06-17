import csv
with open("employee_data.csv","r") as file:
    reader= csv.DictReader(file)

    for row in reader:
        name=row["Name"]
        salary=float(row["Salary"])
        bonus=float(row["Bonus"])
        pay= salary+ bonus

        print(f"Name: {name}")
        print(f"Salary: ${salary:,.2f}")
        print(f"Bonus: ${bonus:,.2f}")
        print(f"Pay: ${pay:,.2f}\n")
        input("Press enter to continue...")
        