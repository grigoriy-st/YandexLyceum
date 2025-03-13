import csv
import sys
from PyQt6.QtGui import QBrush, QColor
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QTableWidget, QLineEdit, QLabel, QTableWidgetItem
)

DECEASED_COLOR = '#FF0000'
SURVIVOR_COLOR = '#00FF00'


class TitanicSearch(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(700, 400)
        self.setupUI()

    def setupUI(self):
        self.label = QLabel("Подстрока для поиска:", self)
        self.label.setGeometry(10, 10, 150, 30)
        self.searchEdit = QLineEdit(self)
        self.searchEdit.setGeometry(170, 10, 300, 30)
        self.searchEdit.textEdited.connect(self.find_info)

        table_headers = ['PassengerID', 'Name', 'PClass', 'Age', 'Sex', 'Survived', 'SexCode']
        self.resultTable = QTableWidget(self)
        self.resultTable.setHorizontalHeaderLabels(table_headers)
        self.resultTable.setGeometry(50, 50, 670, 350)
        self.std_table_filling()

    def find_info(self):
        substr = self.searchEdit.text()

        self.resultTable.setRowCount(0)
        if len(substr) < 3:
            self.std_table_filling()
            return

        with open('titanic.csv', 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file, quotechar='"')
            rows = list(reader)

            index = 0
            for row in rows[1:]:
                if row[1].lower().find(substr.lower()) != -1:

                    self.resultTable.insertRow(index)
                    for col, item in enumerate(row):
                        table_item = QTableWidgetItem(item)
                        self.resultTable.setItem(index, col, table_item)

                        if row[-2] == '1':
                            brush = QBrush(QColor(SURVIVOR_COLOR))
                        else:
                            brush = QBrush(QColor(DECEASED_COLOR))
                        table_item.setBackground(brush)
                    index += 1

    def std_table_filling(self):
        self.resultTable.setColumnCount(7)

        with open('titanic.csv', 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file, quotechar='"')
            rows = list(reader)

            self.resultTable.setRowCount(len(rows) - 1)

            for index, row in enumerate(rows[1:]):
                for col, item in enumerate(row):
                    table_item = QTableWidgetItem(item)
                    self.resultTable.setItem(index, col, table_item)

                    if row[-2] == '1':
                        brush = QBrush(QColor(SURVIVOR_COLOR))
                    else:
                        brush = QBrush(QColor(DECEASED_COLOR))
                    table_item.setBackground(brush)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = TitanicSearch()
    ui.show()
    sys.exit(app.exec())
