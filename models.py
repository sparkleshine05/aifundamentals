import csv
with open("students.csv" , "w", newline="") as f: #f can be any name
    writer = csv.writer(f)
    writer.writerow(["Name","Age","Grade"])
    writer.writerow(["Alice", 14, "8th"])
    writer.writerow(["Bob", 15, "9th"])
    writer.writerow(["Charlie", 14, "8th"])
    writer.writerow(["Swati", 15, "9th"])

with open("students.csv", "r") as f:
    reader = csv.reader(f)
    for i in reader:
        print(i)