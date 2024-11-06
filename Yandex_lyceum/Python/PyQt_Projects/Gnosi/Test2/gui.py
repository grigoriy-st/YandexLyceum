# gui.py
from PyQt5 import QtWidgets, QtGui
from logic import MessageHandler  # Импортируем класс для обработки сообщений

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Пример приложения")
        self.setGeometry(100, 100, 300, 200)

        # Создаем кнопку
        self.button = QtWidgets.QPushButton("Показать сообщение", self)
        self.button.setGeometry(50, 80, 200, 40)

        # Подключаем сигнал нажатия кнопки к методу
        self.button.clicked.connect(self.show_message)

    def show_message(self):
        # Вызываем метод из логики для показа сообщения
        MessageHandler.show_message()