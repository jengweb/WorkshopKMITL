import csv
import pandas as pd
def read_file():
    with open('test2.csv', 'r') as f:
      reader = csv.reader(f)
      my_list = list(reader)
    return(my_list)
#main
def main():
    
    list=read_file()
    print(list)
    array_length = len(list)    
    data  = input("Enter data: ")
    print(list[1][1])
    
with open('test.csv', 'w', newline='') as csvfile:
    fieldnames = ['name', 'id','bal']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'name': 'GAG', 'id': '58010418', 'bal' : 2000.00})
    writer.writerow({'name': 'Beam', 'id': '58010622', 'bal' : 400.00})

    
with open('test2.csv', 'w', newline='') as csvfile:
    fieldnames = ['id', 'price',]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'id': '1234567890', 'price' : 500.00})
    writer.writerow({'id': '1234567899', 'price' : 5000.00})

    
with open('test.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['name'], row['id'],row['bal'])
    
main()
