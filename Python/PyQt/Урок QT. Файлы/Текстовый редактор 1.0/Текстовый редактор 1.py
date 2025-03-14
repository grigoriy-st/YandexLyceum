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
    <width>536</width>
    <height>353</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPlainTextEdit" name="text_edit">
    <property name="geometry">
     <rect>
      <x>170</x>
      <y>10</y>
      <width>351</width>
      <height>291</height>
     </rect>
    </property>
   </widget>
   <widget class="QWidget" name="verticalLayoutWidget">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>0</y>
      <width>160</width>
      <height>171</height>
     </rect>
    </property>
    <layout class="QVBoxLayout" name="verticalLayout">
     <item>
      <widget class="QLineEdit" name="filename_edit"/>
     </item>
     <item>
      <widget class="QPushButton" name="new_button">
       <property name="text">
        <string>Создать новый</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="save_button">
       <property name="text">
        <string>Сохранить файл</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="open_button">
       <property name="text">
        <string>Открыть файл</string>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>536</width>
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


class Notebook(QMainWindow):

    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.initUI()

    def initUI(self):
        self.new_button.clicked.connect(self.create_new_file)
        self.save_button.clicked.connect(self.save_file)
        self.open_button.clicked.connect(self.open_file)

    def create_new_file(self):
        self.text_edit.clear()
        self.filename_edit.setText("")

    def save_file(self):
        file_name = self.filename_edit.text()
        if file_name:
            try:
                f = open(file_name, 'w', encoding='utf-8')
                text = self.text_edit.toPlainText()
                f.write(text)
                f.close()
            except FileNotFoundError:
                ...

    def open_file(self):
        file_name = self.filename_edit.text()
        try:
            with open(file_name, 'r', encoding='utf-8') as f:
                content = f.read()
                self.text_edit.setPlainText(content)

        except FileNotFoundError:
            ...


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Notebook()
    ex.show()
    sys.exit(app.exec())
