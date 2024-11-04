import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton,
    QTabWidget, QLabel, QWidget,
    QVBoxLayout
)
from PyQt6.QtCore import QSize

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(800, 500)
        self.setWindowTitle("Gnosi")
        self.initUI()

    def initUI(self):
        self.tabWidget = QTabWidget()
        self.setCentralWidget(self.tabWidget)
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.West)
        self.tabWidget.setMinimumSize(200, 100)
        self.tabWidget.resize(100, 100)
        self.create_tabs()

    def create_tabs(self):
        # Вкладка 1
        tab1 = QWidget()
        layout1 = QVBoxLayout()
        layout1.addWidget(QLabel("Это первая вкладка"))
        button1 = QPushButton("Кнопка на первой вкладке")
        layout1.addWidget(button1)
        tab1.setLayout(layout1)

        # Установка размера для вкладки 1
        self.tabWidget.addTab(tab1, "Вкладка 1")
        self.tabWidget.setTabSizeHint(0, QSize(150, 50))  # Установка размера для первой вкладки

        # Вкладка 2
        tab2 = QWidget()
        layout2 = QVBoxLayout()
        layout2.addWidget(QLabel("Это вторая вкладка"))
        button2 = QPushButton("Кнопка на второй вкладке")
        layout2.addWidget(button2)
        tab2.setLayout(layout2)

        # Установка размера для вкладки 2
        self.tabWidget.addTab(tab2, "Вкладка 2")
          # Установка размера для второй вкладки

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())