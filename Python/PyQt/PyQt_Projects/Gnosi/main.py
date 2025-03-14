import sys

# Все части программы
from Main_window_UI import Ui_MainWindow
from Auth_dialog_window import Auth_Dialog


from PyQt6 import QtWidgets
from PyQt6.QtWidgets import (
    QMainWindow
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
    auth_window.exec()

    if auth_window.auth_success:
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)

        # Заполнение информации о вошедшем пользователе
        ui.UID = auth_window.UID
        ui.LE_profile_login.setText(auth_window.lineE_login.text())
        ui.LE_profile_type.setText(auth_window.type_ac)
        ui.LE_profileID.setText(auth_window.UID)
        ui.LE_name.setText(auth_window.name)

        # блокировка функции созданию курсов для студентов
        if auth_window.type_ac != "Преподаватель":
            ui.tab_create_cource.setDisabled(True)
        MainWindow.show()
    sys.exit(app.exec())