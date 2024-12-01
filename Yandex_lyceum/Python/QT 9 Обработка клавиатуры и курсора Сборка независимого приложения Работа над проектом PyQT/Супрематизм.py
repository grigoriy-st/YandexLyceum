import sys
from random import randint

from PyQt6.QtWidgets import QMainWindow, QApplication

class Main_Window(QMainWindow):
    def __init__(self):
        self.resize(1000, 1000)
        self.setupUI()

    def setupUI(self):
        ...

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Main_Window()
    ui.show()
    sys.exit(app.exec())