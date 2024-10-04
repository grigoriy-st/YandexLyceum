import sys, io

from PyQt6 import uic  # Импортируем uic
from PyQt6.QtWidgets import QApplication, QMainWindow

template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QWidget" name="horizontalLayoutWidget">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>0</y>
      <width>791</width>
      <height>551</height>
     </rect>
    </property>
    <layout class="QHBoxLayout" name="horizontalLayout">
     <item>
      <layout class="QVBoxLayout" name="verticalLayout_2">
       <item>
        <widget class="QTimeEdit" name="timeEdit"/>
       </item>
       <item>
        <widget class="QCalendarWidget" name="calendarWidget"/>
       </item>
       <item>
        <widget class="QLineEdit" name="lineEdit"/>
       </item>
       <item>
        <widget class="QPushButton" name="addEventBtn">
         <property name="text">
          <string>Добавить событие</string>
         </property>
        </widget>
       </item>
      </layout>
     </item>
     <item>
      <widget class="QListWidget" name="eventList"/>
     </item>
    </layout>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>800</width>
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

class SimplePlanner(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.initUI()

    def initUI(self):
        self.addEventBtn.clicked.connect(self.add_event)
        self.events = {}

    def add_event(self):
        # Time
        time = self.timeEdit.time()
        hour = time.hour()
        minute = time.minute()
        second = time.second()
        # Date
        date = self.calendarWidget.selectedDate()
        # Text
        task = self.lineEdit.text()
        self.lineEdit.setText("")
        if date in self.events:
            self.events[date].append(f'{hour:02d}:\
            {minute:02d}:{second:02d} - {task}')
        else:
            self.events[date] = [f'{hour:02d}:{minute:02d}:{second:02d}\
 - {task}']
        sorted_events = sorted(self.events.keys(),
                               key=lambda x: x.toJulianDay(), reverse=True)

        self.eventList.clear()
        for date in sorted_events:
            date_string = date.toString("yyyy-MM-dd")
            self.eventList.addItem(f'{date_string} \
{','.join([i for i in self.events[date]])}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SimplePlanner()
    ex.show()
    sys.exit(app.exec())
