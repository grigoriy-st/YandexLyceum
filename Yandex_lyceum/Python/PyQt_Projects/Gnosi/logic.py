# logic.py

from PyQt6.QtWidgets import (QTreeWidget, QTreeWidgetItem,
                             QInputDialog, QMessageBox, QMenu)
from lesson_management import Window_lesson_management
from reference import Reference_Dialog

class Logic:
    def __init__(self, treeWidget):
        self.treeWidget = treeWidget

    def open_lesson_management_window(self, item, column):
        if item.parent() is not None:
            print("Открыто окно для создания теории по уроку")
            w_to_choose_when_creating_course = Window_lesson_management(self.treeWidget)
            w_to_choose_when_creating_course.exec()

    def create_module(self):
        module_name, ok = QInputDialog.getText(self.treeWidget, "Создать модуль", "Введите название модуля:")
        if ok and module_name:
            # Добавляем модуль в QTreeWidget
            module_item = QTreeWidgetItem(self.treeWidget, [module_name])
            self.treeWidget.addTopLevelItem(module_item)

    def create_lesson(self):
        selected_items = self.treeWidget.selectedItems()
        if not selected_items:
            # Если модуль не выбран, показываем сообщение об ошибке
            QMessageBox.warning(self.treeWidget, "Ошибка", "Сначала выберите модуль, чтобы создать урок.")
            return

        lesson_name, ok = QInputDialog.getText(self.treeWidget, "Создать урок", "Введите название урока:")
        if ok and lesson_name:
            # Получаем выбранный модуль
            module_item = selected_items[0]
            # Добавляем урок как дочерний элемент к выбранному модулю
            lesson_item = QTreeWidgetItem(module_item, [lesson_name])
            module_item.addChild(lesson_item)

    def move_up(self):
        selected_item = self.treeWidget.currentItem()
        if selected_item is None:
            QMessageBox.warning(self.treeWidget, "Ошибка", "Пожалуйста, выберите объект для перемещения")
            return

        parent_item = selected_item.parent()
        if parent_item is None:
            index = self.treeWidget.indexOfTopLevelItem(selected_item)
            if index > 0:
                self.treeWidget.insertTopLevelItem(index - 1, self.treeWidget.takeTopLevelItem(index))
                self.treeWidget.setCurrentItem(selected_item)
        else:
            index = parent_item.indexOfChild(selected_item)
            if index > 0:
                parent_item.insertChild(index - 1, parent_item.takeChild(index))
                self.treeWidget.setCurrentItem(selected_item)

    def move_down(self):
        selected_item = self.treeWidget.currentItem()
        if selected_item is None:
            QMessageBox.warning(self.treeWidget, "Warning", "Please select an item to move.")
            return

        parent_item = selected_item.parent()
        if parent_item is None:
            index = self.treeWidget.indexOfTopLevelItem(selected_item)
            if index < self.treeWidget.topLevelItemCount() - 1:
                self.treeWidget.insertTopLevelItem(index + 1, self.treeWidget.takeTopLevelItem(index))
                self.treeWidget.setCurrentItem(selected_item)
        else:
            index = parent_item.indexOfChild(selected_item)
            if index < parent_item.childCount() - 1:
                parent_item.insertChild(index + 1, parent_item.takeChild(index))
                self.treeWidget.setCurrentItem(selected_item)

    def show_reference(self):
        w_ref = Reference_Dialog()
        w_ref.exec()

    def show_context_menu(self, pos):
        item = self.treeWidget.itemAt(pos)

        menu = QMenu(self.treeWidget)
        if item is not None:
            # Добавляем действия, доступные для всех элементов
            menu.addAction('Переименовать')
            menu.addAction('Удалить элемент')
            # Добавляем действия, доступные только для дочерних элементов
            if item.parent() is not None:  # Это дочерний элемент
                menu.addAction('Создать теорию')
                menu.addAction('Загрузить готовый материал')
            # Отображаем контекстное меню и получаем выбранный элемент
            action = menu.exec(self.treeWidget.viewport().mapToGlobal(pos))
            # Обрабатываем выбранный элемент
            if action:
                if action.text() == 'Переименовать':
                    self.rename_item(item)
                elif action.text() == 'Удалить элемент':
                    self.delete_item(item)
                elif action.text() == 'Создать теорию':
                    self.create_theory(item)
                elif action.text() == 'Загрузить готовый материал':
                    self.load_material(item)

    def rename_item(self, item):
        new_name, ok = QInputDialog.getText(None, 'Переименовать', 'Введите новое имя:', text=item.text(0))
        if ok and new_name:
            item.setText(0, new_name)

    def delete_item(self, item):
        reply = QMessageBox.question(None, 'Удалить элемент', 'Вы уверены, что хотите удалить этот элемент?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            if item.parent() is None:
                index = item.treeWidget().indexOfTopLevelItem(item)
                item.treeWidget().takeTopLevelItem(index)
            else:
                item.parent().removeChild(item)

    def create_theory(self, item):
        QMessageBox.information(None, 'Создать теорию', f'Создание теории для {item.text(0)}')
    def load_material(self, item):
        QMessageBox.information(None, 'Загрузить материал', f'Загрузка материала для {item.text(0)}')
