import sys
import os
# Все части программы
from Main_window_UI import Ui_MainWindow
from logic import Logic
from Auth_window import Auth_form

from PyQt6.QtGui import QIcon
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton,
    QTabWidget, QLabel, QWidget,
    QVBoxLayout, QDialog,
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.resize(800, 500)
        self.setWindowTitle("Gnosi")



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    auth_window = Auth_form()
    if auth_window.exec() == QDialog.accepted:
        print("hello")

    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())