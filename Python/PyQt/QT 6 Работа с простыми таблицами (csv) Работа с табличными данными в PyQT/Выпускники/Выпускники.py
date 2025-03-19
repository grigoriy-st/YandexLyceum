import csv

num = int(input())

with open('vps.csv', 'r', newline='', encoding='utf-8') as file:
    data = list(csv.reader(file, delimiter=";"))

for row in data[1:]:
    if int(row[4]) >= num:
        print(row[0])
#     headers.append('Количество')
#     self.tableWidget.setColumnCount(3)
#     self.tableWidget.setHorizontalHeaderLabels(headers)
#     self.tableWidget.setRowCount(len(data) - 1)
#
#     for index, row in enumerate(data[1:]):
#         name, price, _ = ro
#         self.tableWidget.setItem(index, 0, QTableWidgetItem(name))
#         self.tableWidget.setItem(index, 1, QTableWidgetItem(price))
#
# tableWidget.itemChanged.connect(self.update_total)
# update_total()