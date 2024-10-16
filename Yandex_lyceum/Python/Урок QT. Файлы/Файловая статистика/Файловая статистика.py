import sys
import os
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
    <width>398</width>
    <height>276</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <property name="statusTip">
   <string/>
  </property>
  <widget class="QWidget" name="centralwidget">
   <property name="statusTip">
    <string/>
   </property>
   <widget class="QWidget" name="verticalLayoutWidget_3">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>10</y>
      <width>361</width>
      <height>201</height>
     </rect>
    </property>
    <layout class="QVBoxLayout" name="verticalLayout_4">
     <item>
      <layout class="QHBoxLayout" name="horizontalLayout">
       <property name="spacing">
        <number>7</number>
       </property>
       <property name="sizeConstraint">
        <enum>QLayout::SetDefaultConstraint</enum>
       </property>
       <item>
        <widget class="QLabel" name="filename_lbl">
         <property name="text">
          <string>Имя файла:</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QLineEdit" name="filenameEdit"/>
       </item>
       <item>
        <widget class="QPushButton" name="button">
         <property name="text">
          <string>Расчитать</string>
         </property>
        </widget>
       </item>
      </layout>
     </item>
     <item>
      <spacer name="verticalSpacer">
       <property name="orientation">
        <enum>Qt::Vertical</enum>
       </property>
       <property name="sizeType">
        <enum>QSizePolicy::Maximum</enum>
       </property>
       <property name="sizeHint" stdset="0">
        <size>
         <width>20</width>
         <height>0</height>
        </size>
       </property>
      </spacer>
     </item>
     <item>
      <layout class="QHBoxLayout" name="horizontalLayout_5">
       <property name="sizeConstraint">
        <enum>QLayout::SetMaximumSize</enum>
       </property>
       <item>
        <layout class="QVBoxLayout" name="verticalLayout_2">
         <item>
          <widget class="QLabel" name="max_lbl">
           <property name="text">
            <string>Максимальное значение:</string>
           </property>
           <property name="alignment">
            <set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set>
           </property>
          </widget>
         </item>
         <item>
          <widget class="QLabel" name="min_lbl">
           <property name="text">
            <string>Минимальное значение:</string>
           </property>
           <property name="alignment">
            <set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set>
           </property>
          </widget>
         </item>
         <item>
          <widget class="QLabel" name="avg_lbl">
           <property name="text">
            <string>Среднее значение:</string>
           </property>
           <property name="alignment">
            <set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set>
           </property>
          </widget>
         </item>
        </layout>
       </item>
       <item>
        <layout class="QVBoxLayout" name="verticalLayout_3">
         <item>
          <widget class="QLineEdit" name="maxEdit"/>
         </item>
         <item>
          <widget class="QLineEdit" name="minEdit"/>
         </item>
         <item>
          <widget class="QLineEdit" name="avgEdit"/>
         </item>
        </layout>
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
     <width>398</width>
     <height>18</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class FileStat(QMainWindow):

    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.initUI()

    def initUI(self):
        self.statusbar = self.statusBar()
        self.button.clicked.connect(self.calculate)

    def calculate(self):
        file_name = self.filenameEdit.text()
        result_list = []

        if os.path.isfile('./' + file_name):
            file = open(file_name, "r", encoding="utf-8")
            file_strings = file.readlines()

            if file_strings:
                for line in file_strings:
                    result_list.extend(line.split())

                result_list = list(map(int, result_list))
                self.minEdit.setText(str(min(result_list)))
                self.maxEdit.setText(str(max(result_list)))

                avg_num = float(sum(result_list)) / len(result_list)
                avg_num = round(avg_num, 2)
                avg_num = avg_num.replace('.', ',')
                self.avgEdit.setText(avg_num)
                self.statusbar.showMessage("")

            # write out file
                out = open("out.txt", 'w', encoding="utf-8")

                out.write(f'Максимальное значение = {self.maxEdit.text()}\n')
                out.write(f'Минимальное значение = {self.minEdit.text()}\n')
                out.write(f'Среднее значение = {self.avgEdit.text()}')

                out.close()
            else:
                self.minEdit.setText('0')
                self.maxEdit.setText('0')
                self.avgEdit.setText('0,00')
                self.statusbar.showMessage("Указанный файл пуст")

        else:
            self.minEdit.setText('0')
            self.maxEdit.setText('0')
            self.avgEdit.setText('0,00')
            self.statusbar.showMessage("Указанный файл не существует")

        file.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FileStat()
    ex.show()
    sys.exit(app.exec())
