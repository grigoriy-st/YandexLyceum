import sys
import io
'''' Нужно изменить логику. Кнопки уже добавлены. Кнопки брать из calc.ui'''
from decimal import Decimal, InvalidOperation
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('calc.ui', self)
        self.initUI()

    def initUI(self):
        self.number_buttons = [self.btn0, self.btn1, self.btn2, self.btn3,
                               self.btn4, self.btn5, self.btn6, self.btn7,
                               self.btn8, self.btn9]

        op_buttons = [self.btn_clear, self.fact,
                      self.btn_div, self.btn_mult,
                      self.btn_minus, self.btn_plus,
                      self.btn_dot, self.pow,
                      self.sqrt, self.btn_eq]

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
