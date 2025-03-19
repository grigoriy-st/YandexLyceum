import sys
from PyQt5.QtWidgets import QApplication, QDialog
from auth_window import AuthWindow
from main_window import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)

    auth_window = AuthWindow()
    if auth_window.exec_() == QDialog.Accepted:  # Если авторизация успешна
        main_window = MainWindow()
        main_window.show()
        sys.exit(app.exec_())