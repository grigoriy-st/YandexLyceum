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
    <width>340</width>
    <height>408</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Записная книжка</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QWidget" name="verticalLayoutWidget_2">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>0</y>
      <width>319</width>
      <height>361</height>
     </rect>
    </property>
    <layout class="QVBoxLayout" name="verticalLayout_4">
     <item>
      <layout class="QHBoxLayout" name="horizontalLayout_3">
       <item>
        <layout class="QVBoxLayout" name="verticalLayout_3">
         <item>
          <layout class="QHBoxLayout" name="horizontalLayout">
           <item>
            <spacer name="horizontalSpacer">
             <property name="orientation">
              <enum>Qt::Horizontal</enum>
             </property>
             <property name="sizeType">
              <enum>QSizePolicy::Maximum</enum>
             </property>
             <property name="sizeHint" stdset="0">
              <size>
               <width>62</width>
               <height>20</height>
              </size>
             </property>
            </spacer>
           </item>
           <item>
            <widget class="QLabel" name="label_1">
             <property name="font">
              <font>
               <pointsize>11</pointsize>
              </font>
             </property>
             <property name="text">
              <string>Имя</string>
             </property>
            </widget>
           </item>
           <item>
            <widget class="QLineEdit" name="contactName">
             <property name="minimumSize">
              <size>
               <width>0</width>
               <height>0</height>
              </size>
             </property>
            </widget>
           </item>
          </layout>
         </item>
         <item>
          <layout class="QHBoxLayout" name="horizontalLayout_2">
           <item>
            <spacer name="horizontalSpacer_2">
             <property name="orientation">
              <enum>Qt::Horizontal</enum>
             </property>
             <property name="sizeType">
              <enum>QSizePolicy::Maximum</enum>
             </property>
             <property name="sizeHint" stdset="0">
              <size>
               <width>30</width>
               <height>20</height>
              </size>
             </property>
            </spacer>
           </item>
           <item>
            <widget class="QLabel" name="label_2">
             <property name="font">
              <font>
               <pointsize>11</pointsize>
              </font>
             </property>
             <property name="text">
              <string>Телефон</string>
             </property>
            </widget>
           </item>
           <item>
            <widget class="QLineEdit" name="contactNumber"/>
           </item>
          </layout>
         </item>
        </layout>
       </item>
       <item>
        <widget class="QPushButton" name="addContactBtn">
         <property name="sizePolicy">
          <sizepolicy hsizetype="Preferred" vsizetype="Minimum">
           <horstretch>0</horstretch>
           <verstretch>0</verstretch>
          </sizepolicy>
         </property>
         <property name="maximumSize">
          <size>
           <width>16777215</width>
           <height>40</height>
          </size>
         </property>
         <property name="text">
          <string>Добавить</string>
         </property>
        </widget>
       </item>
      </layout>
     </item>
     <item>
      <widget class="QListWidget" name="contactList"/>
     </item>
    </layout>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>340</width>
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


class MyNotes(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.initUI()

    def initUI(self):
        self.addContactBtn.clicked.connect(self.add_contact)

    def add_contact(self):
        if self.contactName.text() and self.contactNumber.text():
            contact = f'{self.contactName.text()} {self.contactNumber.text()}'
            self.contactList.addItem(contact)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyNotes()
    ex.show()
    sys.exit(app.exec())
