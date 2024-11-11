from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QPushButton, QComboBox


class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login Dialog")

        self.layout = QVBoxLayout()

        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("Enter your username")
        self.layout.addWidget(self.username_input)

        self.account_type_combo = QComboBox(self)
        self.account_type_combo.addItems(["User ", "Admin", "Guest"])
        self.layout.addWidget(self.account_type_combo)

        self.accept_button = QPushButton("Accept", self)
        self.accept_button.clicked.connect(self.accept)
        self.layout.addWidget(self.accept_button)

        self.setLayout(self.layout)

    def get_login_data(self):
        return self.username_input.text(), self.account_type_combo.currentText()