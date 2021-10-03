import csv

def create_mobile():
    name = str(input("Enter mobile contact:"))
    mobile = str(input("Enter mobile number:"))
    headers = ['name', 'mobile']
    with open("mobile.csv", "a+", encoding='UTF8') as f:
        writer  = csv.DictWriter(f,fieldnames=headers)
        writer.writerow({'name':name, 'mobile':mobile})

def read_mobile():
    headers = ['name', 'mobile']
    with open("mobile.csv", "r", encoding='UTF8') as f:
        reader = csv.DictReader(f,fieldnames=headers)
        print("Row\tName\tMobile\t")
        row_index = 1
        for line in reader:
            print(row_index, "\t", line['name'],"\t",line["mobile"])
            row_index = row_index + 1

print("1. Create a new mobile number on CSV")
print("2. Read all mobile numbers from CSV")
menu = int(input("Enter you menu number [1,2]:"))

if menu == 1:
    create_mobile()
elif menu == 2:
    read_mobile()
