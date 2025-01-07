import sys
import csv
import random

from PyQt6.QtWidgets import (QApplication, QMainWindow, QTableWidget,
                             QTableWidgetItem, QLineEdit, QLabel, QPushButton,
                             )
from PyQt6.QtGui import QColor


class Expensive(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(400, 400)
        self.tableWidget = QTableWidget(self)
        self.tableWidget.resize(400, 250)

        self.lbl1 = QLabel("Итого:", self)
        self.lbl1.setGeometry(150, 210, 70, 30)
        self.total = QLineEdit('0', self)
        self.total.setGeometry(200, 210, 70, 30)

        self.updateButton = QPushButton("Обновить", self)
        self.updateButton.setGeometry(20, 210, 70, 30)
        self.updateButton.clicked.connect(self.change_color)
        self.initUI()

    def initUI(self):
        with open('price.csv', 'r', newline='', encoding='utf-8') as file:
            data = list(csv.reader(file, delimiter=";"))
            headers = data[0]

            headers.append('Количество')
            self.tableWidget.setColumnCount(3)
            self.tableWidget.setHorizontalHeaderLabels(headers)
            self.tableWidget.setRowCount(len(data) - 1)

            data = data[1:]
            for el in range(len(data)):
                name, price, _ = data[el]
                data[el] = (name, int(price))

            data = sorted(data, key=lambda x: x[1], reverse=True)

            for index, row in enumerate(data):
                name, price = row

                self.tableWidget.setItem(index, 0, QTableWidgetItem(name))
                self.tableWidget.setItem(index, 1, QTableWidgetItem(str(price)))
                self.tableWidget.setItem(index, 2, QTableWidgetItem('0'))

        self.tableWidget.itemChanged.connect(self.update_total)
        self.update_total()
        self.change_color()

    def update_total(self):
        total = 0
        for row in range(self.tableWidget.rowCount()):
            price = self.tableWidget.item(row, 1)
            quantity = self.tableWidget.item(row, 2)

            price = int(price.text())
            quantity = int(quantity.text())

            total += price * quantity
        self.total.setText(str(total))

        if self.total:
            self.total.setText(str(self.total.text()))
        else:
            if not self.total:
                self.total.setText('0')

    def change_color(self):
        for row in range(self.tableWidget.rowCount()):
            if row < 5:
                r, g, b = self.get_random_color()
                for column in range(3):
                    item = self.tableWidget.item(row, column)
                    if item:
                        item.setBackground(QColor(r, g, b))

    def get_random_color(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return r, g, b


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Expensive()
    ex.show()
    sys.exit(app.exec())
