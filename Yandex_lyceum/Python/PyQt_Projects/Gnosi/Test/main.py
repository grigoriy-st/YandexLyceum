import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QMessageBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Основное окно")
        self.setGeometry(100, 100, 300, 200)

        # Создаем кнопку для открытия всплывающего окна
        self.button = QPushButton("Открыть меню", self)
        self.button.clicked.connect(self.show_popup)

        # Устанавливаем макет
        layout = QVBoxLayout()
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def show_popup(self):
        # Создаем всплывающее окно с кнопками
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Выберите действие")
        msg_box.setText("Выберите одно из действий:")

        # Добавляем кнопки
        create_theory_button = msg_box.addButton("Создать теорию", QMessageBox.ActionRole)
        create_test_button = msg_box.addButton("Создать тест", QMessageBox.ActionRole)
        upload_file_button = msg_box.addButton("Загрузить файл", QMessageBox.ActionRole)

        # Показываем сообщение и ждем нажатия кнопки
        msg_box.exec_()

        # Проверяем, какая кнопка была нажата
        if msg_box.clickedButton() == create_theory_button:
            QMessageBox.information(self, "Информация", "Вы выбрали 'Создать теорию'")
        elif msg_box.clickedButton() == create_test_button:
            QMessageBox.information(self, "Информация", "Вы выбрали 'Создать тест'")
        elif msg_box.clickedButton() == upload_file_button:
            QMessageBox.information(self, "Информация", "Вы выбрали 'Загрузить файл'")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())