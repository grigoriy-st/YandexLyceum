import sys
import os

from uaclient.api.u.pro.services.disable.v1 import disable

# Все части программы
from Main_window_UI import Ui_MainWindow
# from logic import Logic
from Auth_dialog_window import Auth_Dialog
from Reg_dialog_window import Reg_Dialog

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
        self.setupUI()

    def setupUI(self):
        ...



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    auth_window = Auth_Dialog()
    if auth_window.exec() == QDialog.accepted:
        print("hello")

    if auth_window.auth_success:
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        ui.LE_profile_name.setText(auth_window.lineE_login.text())
        ui.LE_profile_type.setText(auth_window.type_ac)
        if auth_window.type_ac != "Преподаватель":
            ui.tab_create_cource.setDisabled(True)
        MainWindow.show()

    sys.exit(app.exec())