# logic.py
from PyQt5.QtWidgets import QMessageBox

class MessageHandler:
    @staticmethod
    def show_message():
        msg = QMessageBox()
        msg.setWindowTitle("Сообщение")
        msg.setText("Кнопка была нажата!")
        msg.exec_()