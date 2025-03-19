import io
import sys
import sqlite3

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel

template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>501</width>
    <height>355</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QWidget" name="verticalLayoutWidget">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>10</y>
      <width>491</width>
      <height>241</height>
     </rect>
    </property>
    <layout class="QVBoxLayout" name="verticalLayout">
     <item>
      <layout class="QHBoxLayout" name="horizontalLayout">
       <item>
        <widget class="QComboBox" name="parameterSelection">
         <property name="maximumSize">
          <size>
           <width>100</width>
           <height>16777215</height>
          </size>
         </property>
         <item>
          <property name="text">
           <string>Год выпуска</string>
          </property>
         </item>
         <item>
          <property name="text">
           <string>Название</string>
          </property>
         </item>
         <item>
          <property name="text">
           <string>Продолжительность</string>
          </property>
         </item>
        </widget>
       </item>
       <item>
        <widget class="QLineEdit" name="queryLine">
         <property name="maximumSize">
          <size>
           <width>200</width>
           <height>16777215</height>
          </size>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QPushButton" name="queryButton">
         <property name="maximumSize">
          <size>
           <width>100</width>
           <height>16777215</height>
          </size>
         </property>
         <property name="text">
          <string>Поиск</string>
         </property>
        </widget>
       </item>
      </layout>
     </item>
     <item>
      <layout class="QHBoxLayout" name="horizontalLayout_2">
       <property name="spacing">
        <number>50</number>
       </property>
       <item>
        <widget class="QLabel" name="label">
         <property name="text">
          <string>ID:</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QLineEdit" name="idEdit">
         <property name="maximumSize">
          <size>
           <width>350</width>
           <height>16777215</height>
          </size>
         </property>
        </widget>
       </item>
      </layout>
     </item>
     <item>
      <layout class="QHBoxLayout" name="horizontalLayout_5">
       <item>
        <widget class="QLabel" name="label_4">
         <property name="text">
          <string>Название:</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QLineEdit" name="titleEdit">
         <property name="maximumSize">
          <size>
           <width>350</width>
           <height>16777215</height>
          </size>
         </property>
        </widget>
       </item>
      </layout>
     </item>
     <item>
      <layout class="QHBoxLayout" name="horizontalLayout_4">
       <item>
        <widget class="QLabel" name="label_3">
         <property name="text">
          <string>Год выпуска: </string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QLineEdit" name="yearEdit">
         <property name="maximumSize">
          <size>
           <width>350</width>
           <height>16777215</height>
          </size>
         </property>
        </widget>
       </item>
      </layout>
     </item>
     <item>
      <layout class="QHBoxLayout" name="horizontalLayout_6">
       <item>
        <widget class="QLabel" name="label_5">
         <property name="text">
          <string>Жанр:</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QLineEdit" name="genreEdit">
         <property name="maximumSize">
          <size>
           <width>350</width>
           <height>16777215</height>
          </size>
         </property>
        </widget>
       </item>
      </layout>
     </item>
     <item>
      <layout class="QHBoxLayout" name="horizontalLayout_7">
       <item>
        <widget class="QLabel" name="label_6">
         <property name="text">
          <string>Продолжительность:</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QLineEdit" name="durationEdit">
         <property name="maximumSize">
          <size>
           <width>350</width>
           <height>16777215</height>
          </size>
         </property>
        </widget>
       </item>
      </layout>
     </item>
    </layout>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>501</width>
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
