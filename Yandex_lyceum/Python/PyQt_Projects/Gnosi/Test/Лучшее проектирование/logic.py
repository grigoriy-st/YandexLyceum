# logic.py
from PyQt5.QtWidgets import QTreeWidgetItem

class Logic:
    def __init__(self, tree_widget):
        self.tree_widget = tree_widget

    def add_item(self, item_text):
        # Добавляем элемент в QTreeWidget
        QTreeWidgetItem(self.tree_widget, [item_text])