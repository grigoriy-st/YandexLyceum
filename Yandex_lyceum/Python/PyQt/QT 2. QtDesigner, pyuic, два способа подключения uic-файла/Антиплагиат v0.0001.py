import io
import sys

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
    <width>611</width>
    <height>608</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Антиплагиат v0.0001</string>
  </property>
  <property name="statusTip">
   <string/>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QWidget" name="verticalLayoutWidget">
    <property name="geometry">
     <rect>
      <x>9</x>
      <y>10</y>
      <width>591</width>
      <height>531</height>
     </rect>
    </property>
    <layout class="QVBoxLayout" name="verticalLayout">
     <item>
      <layout class="QHBoxLayout" name="horizontalLayout">
       <item>
        <widget class="QLabel" name="label">
         <property name="font">
          <font>
           <pointsize>12</pointsize>
          </font>
         </property>
         <property name="text">
          <string>Порог срабатывания (%)</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QDoubleSpinBox" name="alert_value">
         <property name="sizePolicy">
          <sizepolicy hsizetype="MinimumExpanding" vsizetype="Fixed">
           <horstretch>0</horstretch>
           <verstretch>0</verstretch>
          </sizepolicy>
         </property>
         <property name="font">
          <font>
           <pointsize>10</pointsize>
          </font>
         </property>
        </widget>
       </item>
      </layout>
     </item>
     <item>
      <layout class="QHBoxLayout" name="horizontalLayout_2">
       <item>
        <widget class="QLabel" name="label_1">
         <property name="font">
          <font>
           <pointsize>12</pointsize>
          </font>
         </property>
         <property name="text">
          <string>Текст 1</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QLabel" name="label_2">
         <property name="font">
          <font>
           <pointsize>12</pointsize>
          </font>
         </property>
         <property name="text">
          <string>Текст 2</string>
         </property>
        </widget>
       </item>
      </layout>
     </item>
     <item>
      <layout class="QHBoxLayout" name="horizontalLayout_3">
       <item>
        <widget class="QPlainTextEdit" name="text1"/>
       </item>
       <item>
        <widget class="QPlainTextEdit" name="text2"/>
       </item>
      </layout>
     </item>
     <item>
      <widget class="QPushButton" name="checkBtn">
       <property name="text">
        <string>Сравнить</string>
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
     <width>611</width>
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


class AntiPlagiarism(QMainWindow):
    def __init__(self):
        super().__init__()

        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.initUI()

    def initUI(self):
        self.statusbar = self.statusBar()
        self.checkBtn.clicked.connect(self.compare_text)
        self.alert_value.setValue(50)

    def compare_text(self):
        text1 = self.text1.toPlainText().strip().splitlines()
        text2 = self.text2.toPlainText().strip().splitlines()

        inter = len(set(text1) & set(text2))
        union = len(set(text1) | set(text2))

        if len(text1) == 0:
            inter = 1
        if len(text2) == 0:
            union = 1
        percent = round(100 * inter / union, 2)

        if percent >= self.alert_value.value():
            self.statusbar.showMessage(f'Тексты похожи на {percent:.2f}%, плагиат')
        else:
            self.statusbar.showMessage(f'Тексты похожи на {percent:.2f}%, не плагиат')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AntiPlagiarism()
    ex.show()
    sys.exit(app.exec())
