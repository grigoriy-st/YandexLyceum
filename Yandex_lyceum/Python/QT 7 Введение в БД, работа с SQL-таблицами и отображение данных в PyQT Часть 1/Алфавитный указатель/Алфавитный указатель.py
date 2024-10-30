import sys

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QTableWidget, QTableWidgetItem
)

class MyWidget(QMainWindow):
    def __init(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 200, 500, 300)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())