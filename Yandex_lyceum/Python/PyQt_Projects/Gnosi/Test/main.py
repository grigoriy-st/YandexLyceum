import sys

from PyQt6.QtWidgets import QApplication, QWidget, \
    QLabel, QPushButton, QMainWindow, QVBoxLayout, QStackedWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Пример QStackedWidget")

        # Создание QStackedWidget
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        # Создание виджетов для разных страниц
        self.page1 = self.create_page1()
        self.page2 = self.create_page2()

        # Добавление страниц в QStackedWidget
        self.stacked_widget.addWidget(self.page1)
        self.stacked_widget.addWidget(self.page2)

    def create_page1(self):
        page = QWidget()
        layout = QVBoxLayout()
        label = QLabel("Это первая страница")
        button = QPushButton("Перейти на вторую страницу")
        button.clicked.connect(self.show_page2)

        layout.addWidget(label)
        layout.addWidget(button)
        page.setLayout(layout)
        return page

    def create_page2(self):
        page = QWidget()
        layout = QVBoxLayout()
        label = QLabel("Это вторая страница")
        button = QPushButton("Вернуться на первую страницу")
        button.clicked.connect(self.show_page1)

        layout.addWidget(label)
        layout.addWidget(button)
        page.setLayout(layout)
        return page

    def show_page1(self):
        self.stacked_widget.setCurrentIndex(0)

    def show_page2(self):
        self.stacked_widget.setCurrentIndex(1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
