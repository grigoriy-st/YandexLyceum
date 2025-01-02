import sys
import sqlite3

from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton,
    QTableWidget, QTableWidgetItem, QStatusBar
)


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(550, 520)
        self.statusBar().showMessage("")

        ru_up_alfb = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        self.buttons = []
        for i, let in enumerate(ru_up_alfb):
            btn = QPushButton(let, self)
            btn.setGeometry(i * 30, 30, 30, 30)
            if i > 15:
                btn.setGeometry((i - 16) * 30, 60, 30, 30)

            btn.clicked.connect(self.click_on_let)
            self.buttons.append(btn)

        self.tableWidget = QTableWidget(self)
        self.tableWidget.setGeometry(5, 90, 500, 400)
        self.tableWidget.setColumnCount(5)
        headers = ['ID', 'Название', 'Год', 'Жанр', 'Продолжительность']
        self.tableWidget.setHorizontalHeaderLabels(headers)

    def click_on_let(self):
        btn_name = self.sender().text()

        con = sqlite3.connect('films_db.sqlite')
        cur = con.cursor()
        result = cur.execute(
            f'''
            select
                films.id,
                films.title,
                films.year,
                genres.title,
                films.duration
            from films inner join genres on genres.id = films.genre
            where films.title like '{btn_name}%'
            '''
        ).fetchall()
        con.close()

        self.tableWidget.setRowCount(0)
        if result:
            n = len(result)
            self.tableWidget.setRowCount(n)
            for row, line in enumerate(result):
                rec_id, title, year, genre, duration = line
                self.tableWidget.setItem(row, 0, QTableWidgetItem(str(rec_id)))
                self.tableWidget.setItem(row, 1, QTableWidgetItem(title))
                self.tableWidget.setItem(row, 2, QTableWidgetItem(str(year)))
                self.tableWidget.setItem(row, 3, QTableWidgetItem(genre))
                self.tableWidget.setItem(row, 4,
                                         QTableWidgetItem(str(duration)))

            self.statusBar().showMessage(f'Нашлось {n} записей')
        else:
            self.statusBar().showMessage("К сожалению, ничего не нашлось")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
