import csv
import openpyxl

wb = openpyxl.load_workbook(filename='data.xlsx', data_only=True)

with open('output.csv', mode='w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file, delimiter=';', quotechar='"')
    for sheet in wb.worksheets:
        for row in sheet.iter_rows(values_only=True):
            writer.writerow(row)