import csv
import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QComboBox, QPushButton, QTableWidget, QTableWidgetItem


class OlympResult(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle("Результат олимпиады: фильтрация")
        self.setGeometry(0, 0, 600, 500)

        self.last_resp = {}
        self.schools = QComboBox(self)
        self.schools.addItem('Все')
        self.schools.setGeometry(20, 20, 150, 30)

        self.classes = QComboBox(self)
        self.classes.addItem('Все')
        self.classes.addItem('09')
        self.classes.addItem('10')
        self.classes.addItem('11')
        self.classes.setGeometry(220, 20, 150, 30)

        self.resultButton = QPushButton('Узнать результаты', self)
        self.resultButton.setGeometry(400, 20, 150, 30)

        self.tableWidget = QTableWidget(self)
        self.tableWidget.setGeometry(0, 50, 500, 500)

        with open('rez.csv', 'r', encoding='utf-8') as file:
            self.data = list(csv.DictReader(file, delimiter=','))

        self.resultButton.clicked.connect(self.find_info)
        self.fill_school_nums()

    def fill_school_nums(self):
        """ Заполняет QComboBox номерами школ. """
        history_nums = []

        for entry in self.data:
            s_num = entry['login'].split('-')[2]
            # print(entry)
            if s_num not in history_nums:
                history_nums.append(s_num)

        [self.schools.addItem(i) for i in sorted(history_nums)]

    def find_info(self):
        school = self.schools.currentText()
        class_num = self.classes.currentText()
        self.last_resp.clear()

        for entry in self.data:
            raw_data = entry['login'].split('-')
            s_num = raw_data[2]
            c_num = raw_data[3]

            if (class_num == school == 'Все') or \
                    (class_num == c_num and school == 'Все') or \
                    (school == s_num and class_num == 'Все'):

                surname = entry['user_name'].split()[3]
                score = entry['Score']

                self.last_resp[surname] = int(score)

            elif school == s_num and class_num == c_num:
                surname = entry['user_name'].split()[3]
                score = entry['Score']
                self.last_resp[surname] = int(score)

        self.fill_table()

    def fill_table(self):
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(['Фамилия', 'Результат'])

        row_count = len(self.last_resp.keys())
        self.tableWidget.setRowCount(row_count)

        scores = sorted(set([int(score) for _, score in self.last_resp.items()]))
        row_index = 0

        for el in scores[::-1]:
            for line in self.data:
                print(line)
                if el == int(line['Score']):
                    name = line['user_name'].split()[3]
                    self.tableWidget.setItem(row_index, 0, QTableWidgetItem(name))
                    self.tableWidget.setItem(row_index, 1, QTableWidgetItem(str(el)))
                    row_index += 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = OlympResult()
    ui.show()
    sys.exit(app.exec())
