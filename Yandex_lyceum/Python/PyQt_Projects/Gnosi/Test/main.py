import sys
from PyQt5.QtWidgets import QApplication, QTreeWidget, QTreeWidgetItem, QMessageBox, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Создаем QTreeWidget
        self.tree_widget = QTreeWidget()
        self.setCentralWidget(self.tree_widget)

        # Устанавливаем заголовок
        self.tree_widget.setHeaderLabel("Items")

        # Добавляем элементы в QTreeWidget
        parent_item = QTreeWidgetItem(self.tree_widget, ["Parent Item"])
        child_item1 = QTreeWidgetItem(parent_item, ["Child Item 1"])
        child_item2 = QTreeWidgetItem(parent_item, ["Child Item 2"])

        # Подключаем сигнал itemClicked к слоту
        self.tree_widget.itemClicked.connect(self.on_item_clicked)

    def on_item_clicked(self, item, column):
        # Проверяем, что кликнули на потомка
        if item.parent() is not None:
            # Открываем окно с информацией о выбранном элементе
            self.show_message_box(item.text(0))

    def show_message_box(self, item_name):
        # Создаем и показываем окно сообщения
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Item Clicked")
        msg_box.setText(f"You clicked on: {item_name}")
        msg_box.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())