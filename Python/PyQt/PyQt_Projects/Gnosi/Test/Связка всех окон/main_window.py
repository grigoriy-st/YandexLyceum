from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Основное окно")

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Добро пожаловать в основное окно!"))

        self.additional_button = QPushButton("Открыть дополнительное окно", self)
        layout.addWidget(self.additional_button)

        # Здесь вы можете подключить сигнал для открытия дополнительного окна
        self.additional_button.clicked.connect(self.open_additional_window)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def open_additional_window(self):
        from additional_window import AdditionalWindow  # Импортируем класс дополнительного окна
        self.additional_window = AdditionalWindow()
        self.additional_window.show()