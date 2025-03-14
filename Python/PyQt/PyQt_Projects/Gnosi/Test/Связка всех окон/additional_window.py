from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel


class AdditionalWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Дополнительное окно")

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Это дополнительное окно."))
        self.setLayout(layout)