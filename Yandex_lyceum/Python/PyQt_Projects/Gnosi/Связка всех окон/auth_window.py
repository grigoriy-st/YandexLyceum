from PyQt5.QtWidgets import QDialog, QVBoxLayout, QPushButton, QLabel, QLineEdit


class AuthWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Авторизация")

        layout = QVBoxLayout()
        self.username_input = QLineEdit(self)
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)

        layout.addWidget(QLabel("Имя пользователя:"))
        layout.addWidget(self.username_input)
        layout.addWidget(QLabel("Пароль:"))
        layout.addWidget(self.password_input)

        self.login_button = QPushButton("Войти", self)
        self.login_button.clicked.connect(self.handle_login)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def handle_login(self):
        # Здесь должна быть логика проверки авторизации
        if self.username_input.text() == "user" and self.password_input.text() == "pass":
            self.accept()  # Закрывает диалог и возвращает QDialog.Accepted
        else:
            print("Неверные учетные данные")