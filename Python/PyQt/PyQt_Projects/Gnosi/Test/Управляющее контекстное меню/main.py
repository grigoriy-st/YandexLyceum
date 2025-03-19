import sys
from PyQt5.QtWidgets import QApplication, QTreeWidget, QTreeWidgetItem, QMenu, QAction, QMessageBox, QInputDialog
from PyQt5.QtCore import Qt

class MyTreeWidget(QTreeWidget):
    def __init__(self):
        super().__init__()
        self.setHeaderLabels(["Items"])

        # Пример добавления элементов
        self.addTopLevelItem(QTreeWidgetItem(["Элемент 1"]))
        child_item = QTreeWidgetItem(["Дочерний элемент 1"])
        self.topLevelItem(0).addChild(child_item)
        child_item.addChild(QTreeWidgetItem(["Дочерний от дочернего элемент 1"]))

        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.show_context_menu)

    def show_context_menu(self, position):
        item = self.itemAt(position)
        menu = QMenu(self)

        create_theory_action = QAction("Создать теорию", self)
        load_file_action = QAction("Загрузить готовый файл", self)
        rename_action = QAction("Переименовать", self)
        delete_action = QAction("Удалить", self)

        create_theory_action.triggered.connect(self.create_theory)
        load_file_action.triggered.connect(self.load_file)
        rename_action.triggered.connect(self.rename_item)
        delete_action.triggered.connect(self.delete_item)

        menu.addAction(create_theory_action)
        menu.addAction(load_file_action)
        menu.addAction(rename_action)
        menu.addAction(delete_action)

        menu.exec_(self.viewport().mapToGlobal(position))

    def create_theory(self):
        QMessageBox.information(self, "Создать теорию", "Создание теории...")

    def load_file(self):
        QMessageBox.information(self, "Загрузить файл", "Загрузка файла...")

    def rename_item(self):
        item = self.currentItem()
        if item:
            new_name, ok = QInputDialog.getText(self, "Переименовать", "Введите новое имя:", text=item.text(0))
            if ok and new_name:
                item.setText(0, new_name)

    def delete_item(self):
        item = self.currentItem()
        if item:
            index = self.indexOfTopLevelItem(item) if item.parent() is None else item.parent().indexOfChild(item)
            if item.parent() is None:
                self.takeTopLevelItem(index)
            else:
                item.parent().removeChild(item)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    tree_widget = MyTreeWidget()
    tree_widget.resize(400, 300)
    tree_widget.show()
    sys.exit(app.exec_())