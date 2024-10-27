import sys
import csv

from PyQt6.QtWidgets import (QApplication, QMainWindow, QTableWidget,
                             QTableWidgetItem, QLineEdit, QLabel)


class InteractiveReceipt(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(400, 400)
        self.tableWidget = QTableWidget(self)
        self.tableWidget.resize(400, 250)

        self.lbl1 = QLabel("Итого:", self)
        self.lbl1.setGeometry(150, 210, 70, 30)
        self.total = QLineEdit('0', self)
        self.total.setGeometry(200, 210, 70, 30)

        self.initUI()

    def initUI(self):

        with open('price.csv', 'r', newline='', encoding='utf-8') as file:
            data = list(csv.reader(file, delimiter=";"))
            headers = data[0]

            headers.append('Количество')
            self.tableWidget.setColumnCount(3)
            self.tableWidget.setHorizontalHeaderLabels(headers)
            self.tableWidget.setRowCount(len(data) - 1)

            for index, row in enumerate(data[1:]):
                name, price, _ = row

                self.tableWidget.setItem(index, 0, QTableWidgetItem(name))
                self.tableWidget.setItem(index, 1, QTableWidgetItem(price))

        self.tableWidget.itemChanged.connect(self.update_total)
        self.update_total()

    def update_total(self):

        for row in range(self.tableWidget.rowCount()):
            price = self.tableWidget.item(row, 1)
            quantity = self.tableWidget.item(row, 2)

            if quantity:
                price = int(price.text())
                quantity = int(quantity.text())
                self.total += price * quantity

        if self.total:
            self.total.setText(str(self.total))
        else:
            if not self.total:
                self.total.setText('0')

    def add_contact(self):
        ...


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = InteractiveReceipt()
    ex.show()
    sys.exit(app.exec())
