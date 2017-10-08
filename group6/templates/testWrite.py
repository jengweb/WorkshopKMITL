import csv

with open('names.csv', 'w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'first_name': 'Baimon', 'last_name': 'Kradae'})
    writer.writerow({'first_name': 'Ji', 'last_name': 'Dwarf'})
    writer.writerow({'first_name': 'Pungpond111', 'last_name': 'Narak'})