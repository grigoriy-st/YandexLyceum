import sys
import os
# print("Текущая директория:", os.listdir())
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r'Калькулятор.ui', self)
        self.initUI()

    def initUI(self):
        self.number_buttons= [self.btn0, self.btn1, self.btn2, self.btn3, 
                         self.btn4, self.btn5, self.btn6, self.btn7, 
                         self.btn8, self.btn9]
        
        op_buttons = [self.clear_button, self.clear_entry_button, self.divide_button, self.multiply_button,
                      self.substract_button, self.add_button, self.float_point_button,
                      self.plus_minus_button, self.equals_button]
        
        for btn in self.number_buttons:
            btn.clicked.connect(self.click_btn)

        for btn in op_buttons:
            btn.clicked.connect(self.click_btn)
        self.last_is_eq = False
        self.last_is_op = False

    def click_btn(self):
        sender = self.sender()
        main_label = self.main_label.text()
        secondary_label = self.secondary_label.text()
        
        # if sender.text() in '=-*+' and not secondary_label:
        #     return None
        
        if sender.text() in '=-*+/±':
            match sender.text():
                case '=':
                    try:
                        result = eval(secondary_label + main_label)
                    except ZeroDivisionError:
                        result = 'ОШИБКА'
                    self.secondary_label.setText("")
                    self.main_label.setText(str(result))
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
                    if int(main_label) != 0:
                        self.main_label.setText(str(int(main_label) * -1))
            self.last_is_op = True

        elif sender.text().isdigit():
            if self.last_is_eq:
                self.main_label.setText("0")
                self.last_is_eq = False

            if not secondary_label:
                if main_label == '0':
                    self.main_label.setText(sender.text())
                else:
                    self.main_label.setText(main_label + sender.text())
            elif secondary_label:
                if self.last_is_op:
                    self.main_label.setText(sender.text())
                    self.last_is_op = False
                elif main_label == '0':
                    self.main_label.setText(sender.text())
                else:
                    self.main_label.setText(main_label + sender.text())

        elif sender.text() in ['C', 'CE', '.']:
            match sender.text():
                case 'C':
                    self.main_label.setText("0")
                    self.secondary_label.setText("")
                case 'CE':
                    self.main_label.setText("0")
                case '.':
                    if '.' not in self.main_label.text():
                        self.main_label.setText(self.main_label.text() + '.')

'''Добавить функционал на:
- Экспоненциальную запись
- С плавающей точкой
'''                

        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Calculator()
    ex.show()
    sys.exit(app.exec())
