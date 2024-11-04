import io
import sys
import sqlite3

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.errorLabel = QLabel(self)
        self.errorLabel.setGeometry(10, 250, 200, 40)
        self.errorLabel.setVisible(False)
        self.filter_list = {
            'Название': 'title',
            'Год выпуска': 'year',
            'Продолжительность': 'duration',
        }

        self.queryButton.clicked.connect(self.find)

    def find(self):
        filter_name = self.parameterSelection.currentText()
        text_filter = self.queryLine.text()

        con = sqlite3.connect('films.db')
        cur = con.cursor()

        db_elem = self.filter_list[filter_name]
        result = cur.execute(f"""select films.id,
                                        films.title,
                                        films.year,
                                        films.genre,
                                        films.duration
        from films inner join genres on genres.id=films.genre\
        where films.{db_elem}='{text_filter}'""").fetchall()

        if result:
            self.errorLabel.setVisible(False)
            self.errorLabel.setText('')
            id, title, year, genre, duration = result[0]
            self.idEdit.setText(str(id))
            self.titleEdit.setText(title)
            self.yearEdit.setText(str(year))
            self.genreEdit.setText(str(genre))
            self.durationEdit.setText(str(duration))
        elif text_filter == '':
            self.clear_edit_lines()
            self.errorLabel.setText("Неправильный запрос")
            self.errorLabel.setVisible(True)
        else:
            self.clear_edit_lines()

            self.errorLabel.setText("Ничего не найдено")
            self.errorLabel.setVisible(True)

    def clear_edit_lines(self):
        self.idEdit.clear()
        self.titleEdit.clear()
        self.yearEdit.clear()
        self.genreEdit.clear()
        self.durationEdit.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
