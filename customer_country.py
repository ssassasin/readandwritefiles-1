import csv

with open("customers.csv","r") as infile, open("customer_country.csv","w",newline="") as outfile:
    reader =csv.reader(infile)
    writer= csv.writer(outfile)

    headers=next(reader)
    first_index=headers.index("First Name")
    last_index=headers.index("Last Name")
    country_index=headers.index("Country")

    writer.writerow(["Customer Name","Country"])

    for row in reader:
        name=f"{row[first_index]}{row[last_index]}"
        country= row[country_index]
        writer.writerow([name,country])
        