from sys import stdin
import csv

lines = stdin.readlines()
headers = ['nomen', 'definitio', 'pluma', 'Russian nomen',
           'familia', 'Russian nomen familia']

with open('plantis.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file, delimiter=';',
                        quoting=csv.QUOTE_NONE, escapechar='\\')
    writer.writerow(headers)

    for line in lines:
        writer.writerow(line.rstrip('\n').split('\t'))
