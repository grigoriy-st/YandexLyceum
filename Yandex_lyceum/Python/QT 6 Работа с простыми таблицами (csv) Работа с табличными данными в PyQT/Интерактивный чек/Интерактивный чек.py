import io
import sys
import csv

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
    <width>733</width>
    <height>446</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QTableWidget" name="tableWidget">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>10</y>
      <width>701</width>
      <height>361</height>
     </rect>
    </property>
   </widget>
   <widget class="QLineEdit" name="lineEdit">
    <property name="geometry">
     <rect>
      <x>576</x>
      <y>378</y>
      <width>113</width>
      <height>20</height>
     </rect>
    </property>
   </widget>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>530</x>
      <y>380</y>
      <width>41</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>Итого:</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>733</width>
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

class InteractiveReceipt(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)

        with open('price.csv', 'r') as file:
            self.data = csv.reader(file, delimiter=';')

        self.initUI()

    def initUI(self):
        ...

    def add_contact(self):
        ...


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = InteractiveReceipt()
    ex.show()
    sys.exit(app.exec())