from PyQt5.QtWidgets import (QApplication,
                             QWidget, QGridLayout,
                             QLabel, QPushButton, QVBoxLayout)


class ProductCard(QWidget):
    def __init__(self, name, price):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel(name))
        layout.addWidget(QLabel(f'Price: {price}'))
        layout.addWidget(QPushButton('Buy'))
        self.setLayout(layout)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QGridLayout()

        # Пример добавления карточек товаров
        products = [
            ("Product 1", "$10"),
            ("Product 2", "$20"),
            ("Product 3", "$30"),
        ]

        for index, (name, price) in enumerate(products):
            card = ProductCard(name, price)
            layout.addWidget(card, index // 3, index % 3)  # размещение в сетке

        self.setLayout(layout)


app = QApplication([])
window = MainWindow()
window.show()
app.exec_()