import sys
import random
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
from PyQt6.QtCore import Qt, QPoint


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Убегающая кнопка")
        self.setGeometry(200, 200, 800, 600)
        self.button = QPushButton("Нажми на меня", self)
        self.button.setGeometry(100, 100, 100, 50)
        self.button.setMouseTracking(True)
        self.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        button_pos = self.button.geometry()
        if button_pos.contains(event.pos()):
            self.move_button()

    def move_button(self):
        w_width = self.width()
        w_height = self.height()
        button_width = self.button.width()
        button_height = self.button.height()

        new_x = random.randint(0, w_width - button_width)
        new_y = random.randint(0, w_height - button_height)

        self.button.move(new_x, new_y)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())