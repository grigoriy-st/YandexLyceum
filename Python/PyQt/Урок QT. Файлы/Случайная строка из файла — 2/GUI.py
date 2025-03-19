import sys
import random

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit


class RandomString(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.button = QPushButton("Получить", self)
        self.button.setGeometry(10, 10, 60, 30)
        self.button.clicked.connect(self.get_line)

        self.text_field = QTextEdit("", self)
        self.text_field.setGeometry(80, 10, 100, 30)

    def get_line(self):
        f = open('lines.txt', mode="rt", encoding="utf-8")
        strings = f.readlines()

        if strings:
            max_length = len(strings)
            random_num = 0
            if max_length > 1:
                random_num = random.randint(0, max_length - 1)
            if strings[random_num]:
                self.text_field.setText(strings[random_num])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RandomString()
    ex.show()
    sys.exit(app.exec())



