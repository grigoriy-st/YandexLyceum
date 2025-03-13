import csv

with open('wares.csv', 'r', encoding='utf-8') as file:
    data = list(csv.DictReader(file, delimiter=';'))

    for row in data[1:]:
        if int(row['Old price']) > int(row['New price']):
            print(row['Name'])
