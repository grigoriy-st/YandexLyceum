import sys
import sqlite3

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt6 import uic

DB_NAME = './database.sql'

class AboutBootDialog(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('./about_book_dialog.ui', self)


class LibraryCatalog(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('./main_dialog.ui', self)

        self.last_resp = None   # Список записей из последнего запроса
        self.setupUI()

    def setupUI(self):
        self.btn_find.clicked.connect(self.find_data)   # кнопка поиска

        self.list_widget.itemClicked.connect(self.open_info_window) # обработка клика по элементу списка


    def find_data(self):
        """ Поиск данных. """
        filter = self.cb_filter.currentText()
        line_text = self.le_search_box.text()

        if filter == 'Название':
            filter = 'name'
        if filter == 'Автор':
            filter = 'author'

        self.db_ops(filter, line_text)

    def db_ops(self, filter, line_text):
        """ Операции с БД. """
        con = sqlite3.connect(DB_NAME)
        cur = con.cursor()

        q_parametr = None   # Часть запроса
        if filter == 'name':
            q_parametr = f'''
                        catalog.title LIKE '%{line_text}%'
                        '''
        elif filter == 'author':
            q_parametr = f'''
                        authors.name LIKE '%{line_text}%'
                        '''

        q = f'''
            select 
                title, Authors.name, year, 
                Genres.genre, image_path
            from catalog
            inner join 
                authors on authors.id = author,
                genres on genres.id = catalog.genre
            where
                {q_parametr}
            '''
        self.last_resp = list(cur.execute(q))   # запись в переменную последнего ответа

        self.list_widget.clear()

        for element in self.last_resp:
            self.list_widget.addItem(element[0])    # Добавление записей в список

    def open_info_window(self, item):
        """ Открытие второго окна. """
        info_window = AboutBootDialog()
        book_title = item.text()    # Получение названия элемента списка по клику

        for entry in self.last_resp:    # Поиск название книги в результатах последнего ответа
            if book_title in entry:
                info_window.lbl_book_name.setText(entry[0])
                info_window.lbl_book_author.setText(entry[1])
                info_window.lbl_book_year.setText(str(entry[2]))
                info_window.lbl_book_genre.setText(entry[3])

                if entry[4]:    # Проверка на то, есть картинка у книги
                    img = QPixmap(entry[4])
                else:
                    img = QPixmap('./std.png')  # Установка стандартного изображения
                info_window.lbl_for_image.setPixmap(img)

        info_window.exec()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = LibraryCatalog()
    ui.show()
    sys.exit(app.exec())