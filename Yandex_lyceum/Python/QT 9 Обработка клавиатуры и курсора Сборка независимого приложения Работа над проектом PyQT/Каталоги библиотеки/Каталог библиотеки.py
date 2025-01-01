import sys
import sqlite3
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt6 import uic

DB_NAME = './database.sql'

class LibraryCatalog(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('./main_dialog.ui', self)
        self.setupUI()

    def setupUI(self):
        self.btn_find.clicked.connect(self.find_data)

    def find_data(self):
        filter = self.cb_filter.currentText()
        line_text = self.le_search_box.text()

        if filter == 'Название':
            filter = 'name'
        if filter == 'Автор':
            filter = 'author'

        self.db_ops(filter, line_text)


    def db_ops(self, filter, line_text):
        con = sqlite3.connect(DB_NAME)
        cur = con.cursor()

        q_parametr = None
        if filter == 'name':
            q_parametr = f'''
                        authors.name == {line_text}
                        '''
        elif filter == 'author':
            q_parametr = f'''
                        authors.name == {line_text}
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
        data = cur.execute(q)
        for element in data:
            self.list_widget.addItem(element[0])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = LibraryCatalog()
    ui.show()
    sys.exit(app.exec())