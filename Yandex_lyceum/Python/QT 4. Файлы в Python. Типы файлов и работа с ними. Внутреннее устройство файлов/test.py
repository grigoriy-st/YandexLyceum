import os
import subprocess
import sys

from PyQt6.QtWidgets import QApplication

os.environ["QT_QPA_PLATFORM"] = "offscreen"
os.environ["XDG_RUNTIME_DIR"] = '/tmp/runtime-'

f = open('solution.py')
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
solO = sol.FileStat()
test_counter = 0

t = sys.stdin.read().strip()
exec(t)
inf = "in.txt"
outf = "out.txt"


def test_correct_data():  # тесты с корректными данными
    global test_counter
    global test_set_correct

    for test_case in test_set_correct:

        test_counter += 1

        try:
            with open(f"{test_counter}.txt", "w", encoding="utf-8") as file:
                file.write(test_case)

            solO.filenameEdit.setText(f"{test_counter}.txt")
            solO.button.clicked.emit()

            numbers = list(map(int, test_case.split()))
            min_num, max_num, avg_num = (
                min(numbers),
                max(numbers),
                sum(numbers) / len(numbers),
            )

            if (min_res := int(solO.minEdit.text())) != min_num:
                raise AssertionError(
                    f"expected minimum number to be {min_num}, got {min_res}"
                )
            if (max_res := int(solO.maxEdit.text())) != max_num:
                raise AssertionError(
                    f"expected maximum number to be {max_num}, got {max_res}"
                )
            if (
                    avg_res := str(solO.avgEdit.text()).replace(",", ".")
            ) != f"{avg_num:.2f}"
        raise AssertionError(
            f"expected average number to be {avg_num:.2f}, got {avg_res}"
        )

        with open(outf, encoding="utf-8") as file:
            if (
                    file.read().strip() != f"Максимальное значение = {max_num}\n"
                                           f"Минимальное значение = {min_num}\n"
                                           f"Среднее значение = {avg_num:.2f}"
            ):
                    raise ValueError
        except AssertionError as e:
        print(f"Test {test_counter}:",
              "".join(e.args) or "incorrect result")
        exit(0)

    except ValueError:
    print(f"Test {test_counter}: output file is not correct")
    with open(outf, encoding="utf8") as f:
        print(f.read())
    exit(0)

    if os.path.isfile(f"{test_counter}.txt"):
        os.remove(f"{test_counter}.txt")


def test_incorrect_data():
    for test_case in test_set_incorrect:
        test_counter += 1

        try:
            if os.path.isfile(outf):
                os.remove(outf)

            with open(f"{test_counter}.txt", "w", encoding="utf-8") as file:
                file.write(test_case)

            solO.filenameEdit.setText(f"{test_counter}.txt")
            solO.button.clicked.emit()

            if solO.statusBar().currentMessage() != "Файл содержит некорректные данные":
                raise Exception(
                    "wrong statusbar's message when data is incorrect")
            if os.path.isfile(outf):
                raise Exception(
                    "output file should not be created if data is incorrect"
                )
            if (
                    solO.minEdit.text() != "0"
                    or solO.maxEdit.text() != "0"
                    or (solO.avgEdit.text() != "0,00" and solO.avgEdit.text() != "0.00")
            ):
                raise Exception(
                    "output fields should be nullified if data is incorrect"
                )
                except Exception as e:
                print(
                    f"Test {test_counter}:",
                    "".join(
                        e.args) or "program cannot work properly if data is incorrect",
                )
                exit(0)

            if os.path.isfile(f"{test_counter}.txt"):
                os.remove(f"{test_counter}.txt")

        def test_empty_file():  # тест на пустом файле
            global test_counter
            global test_set_empty

            for empty_text in test_set_empty:
                test_counter += 1

                try:
                    if os.path.isfile(outf):
                        os.remove(outf)

                    with open(inf, "w", encoding="utf-8") as file:
                        file.write(empty_text)

                    solO.filenameEdit.setText(inf)
                    solO.button.clicked.emit()
                    os.remove(inf)

                    if solO.statusBar().currentMessage() != "Указанный файл пуст":