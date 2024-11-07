import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLabel

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Создаем QGridLayout
        grid_layout = QGridLayout()

        # Создаем элементы
        label = QLabel("Label")
        button1 = QPushButton("Button 1")
        button2 = QPushButton("Button 2")
        button3 = QPushButton("Button 3")
        button4 = QPushButton("Button 4")

        # Добавляем элементы в QGridLayout
        grid_layout.addWidget(label, 0, 0)      # (строка, столбец)
        grid_layout.addWidget(button1, 0, 1)
        grid_layout.addWidget(button2, 1, 0)
        grid_layout.addWidget(button3, 1, 1)
        grid_layout.addWidget(button4, 2, 0, 1, 2)  # занимает 1 строку и 2 столбца

        # Устанавливаем layout для окна
        self.setLayout(grid_layout)

        self.setWindowTitle("QGridLayout Example")
        self.resize(300, 200)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())