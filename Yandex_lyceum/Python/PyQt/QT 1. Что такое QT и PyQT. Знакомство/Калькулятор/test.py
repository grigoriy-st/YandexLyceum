import os
import subprocess
import sys
import traceback
from collections import namedtuple

from PyQt6.QtWidgets import QApplication

os.environ["QT_QPA_PLATFORM"] = "offscreen"
os.environ["XDG_RUNTIME_DIR"] = '/tmp/runtime-'

f = open('Калькулятор.py')
s = f.read()
f.close()
if "import inspect" in s or "from inspect" in s:
    print("don't inspect LMS")
    sys.exit(1)

if "exit()" in s or "quit()" in s:
    print("don't use exit() or quit()")
    sys.exit(1)

result = None
try:
    result = subprocess.run(
        [sys.executable, "-c", s], capture_output=True, text=True, timeout=1
    )
except subprocess.TimeoutExpired as e:
    pass

if not (result is None):
    if result.stderr != "":
        print(result.stderr)
        sys.exit(1)

import solution as sol

app = QApplication(sys.argv)
solO = sol.Calculator()
num = 0

TestCase = namedtuple(
    "test_case", ["first_value", "operator_button", "second_value", "result"]
)
t = sys.stdin.read().strip()
exec(t)


def dial_value(value: int | str) -> None:  # заносит число в калькулятор
    """
    Dials a number step by step using every number
    as an index of number_buttons array
    """
    is_negative = False

    for element in str(value):
        if element == ".":
            solO.float_point_button.clicked.emit()
        elif element == "-":
            is_negative = True
        else:
            solO.number_buttons[int(element)].clicked.emit()

    if is_negative:
        solO.plus_minus_button.clicked.emit()


try:
    num += 1  # тест на корректное название программы
    if solO.windowTitle() != "Калькулятор":
        print(f"Test {num}: window has incorrect title")

    num += 1  # тест на наличие нуля в главном поле ввода при запуске программы
    if solO.main_label.text() != "0":
        print(f'Test {num}: main label should display "0" after launch')

    num += 1  # тест на пустоту дополнительного поля ввода при запуске программы
    if solO.secondary_label.text().strip() != "":
        print(f"Test {num}: secondary label should be empty after launch")

        num += 1  # тест на работу кнопки "CE" (см. задание)
        dial_value(123456)
        solO.add_button.clicked.emit()
        dial_value(789)
        solO.clear_entry_button.clicked.emit()
        if solO.main_label.text() != "0":
            print(f"Test {num}: clear_entry_button doesn't clear main_label")
        if solO.secondary_label.text().strip().split() != ["123456", "+"]:
            print(
                f"Test {num}: clear_entry_button clears secondary_label, that is incorrect behavior"
            )

        num += 1  # тест на работу кнопки "C" (см. задание)
        dial_value(123456)
        solO.add_button.clicked.emit()
        dial_value(789)
        solO.clear_button.clicked.emit()
        if solO.main_label.text() != "0":
            print(f"Test {num}: clear_button doesn't clear main_label")
        if solO.secondary_label.text().strip() != "":
            print(f"Test {num}: clear_button doesn't clear secondary_label")

        num += 1
        dial_value("192.168.1.0")
    if solO.main_label.text() != "192.16810":
        print(f"Test {num}: several float_point_button activations should be ignored")
    solO.clear_button.clicked.emit()

    num += 1  # тест на игнорирование кнопки "±", если введенное число равно нулю (или 0.00 и т.д.)
    dial_value("-0")
    if solO.main_label.text() != "0":
        print(
            f"Test {num}: plus_minus_button shouldn't change the sign of 0, 0.00 etc."
        )
    solO.clear_button.clicked.emit()
    dial_value("-0.00")
    if solO.main_label.text() != "0.00":
        print(
            f"Test {num}: plus_minus_button shouldn't change the sign of 0, 0.00 etc."
        )
    solO.clear_button.clicked.emit()

    num += 1  # тест на отображение ошибки при попытке деления на ноль
    dial_value(123)
    solO.divide_button.clicked.emit()
    dial_value(0)
    solO.equals_button.clicked.emit()
    if solO.main_label.text() != "ОШИБКА":
        ...
