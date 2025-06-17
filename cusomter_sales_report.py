import csv
from collections import defaultdict

totals= defaultdict(float)

with open("sales.csv") as infile:
    reader=csv.DictReader(infile)
    for row in reader:
        totals[row["Customer ID"]]+=float(row["Amount"])

with open("salesreport.csv","w",newline="") as outfile:
    writer=csv.writer(outfile)
    writer.writerow(["Customer ID","Total"])
    for cid, total in totals.items():
        writer.writerow([cid,f"{total:.2f}"])

    