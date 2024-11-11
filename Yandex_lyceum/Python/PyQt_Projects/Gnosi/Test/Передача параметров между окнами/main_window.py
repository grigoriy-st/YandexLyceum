import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QDialog
from login_dialog import LoginDialog  # Импортируем LoginDialog из другого файла

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")
        self.setGeometry(100, 100, 300, 200)

        self.label = QLabel("No user logged in", self)
        self.label.setGeometry(50, 50, 200, 50)

        self.login_button = QPushButton("Login", self)
        self.login_button.setGeometry(50, 120, 200, 40)
        self.login_button.clicked.connect(self.open_login_dialog)

    def open_login_dialog(self):
        dialog = LoginDialog()
        if dialog.exec_() == QDialog.Accepted:
            username, account_type = dialog.get_login_data()
            self.label.setText(f"Logged in as: {username} ({account_type})")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())