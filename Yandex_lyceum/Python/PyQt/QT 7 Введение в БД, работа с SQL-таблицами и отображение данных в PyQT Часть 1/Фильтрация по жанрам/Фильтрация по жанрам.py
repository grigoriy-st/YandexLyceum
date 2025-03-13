import io
import sys
import sqlite3

from PyQt6 import uic
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QTableWidgetItem
)

template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>620</width>
    <height>364</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QTableWidget" name="tableWidget">
    <property name="geometry">
     <rect>
      <x>130</x>
      <y>0</y>
      <width>481</width>
      <height>321</height>
     </rect>
    </property>
   </widget>
   <widget class="QPushButton" name="queryButton">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>50</y>
      <width>80</width>
      <height>24</height>
     </rect>
    </property>
    <property name="text">
     <string>Пуск</string>
    </property>
   </widget>
   <widget class="QComboBox" name="parameterSelection">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>10</y>
      <width>121</width>
      <height>24</height>
     </rect>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>620</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.initUI()

    def initUI(self):

        con = sqlite3.connect('films_db.sqlite')
        cur = con.cursor()

        result = cur.execute('''
            select distinct genres.title
            from films inner join genres on films.genre = genres.id
        ''')
        genres = [item[0] for item in result]
        con.close()

        for genre in genres:
            self.parameterSelection.addItem(genre)

        # Fill tableWidget
        headers = ['Название', 'Жанр', 'Год']

        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(headers)

        con = sqlite3.connect('films_db.sqlite')
        cur = con.cursor()

        result = cur.execute(f'''
                            select films.title, films.genre, films.year
                            from films inner join genres on films.genre = genres.id
                        ''').fetchall()
        con.close()

        self.tableWidget.setRowCount(len(result) - 1)
        self.fill_table(result)

        self.queryButton.clicked.connect(self.find)

    def find(self):

        con = sqlite3.connect('films_db.sqlite')
        cur = con.cursor()

        genre_name = self.parameterSelection.currentText()
        result = cur.execute(f'''
                    select films.title, films.genre, films.year
                    from films inner join genres on films.genre = genres.id
                    where genres.title = '{genre_name}'
                ''').fetchall()
        con.close()
        self.fill_table(result)

    def fill_table(self, data):
        for index, item in enumerate(data):
            title, genre, year = item

            self.tableWidget.setItem(index, 0, QTableWidgetItem(title))
            self.tableWidget.setItem(index, 1, QTableWidgetItem(str(genre)))
            self.tableWidget.setItem(index, 2, QTableWidgetItem(str(year)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
