import sys
import os

from uaclient.api.u.pro.services.disable.v1 import disable

# Все части программы
from Main_window_UI import Ui_MainWindow

from Auth_dialog_window import Auth_Dialog


from PyQt6 import QtWidgets
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton,
    QTabWidget, QLabel, QWidget,
    QVBoxLayout, QDialog,
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main_window = Ui_MainWindow()
        self.resize(800, 500)
        self.setWindowTitle("Gnosi")
        self.setupUI()

    def setupUI(self):
        ...
    def run(self):
        ...


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.run()
    auth_window = Auth_Dialog()

    if auth_window.exec() == 1:
        print("hello")

    if auth_window.auth_success:
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        print("---------", auth_window.UID)
        ui.UID = auth_window.UID
        ui.LE_profile_login.setText(auth_window.lineE_login.text())
        ui.LE_profile_type.setText(auth_window.type_ac)
        ui.LE_profileID.setText(auth_window.UID)
        if auth_window.type_ac != "Преподаватель":
            ui.tab_create_cource.setDisabled(True)
        MainWindow.show()
    sys.exit(app.exec())