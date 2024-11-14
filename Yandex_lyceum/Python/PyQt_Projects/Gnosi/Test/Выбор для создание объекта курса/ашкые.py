import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QFileDialog, QVBoxLayout


class FileDialogExample(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Выбор файла")

        # Создаем кнопку
        self.button = QPushButton("Выбрать файл", self)
        self.button.clicked.connect(self.open_file_dialog)

        # Устанавливаем вертикальный layout
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        self.setLayout(layout)

    def open_file_dialog(self):
        # Открываем диалог выбора файла
        file_name, _ = QFileDialog.getOpenFileName(self, "Выберите файл", "", "Все файлы (*)")
        if file_name:
            QMessageBox.information(self, "Информация", f"Вы выбрали файл: {file_name}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileDialogExample()
    window.show()
    sys.exit(app.exec())