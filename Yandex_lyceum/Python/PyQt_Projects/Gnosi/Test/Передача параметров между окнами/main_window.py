import sys
from PyQt5.QtWidgets import QApplication, QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget, QPushButton


class TreeWidgetExample(QWidget):
    def __init__(self):
        super().__init__()

        # Создаем QTreeWidget
        self.tree_widget = QTreeWidget()
        self.tree_widget.setHeaderLabels(['Column 1', 'Column 2'])

        # Добавляем корневой элемент
        self.root_item = QTreeWidgetItem(self.tree_widget, ['Root Item', 'Root Data'])

        # Добавляем дочерний элемент к корневому элементу
        self.child_item1 = QTreeWidgetItem(self.root_item, ['Child Item 1', 'Child Data 1'])
        self.child_item2 = QTreeWidgetItem(self.root_item, ['Child Item 2', 'Child Data 2'])

        # Кнопка для добавления потомка к потомку
        self.add_button = QPushButton("Добавить потомка к Child Item 1")
        self.add_button.clicked.connect(self.add_child_to_item1)

        # Устанавливаем layout
        layout = QVBoxLayout()
        layout.addWidget(self.tree_widget)
        layout.addWidget(self.add_button)
        self.setLayout(layout)

        self.setWindowTitle("QTreeWidget Example")
        self.resize(400, 300)

    def add_child_to_item1(self):
        # Создаем нового потомка для child_item1
        new_child_item = QTreeWidgetItem(self.child_item1, ['Grandchild Item', 'Grandchild Data'])
        # Можно также установить дополнительные свойства для нового элемента, если необходимо
        new_child_item.setText(1, 'Updated Grandchild Data')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TreeWidgetExample()
    window.show()
    sys.exit(app.exec_())