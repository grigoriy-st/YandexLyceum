import sys
from PyQt5.QtWidgets import (QApplication, QTreeWidget,
                             QTreeWidgetItem, QMenu, QAction, QMessageBox,
                            QInputDialog
                             )
from PyQt5.QtCore import Qt
class MyTreeWidget(QTreeWidget):
    def __init__(self):
        super().__init__()
        self.setHeaderLabels(['Items'])
        self.add_sample_items()
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.show_context_menu)

    def add_sample_items(self):
        parent_item = QTreeWidgetItem(self, ['Parent Item'])
        child_item1 = QTreeWidgetItem(parent_item, ['Child Item 1'])
        child_item2 = QTreeWidgetItem(parent_item, ['Child Item 2'])
        QTreeWidgetItem(self, ['Another Parent Item'])

    def show_context_menu(self, pos):
        item = self.itemAt(pos)
        menu = QMenu(self)

        if item is not None:
            # Добавляем действия, доступные для всех элементов
            rename_action = QAction('Переименовать', self)
            delete_action = QAction('Удалить элемент', self)

            # Добавляем действия, доступные только для дочерних элементов
            if item.parent() is not None:  # Это дочерний элемент
                create_theory_action = QAction('Создать теорию', self)
                load_material_action = QAction('Загрузить готовый материал', self)
                menu.addAction(create_theory_action)
                menu.addAction(load_material_action)

            menu.addAction(rename_action)
            menu.addAction(delete_action)

            # Подключаем действия к методам
            rename_action.triggered.connect(lambda: self.rename_item(item))
            delete_action.triggered.connect(lambda: self.delete_item(item))

            # Отображаем контекстное меню
            menu.exec_(self.viewport().mapToGlobal(pos))

    def rename_item(self, item):
        # Логика переименования элемента
        new_name, ok = QInputDialog.getText(self, 'Переименовать', 'Введите новое имя:', text=item.text(0))
        if ok and new_name:
            item.setText(0, new_name)

    def delete_item(self, item):
        # Логика удаления элемента
        reply = QMessageBox.question(self, 'Удалить элемент', 'Вы уверены, что хотите удалить этот элемент?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            index = self.indexOfTopLevelItem(item) if item.parent() is None else item.parent().indexOfChild(item)
            if item.parent() is None:
                self.takeTopLevelItem(index)
            else:
                item.parent().removeChild(item)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    tree_widget = MyTreeWidget()
    tree_widget.resize(400, 300)
    tree_widget.show()
    sys.exit(app.exec_())