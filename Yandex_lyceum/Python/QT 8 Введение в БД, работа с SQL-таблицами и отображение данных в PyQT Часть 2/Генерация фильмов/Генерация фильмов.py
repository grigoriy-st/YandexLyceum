import sys
import sqlite3

from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QTableWidget,
    QPushButton, QLineEdit, QMessageBox, QStatusBar,
    QTableWidgetItem
)


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(500, 400)
        self.textEdit = QLineEdit(self)
        self.textEdit.setGeometry(10, 10, 200, 60)

        self.pushButton = QPushButton('Запуск', self)
        self.pushButton.setGeometry(250, 20, 100, 30)

        self.saveButton = QPushButton('Изменить', self)
        self.saveButton.setGeometry(350, 20, 100, 30)

        self.tableWidget = QTableWidget(self)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setGeometry(10, 100, 480, 250)

        self.msg = QMessageBox(self)
        self.msg.hide()
        self.msg.setGeometry(500, 500, 300, 100)

        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)

        self.pushButton.clicked.connect(self.find_el_in_db)
        self.saveButton.clicked.connect(self.choose)

    def find_el_in_db(self):
        id_num = self.textEdit.text().split('=')[-1]
        con = sqlite3.connect('films_db.sqlite')
        cur = con.cursor()

        try:
            result = cur.execute(f'''
                select
                    films.title,
                    films.year,
                    films.genre,
                    films.duration
                from films inner join genres on films.id = genres.id
                where films.id = {id_num}
            ''').fetchall()

            if result:
                self.statusBar.showMessage("")

                self.tableWidget.setRowCount(len(result))

                for index, line in enumerate(result):
                    title, year, genre, duration = line
                    self.fill_table(id_num, title, year, genre, duration)
            else:
                self.statusBar.showMessage(
                    "По этому запросу ничего не найдено"
                )
        except sqlite3.OperationalError:
            self.statusBar.showMessage("По этому запросу ничего не найдено")
        finally:
            con.close()

    def choose(self):
        id_num = int(self.textEdit.text().split('=')[-1])
        btn_question = f'Действительно заменить элементы с id {id_num}'
        buttons = (QMessageBox.StandardButton.No |
                   QMessageBox.StandardButton.Yes)
        button = self.msg.question(self, "Заголовок", btn_question,
                                   buttons=buttons
                                   )

        if button == QMessageBox.StandardButton.Yes:
            con = sqlite3.connect('films_db.sqlite')
            cur = con.cursor()

            result = cur.execute(f'''
                    select
                        films.title,
                        films.year,
                        films.genre,
                        films.duration
                    from films inner join genres on films.id = genres.id
                    where films.id={id_num}
                    ''').fetchall()
            self.tableWidget.setRowCount(len(result))

            title, year, genre, duration = result[0]
            title = str(title)[::-1]
            year += 1000
            duration *= 2

            result = cur.execute(f'''
                    update films
                    set
                        title = '{title}',
                        year = {year},
                        duration = {duration}
                    where films.id = {id_num}
                    ''').fetchall()
            con.commit()
            self.fill_table(id_num, title, year, genre, duration)
            con.close()

    def fill_table(self, id_num, title, year, genre, duration):
        self.tableWidget.setItem(0, 0, QTableWidgetItem(str(id_num)))
        self.tableWidget.setItem(0, 1, QTableWidgetItem(title))
        self.tableWidget.setItem(0, 2, QTableWidgetItem(str(year)))
        self.tableWidget.setItem(0, 3, QTableWidgetItem(str(genre)))
        self.tableWidget.setItem(0, 4, QTableWidgetItem(str(duration)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
