import sys
import io

from decimal import Decimal, InvalidOperation
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
    <width>331</width>
    <height>461</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Калькулятор</string>
  </property>
  <property name="statusTip">
   <string/>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QWidget" name="verticalLayoutWidget">
    <property name="geometry">
     <rect>
      <x>5</x>
      <y>0</y>
      <width>322</width>
      <height>431</height>
     </rect>
    </property>
    <layout class="QVBoxLayout" name="verticalLayout">
     <item>
      <widget class="QLabel" name="secondary_label">
       <property name="maximumSize">
        <size>
         <width>16777215</width>
         <height>30</height>
        </size>
       </property>
       <property name="font">
        <font>
         <family>Arial</family>
         <pointsize>13</pointsize>
        </font>
       </property>
       <property name="text">
        <string/>
       </property>
       <property name="alignment">
        <set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QLabel" name="main_label">
       <property name="font">
        <font>
         <family>Arial</family>
         <pointsize>31</pointsize>
         <weight>50</weight>
         <bold>false</bold>
         <strikeout>false</strikeout>
         <kerning>true</kerning>
        </font>
       </property>
       <property name="layoutDirection">
        <enum>Qt::LeftToRight</enum>
       </property>
       <property name="text">
        <string>0</string>
       </property>
       <property name="alignment">
        <set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set>
       </property>
      </widget>
     </item>
     <item>
      <layout class="QHBoxLayout" name="horizontalLayout_2">
       <item>
        <widget class="QPushButton" name="btn7">
         <property name="sizePolicy">
          <sizepolicy hsizetype="Maximum" vsizetype="Minimum">
           <horstretch>0</horstretch>
           <verstretch>0</verstretch>
          </sizepolicy>
         </property>
         <property name="font">
          <font>
           <family>Arial</family>
           <pointsize>19</pointsize>
          </font>
         </property>
         <property name="text">
          <string>7</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QPushButton" name="btn8">
         <property name="sizePolicy">
          <sizepolicy hsizetype="Minimum" vsizetype="Minimum">
           <horstretch>0</horstretch>
           <verstretch>0</verstretch>
          </sizepolicy>
         </property>
         <property name="font">
          <font>
           <family>Arial</family>
           <pointsize>19</pointsize>
          </font>
         </property>
         <property name="text">
          <string>8</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QPushButton" name="btn9">
         <property name="sizePolicy">
          <sizepolicy hsizetype="Minimum" vsizetype="Minimum">
           <horstretch>0</horstretch>
           <verstretch>0</verstretch>
          </sizepolicy>
         </property>
         <property name="font">
          <font>
           <family>Arial</family>
           <pointsize>19</pointsize>
          </font>
         </property>
         <property name="text">
          <string>9</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QPushButton" name="divide_button">
         <property name="sizePolicy">
          <sizepolicy hsizetype="Minimum" vsizetype="Minimum">
           <horstretch>0</horstretch>
           <verstretch>0</verstretch>
          </sizepolicy>
         </property>
         <property name="font">
          <font>
           <family>Arial</family>
           <pointsize>19</pointsize>
          </font>
         </property>
         <property name="text">
          <string>/</string>
         </property>
        </widget>
       </item>
      </layout>
     </item>
     <item>
      <layout class="QHBoxLayout" name="horizontalLayout_5">
       <item>
        <widget class="QPushButton" name="btn4">
         <property name="sizePolicy">
          <sizepolicy hsizetype="Maximum" vsizetype="Minimum">
           <horstretch>0</horstretch>
           <verstretch>0</verstretch>
          </sizepolicy>
         </property>
         <property name="font">
          <font>
           <family>Arial</family>
           <pointsize>19</pointsize>
          </font>
         </property>
         <property name="text">
          <string>4</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QPushButton" name="btn5">
         <property name="sizePolicy">
          <sizepolicy hsizetype="Minimum" vsizetype="Minimum">
           <horstretch>0</horstretch>
           <verstretch>0</verstretch>
          </sizepolicy>
         </property>
         <property name="font">
          <font>
           <family>Arial</family>
           <pointsize>19</pointsize>
          </font>
         </property>
         <property name="text">
          <string>5</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QPushButton" name="btn6">
         <property name="sizePolicy">
          <sizepolicy hsizetype="Minimum" vsizetype="Minimum">
           <horstretch>0</horstretch>
           <verstretch>0</verstretch>
          </sizepolicy>
         </property>
         <property name="font">
          <font>
           <family>Arial</family>
           <pointsize>19</pointsize>
          </font>
         </property>
         <property name="text">
          <string>6</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QPushButton" name="multiply_button">
         <property name="sizePolicy">
          <sizepolicy hsizetype="Minimum" vsizetype="Minimum">
           <horstretch>0</horstretch>
           <verstretch>0</verstretch>
          </sizepolicy>
         </property>
         <property name="font">
          <font>
           <family>Arial</family>
           <pointsize>19</pointsize>
          </font>
         </property>
         <property name="text">
          <string>*</string>
         </property>
        </widget>
       </item>
      </layout>
     </item>
     <item>
      <layout class="QHBoxLayout" name="horizontalLayout">
       <item>
        <widget class="QPushButton" name="btn1">
         <property name="sizePolicy">
          <sizepolicy hsizetype="Maximum" vsizetype="Minimum">
           <horstretch>0</horstretch>
           <verstretch>0</verstretch>
          </sizepolicy>
         </property>
         <property name="font">
          <font>
           <family>Arial</family>
           <pointsize>19</pointsize>
          </font>
         </property>
         <property name="text">
          <string>1</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QPushButton" name="btn2">
         <property name="sizePolicy">
          <sizepolicy hsizetype="Minimum" vsizetype="Minimum">
           <horstretch>0</horstretch>
           <verstretch>0</verstretch>
          </sizepolicy>
         </property>
         <property name="font">
          <font>
           <family>Arial</family>
           <pointsize>19</pointsize>
          </font>
         </property>
         <property name="text">
          <string>2</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QPushButton" name="btn3">
         <property name="sizePolicy">
          <sizepolicy hsizetype="Minimum" vsizetype="Minimum">
           <horstretch>0</horstretch>
           <verstretch>0</verstretch>
          </sizepolicy>
         </property>
         <property name="font">
          <font>
           <family>Arial</family>
           <pointsize>19</pointsize>
          </font>
         </property>
         <property name="text">
          <string>3</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QPushButton" name="substract_button">
         <property name="sizePolicy">
          <sizepolicy hsizetype="Minimum" vsizetype="Minimum">
           <horstretch>0</horstretch>
           <verstretch>0</verstretch>
          </sizepolicy>
         </property>
         <property name="font">
          <font>
           <family>Arial</family>
           <pointsize>19</pointsize>
          </font>
         </property>
         <property name="text">
          <string>-</string>
         </property>
        </widget>
       </item>
      </layout>
     </item>
     <item>
      <layout class="QHBoxLayout" name="horizontalLayout_3">
       <item>
        <widget class="QPushButton" name="clear_button">
         <property name="sizePolicy">
          <sizepolicy hsizetype="Maximum" vsizetype="Minimum">
           <horstretch>0</horstretch>
           <verstretch>0</verstretch>
          </sizepolicy>
         </property>
         <property name="font">
          <font>
           <family>Arial</family>
           <pointsize>19</pointsize>
          </font>
         </property>
         <property name="text">
          <string>C</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QPushButton" name="btn0">
         <property name="sizePolicy">
          <sizepolicy hsizetype="Minimum" vsizetype="Minimum">
           <horstretch>0</horstretch>
           <verstretch>0</verstretch>
          </sizepolicy>
         </property>
         <property name="font">
          <font>
           <family>Arial</family>
           <pointsize>19</pointsize>
          </font>
         </property>
         <property name="text">
          <string>0</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QPushButton" name="clear_entry_button">
         <property name="sizePolicy">
          <sizepolicy hsizetype="Minimum" vsizetype="Minimum">
           <horstretch>0</horstretch>
           <verstretch>0</verstretch>
          </sizepolicy>
         </property>
         <property name="font">
          <font>
           <family>Arial</family>
           <pointsize>19</pointsize>
          </font>
         </property>
         <property name="text">
          <string>CE</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QPushButton" name="add_button">
         <property name="sizePolicy">
          <sizepolicy hsizetype="Minimum" vsizetype="Minimum">
           <horstretch>0</horstretch>
           <verstretch>0</verstretch>
          </sizepolicy>
         </property>
         <property name="font">
          <font>
           <family>Arial</family>
           <pointsize>19</pointsize>
          </font>
         </property>
         <property name="text">
          <string>+</string>
         </property>
        </widget>
       </item>
      </layout>
     </item>
     <item>
      <layout class="QHBoxLayout" name="horizontalLayout_6">
       <item>
        <widget class="QPushButton" name="float_point_button">
         <property name="sizePolicy">
          <sizepolicy hsizetype="Maximum" vsizetype="Minimum">
           <horstretch>0</horstretch>
           <verstretch>0</verstretch>
          </sizepolicy>
         </property>
         <property name="font">
          <font>
           <family>Arial</family>
           <pointsize>19</pointsize>
          </font>
         </property>
         <property name="text">
          <string>.</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QPushButton" name="plus_minus_button">
         <property name="sizePolicy">
          <sizepolicy hsizetype="Fixed" vsizetype="Minimum">
           <horstretch>0</horstretch>
           <verstretch>0</verstretch>
          </sizepolicy>
         </property>
         <property name="font">
          <font>
           <family>Arial</family>
           <pointsize>19</pointsize>
          </font>
         </property>
         <property name="text">
          <string>±</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QPushButton" name="equals_button">
         <property name="sizePolicy">
          <sizepolicy hsizetype="Minimum" vsizetype="Minimum">
           <horstretch>0</horstretch>
           <verstretch>0</verstretch>
          </sizepolicy>
         </property>
         <property name="font">
          <font>
           <family>Arial</family>
           <pointsize>19</pointsize>
          </font>
         </property>
         <property name="text">
          <string>=</string>
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
     <width>331</width>
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


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.initUI()

    def initUI(self):
        self.number_buttons = [self.btn0, self.btn1, self.btn2, self.btn3,
                               self.btn4, self.btn5, self.btn6, self.btn7,
                               self.btn8, self.btn9]

        op_buttons = [self.clear_button, self.clear_entry_button,
                      self.divide_button, self.multiply_button,
                      self.substract_button, self.add_button,
                      self.float_point_button, self.plus_minus_button,
                      self.equals_button]

        for btn in self.number_buttons:
            btn.clicked.connect(self.click_btn)

        for btn in op_buttons:
            btn.clicked.connect(self.click_btn)
        self.last_is_eq = False
        self.last_is_op = False

        op_buttons[6].clicked.connect(self.checking_for_an_extra_point)

    def click_btn(self):
        sender = self.sender()
        main_label = self.main_label.text()
        secondary_label = self.secondary_label.text()

        if sender.text() in '=-*+/±':
            if self.last_is_op and sender.text() == '-':
                self.main_label.setText("-")
                self.last_is_op = False
                return

            match sender.text():
                case '=':
                    try:
                        # Преобразуем числа в Decimal перед выполнением операции
                        result = eval(f"{secondary_label.strip()} {main_label}")
                        # print('With equality:', secondary_label.strip(), main_label)

                    except ZeroDivisionError:
                        result = 'ОШИБКА'
                    except InvalidOperation:
                        result = 'ОШИБКА'

                    self.secondary_label.setText("")
                    if len(str(result).replace('.', '')) > 11:
                        temp_num = self.conversion_to_exponential_form(result)
                        temp_num = self.clear_extra_zeros(temp_num)
                        self.main_label.setText(temp_num)
                    else:
                        result = self.clear_extra_zeros(str(result))
                        self.main_label.setText(result)

                    self.last_is_eq = True

                case '/':
                    self.secondary_label.setText(main_label + ' /')

                case '*':
                    self.secondary_label.setText(main_label + ' *')

                case '-':
                    self.secondary_label.setText(main_label + ' -')

                case '+':
                    self.secondary_label.setText(main_label + ' +')

                case '±':
                    if main_label.replace('.', '').replace('0', ''):
                        self.main_label.setText(str(int(main_label) * -1))

            self.last_is_op = True

        elif sender.text().isdigit():
            if self.last_is_eq:
                self.main_label.setText(sender.text())
                self.last_is_eq = False

            elif not secondary_label:
                if main_label == '0':
                    self.main_label.setText(sender.text())
                else:
                    temp_num = main_label + sender.text()
                    if len(temp_num) > 11:
                        temp_num = self.conversion_to_exponential_form(temp_num)
                        self.main_label.setText(temp_num)
                    else:
                        self.main_label.setText(temp_num)

            elif secondary_label:
                if self.last_is_op:
                    self.main_label.setText(sender.text())
                    self.last_is_op = False
                elif main_label == '0':
                    self.main_label.setText(sender.text())
                else:
                    temp_num = main_label + sender.text()
                    if len(temp_num) > 11:
                        temp_num = self.clear_extra_zeros(temp_num)
                        temp_num = self.conversion_to_exponential_form(temp_num)
                        self.main_label.setText(temp_num)
                    else:
                        result = self.clear_extra_zeros(main_label + sender.text())
                        self.main_label.setText(result)

        elif sender.text() in ['C', 'CE']:
            match sender.text():
                case 'C':
                    self.main_label.setText("0")
                    self.secondary_label.setText("")
                case 'CE':
                    self.main_label.setText("0")

    def clear_extra_zeros(self, num):
        """ Удаляет лишние нули. """
        if '.' in num and int(float(num)) != 0:
            num = num.rstrip('0')
            num = num.rstrip('.')

        return num

    def conversion_to_exponential_form(self, num):
        """ Преобразует число к экспоненциальному виду. """

        temp_num = Decimal(num)
        temp_num = "{0:.2e}".format(temp_num)
        # print('In conversation:', num, temp_num)

        temp_num = temp_num.replace("+", "")

        return temp_num

    def checking_for_an_extra_point(self):
        """ Проверка на лишнее добавление точки. """
        if '.' not in self.main_label.text():
            self.main_label.setText(self.main_label.text() + '.')
        else:
            return  # игнорирование нажатие кнопки float_point_button


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Calculator()
    ex.show()
    sys.exit(app.exec())
