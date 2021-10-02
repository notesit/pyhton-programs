import csv

def save_mobile():
    name = str(input("Enter mobile contact:"))
    mobile = str(input("Enter mobile number:"))
    with open("mobile.csv", "a+", encoding='UTF8') as f:
        writer  = csv.writer(f)
        writer.writerow([name, mobile])

def read_mobile():
    with open("mobile.csv", "r", encoding='UTF8') as f:
        reader = csv.reader(f)
        for line in reader:
            print(line)

print("1. Save mobile number on CSV")
print("2. Display mobile number from CSV")
menu = int(input("Enter you menu number [1,2]:"))

if menu == 1:
    save_mobile()
elif menu == 2:
    read_mobile()

