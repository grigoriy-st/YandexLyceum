# logic.py
import os
import random

from PyQt6.QtWidgets import (QTreeWidget, QTreeWidgetItem,
                             QInputDialog, QMessageBox, QMenu, QDialog)
from lesson_management import Window_lesson_management
from reference import Reference_Dialog
from w_create_theory import Window_for_create_theory
class Logic:
    def __init__(self, treeWidget):
        self.treeWidget = treeWidget
        self.temp_course_name = None


    def create_module(self):
        module_name, ok = QInputDialog.getText(self.treeWidget, "Создать модуль", "Введите название модуля:")
        if ok and module_name:
            # Добавляем модуль в QTreeWidget
            module_item = QTreeWidgetItem(self.treeWidget, [module_name])
            self.treeWidget.addTopLevelItem(module_item)
            os.chdir("Courses")
            self.temp_course_name = f'Unsaved_{random.randint(0, 10)}'
            while not os.path.exists(self.temp_course_name):
                self.temp_course_name = f'Unsaved_{random.randint(0, 10)}'
                os.mkdir(self.temp_course_name)
            os.chdir(self.temp_course_name)
            os.mkdir(module_name)

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
            module_name = module_item.text(0)
            print(module_name)
            # Добавляем урок как дочерний элемент к выбранному модулю
            lesson_item = QTreeWidgetItem(module_item, [lesson_name])
            module_item.addChild(lesson_item)

            os.chdir(f"Courses/{self.temp_course_name}/{module_name}")
            os.mkdir(lesson_name)

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

            # Проверяем уровень вложенности
            level = 0
            parent = item.parent()
            while parent is not None:
                level += 1
                parent = parent.parent()

            # Добавляем действия, доступные только для дочерних элементов второго уровня
            if level == 1:  # Это дочерний элемент второго уровня
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
                                     QMessageBox.StandardButton.Yes |
                                     QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            if item.parent() is None:
                index = item.treeWidget().indexOfTopLevelItem(item)
                item.treeWidget().takeTopLevelItem(index)
            else:
                item.parent().removeChild(item)

    def create_theory(self, item):
        ui = Window_for_create_theory()
        if ui.exec() == 1:

            lesson_name, lesson_text = ui.get_article_info()
            print(lesson_name, lesson_text)
            _ = QTreeWidgetItem(item, [lesson_name])

            with open(lesson_name, "w", encoding="utf-8") as f:
                f.write(lesson_text)


    def load_material(self, item):
        QMessageBox.information(None, 'Загрузить материал', f'Загрузка материала для {item.text(0)}')
