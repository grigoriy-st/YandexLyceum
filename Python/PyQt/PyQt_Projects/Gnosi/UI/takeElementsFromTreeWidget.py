import sys
import json
from PyQt5.QtWidgets import QApplication, QTreeWidget, QTreeWidgetItem, QPushButton, QVBoxLayout, QWidget


def tree_to_dict(tree_widget):
    """ Преобразует QTreeWidget в словарь. """
    tree_dict = {}

    for index in range(tree_widget.topLevelItemCount()):
        item = tree_widget.topLevelItem(index)
        tree_dict[item.text(0)] = item_to_dict(item)

    return tree_dict


def item_to_dict(item):
    """ Рекурсивно преобразует элемент QTreeWidgetItem в словарь. """
    item_dict = {}

    for index in range(item.childCount()):
        child_item = item.child(index)
        item_dict[child_item.text(0)] = item_to_dict(child_item)

    return item_dict


def save_tree_to_json(tree_widget, filename):
    """ Сохраняет данные QTreeWidget в JSON-файл. """
    tree_data = tree_to_dict(tree_widget)
    with open(filename, 'w') as json_file:
        json.dump(tree_data, json_file, indent=4)


class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.tree_widget = QTreeWidget()
        self.tree_widget.setHeaderLabel("My Tree")

        # Пример заполнения QTreeWidget
        item1 = QTreeWidgetItem(self.tree_widget, ["Item 1"])
        item2 = QTreeWidgetItem(self.tree_widget, ["Item 2"])
        child1 = QTreeWidgetItem(item1, ["Child 1"])
        child2 = QTreeWidgetItem(item1, ["Child 2"])

        # Кнопка для сохранения в JSON
        self.save_button = QPushButton("Save to JSON")
        self.save_button.clicked.connect(self.save_to_json)

        layout = QVBoxLayout()
        layout.addWidget(self.tree_widget)
        layout.addWidget(self.save_button)

        self.setLayout(layout)

    def save_to_json(self):
        save_tree_to_json(self.tree_widget, 'tree_data.json')
        print("Данные сохранены в tree_data.json")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())