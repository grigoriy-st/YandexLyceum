import sqlite3
import sys

from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QTableWidget,
    QTableWidgetItem, QPushButton, QPlainTextEdit,
    QComboBox, QWidget, QLabel, QStatusBar
)


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(700, 500)
        self.add_form = None

        self.addButton = QPushButton("Добавить", self)
        self.addButton.setGeometry(10, 10, 70, 30)
        self.addButton.clicked.connect(self.adding)

        self.tableWidget = QTableWidget(self)
        self.tableWidget.setGeometry(10, 50, 650, 450)
        headers = ['ИД', 'Название фильма', 'Год выпуска',
                   'Жанр', ' Продолжительность']
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(headers)
        self.update_table()

    def adding(self):
        self.add_form = AddWidget(self)
        self.add_form.show()

    def update_table(self):
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
            order by films.id desc
            '''
        ).fetchall()
        con.close()

        self.tableWidget.setRowCount(len(result))

        for index, rec in enumerate(result):
            rec_id, title, year, genre, duration = rec

            self.tableWidget.setItem(index, 0, QTableWidgetItem(str(rec_id)))
            self.tableWidget.setItem(index, 1, QTableWidgetItem(str(title)))
            self.tableWidget.setItem(index, 2, QTableWidgetItem(str(year)))
            self.tableWidget.setItem(index, 3, QTableWidgetItem(str(genre)))
            self.tableWidget.setItem(index, 4, QTableWidgetItem(str(duration)))





class AddWidget(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent

        self.initUI()

    def initUI(self):
        self.resize(300, 300)
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)

        self.lbl_title = QLabel("Название", self)
        self.lbl_title.setGeometry(0, 10, 100, 30)
        self.title = QPlainTextEdit(self)
        self.title.setGeometry(100, 10, 200, 30)

        self.lbl_year = QLabel("Год выпуска", self)
        self.lbl_year.setGeometry(0, 50, 100, 30)
        self.year = QPlainTextEdit(self)
        self.year.setGeometry(100, 50, 200, 30)

        self.lbl_gen = QLabel("Жанр", self)
        self.lbl_gen.setGeometry(0, 90, 100, 30)
        self.comboBox = QComboBox(self)
        self.comboBox.setGeometry(100, 90, 200, 30)
        con = sqlite3.connect('films_db.sqlite')
        cur = con.cursor()
        self.params = cur.execute(
            '''
            select distinct genres.title
            from films inner join genres on genres.id = films.genre
            '''
        ).fetchall()
        cur.close()
        self.params = {genre[0]: index for index, genre in enumerate(self.params)}
        self.comboBox.addItems(self.params.keys())

        self.lbl_dur = QLabel("Длина", self)
        self.lbl_dur.setGeometry(0, 130, 100, 30)
        self.duration = QPlainTextEdit(self)
        self.duration.setGeometry(100, 130, 200, 30)

        self.pushbutton = QPushButton('Добавить', self)
        self.pushbutton.setGeometry(150, 250, 100, 30)
        self.pushbutton.clicked.connect(self.exec_query)

    def exec_query(self):
        self.statusBar.showMessage("")

        title = self.title.toPlainText()
        year = self.year.toPlainText()
        genre = self.comboBox.currentText()
        duration = self.duration.toPlainText()
        correct_input = self.get_adding_verdict(title, year, genre, duration)

        if not correct_input:
            self.statusBar.showMessage("Неверно заполнена форма")

    def get_adding_verdict(self, title, year, genre, duration):
        if not year.isdigit():
            return False
        if not title or not year or not genre or not duration:
            return False

        genre_id = self.params[genre]
        con = sqlite3.connect('films_db.sqlite')
        cur = con.cursor()
        try:
            _ = cur.execute(
                f'''
                insert into films
                (title, year, genre, duration)
                values ('{title}', {year}, {genre_id}, {duration})
                '''
            )
            con.commit()
            self.parent.update_db()
            self.close()

        except sqlite3.OperationalError:
            self.statusBar.showMessage("Неверно заполнена форма")
        finally:
            cur.close()
        return True



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())