# main.py
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeWidget, QTreeWidgetItem, QPushButton, QVBoxLayout, QWidget
from logic import Logic

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Main Window")
        self.setGeometry(100, 100, 400, 300)

        # Создаем виджет QTreeWidget
        self.tree_widget = QTreeWidget()
        self.tree_widget.setHeaderLabel("Items")

        # Кнопка для добавления элемента
        self.button = QPushButton("Add Item")
        self.button.clicked.connect(self.add_item)

        # Устанавливаем макет
        layout = QVBoxLayout()
        layout.addWidget(self.tree_widget)
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Создаем экземпляр логики
        self.logic = Logic(self.tree_widget)

    def add_item(self):
        self.logic.add_item("New Item")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())