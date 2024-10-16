import sys
import io

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow

template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>348</width>
    <height>332</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="button">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>10</y>
      <width>121</width>
      <height>25</height>
     </rect>
    </property>
    <property name="text">
     <string>Загрузить строки</string>
    </property>
   </widget>
   <widget class="QTextBrowser" name="text_field">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>40</y>
      <width>341</width>
      <height>231</height>
     </rect>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>348</width>
     <height>22</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class Suffle(QMainWindow):

    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.initUI()

    def initUI(self):
        self.button.clicked.connect(self.add_data)

    def add_data(self):
        try:
            f = open('lines.txt', 'r', encoding='utf-8')
            data = f.readlines()

            for string in range(1, len(data), 2):
                self.text_field.insertPlainText(data[string])
            for string in range(0, len(data), 2):
                self.text_field.insertPlainText(data[string])

            f.close()
        except FileNotFoundError:
            ...


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Suffle()
    ex.show()
    sys.exit(app.exec())
