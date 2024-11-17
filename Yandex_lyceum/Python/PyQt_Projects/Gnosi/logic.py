# logic.py
import os
import random
import shutil
import sqlite3
import datetime
from readline import get_history_item

from Cryptodome.SelfTest.Cipher.test_OFB import file_name
from PyQt6.QtWidgets import (QTreeWidget, QTreeWidgetItem,
                             QInputDialog, QMessageBox, QMenu, QDialog, QFileDialog)
from lesson_management import Window_lesson_management
from reference import Reference_Dialog
from w_create_theory import Window_for_create_theory
class Logic:
    def __init__(self, treeWidget):
        self.treeWidget = treeWidget
        self.temp_course_name = None
        os.chdir("Courses")

    def create_module(self):
        module_name, ok = QInputDialog.getText(self.treeWidget, "Создать модуль", "Введите название модуля:")
        if ok and module_name:
            # Добавляем модуль в QTreeWidget
            module_item = QTreeWidgetItem(self.treeWidget, [module_name])
            self.treeWidget.addTopLevelItem(module_item)
            print(os.listdir('.'))

            if not self.temp_course_name:
                self.temp_course_name = f'Unsaved_{random.randint(0, 10)}'
                while not os.path.exists(self.temp_course_name):
                    self.temp_course_name = f'Unsaved_{random.randint(0, 10)}'
                    os.mkdir(self.temp_course_name)
                os.chdir(self.temp_course_name)
            os.mkdir(module_name)

    def create_lesson(self):
        selected_items = self.treeWidget.selectedItems()
        print("Ты вместе с: ", '  '.join(os.listdir('.')))
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
            lesson = QTreeWidgetItem(module_item, [lesson_name])
            module_item.addChild(lesson)

            os.chdir(module_name)
            os.mkdir(lesson_name)
            os.chdir('..')

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
        print("ТЫ хочаешь создать теорию в :", os.listdir('.'))
        if ui.exec() == 1:
            lesson_item_name, lesson_text = ui.get_article_info()

            selected_items = self.treeWidget.selectedItems()
            fs_lvl1, fs_lvl2 = self.get_item_hierarchy(item) # поиск элементов выше по иерархии
            lesson_item = selected_items[0]
            lesson_name = lesson_item.text(0)

            # print(lesson_name, lesson_text)
            lesson = QTreeWidgetItem(item, [lesson_item_name])
            lesson_item.addChild(lesson)

            with open(f"{fs_lvl1}/{lesson_name}/{lesson_item_name}", "w", encoding="utf-8") as f:
                f.write(lesson_text)


    def load_material(self, item):
        file_path, _ = QFileDialog.getOpenFileName(self.treeWidget, "Выберите файл", "", "Все файлы (*)")
        if file_path:
            QMessageBox. information(self.treeWidget, "Информация", f"Вы выбрали файл: {file_path}")
        file_name = str(file_path).split('/')[-1]
        destination_path = "/".join(self.get_item_hierarchy(item))
        print("-->", destination_path)
        print(os.getcwd())
        try:
            # Копируем файл
            shutil.copy(file_path, f"{destination_path}")
            print(f'Файл скопирован в: {destination_path}')
            lesson = QTreeWidgetItem(item, [file_name])
        except Exception as e:
            print("Ошибка!", e)


    def get_item_hierarchy(self, item) -> list:
        hierarchy = []
        current_item = item
        # Сбор информации о родителях
        while current_item:
            hierarchy.insert(0, current_item.text(0))  # Добавляем текст элемента в начало списка
            current_item = current_item.parent()
        return hierarchy

    def get_selected_items_hierarchy(self):
        selected_items = self.treeWidget.selectedItems()
        for item in selected_items:
            hierarchy = self.get_item_hierarchy(item)

            print(" -> ".join(hierarchy))

    def create_course(self, course_name, course_description):
        con = sqlite3.connect("test_db.sqlite")
        cur = con.cursor()

        courseID = ...
        title = course_name
        userid = ...
        description = course_description
        complexity = ...
        createdDate = datetime.now().strftime("%Y-%m-%d")

        _ = cur.execute(
            f'''
            insert into courses
            ({courseID}, {title}, {userid}, {description}, {complexity}, {createdDate})
            values
            (1, "hello", 2, " world", 2, "!")
            '''
        )

    def create_json_course_path(self):
        ...

    def generate_courseID(self) -> int:
        ...