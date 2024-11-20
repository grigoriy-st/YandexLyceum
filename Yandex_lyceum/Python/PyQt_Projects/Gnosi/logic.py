# logic.py
import os
import random
import shutil
import sqlite3
import datetime
import json
import traceback

from PyQt6.QtWidgets import (QTreeWidget, QTreeWidgetItem,
                             QInputDialog, QMessageBox, QMenu, QDialog, QFileDialog, QTableWidget, QTableWidgetItem)
from PyQt6.QtCore import Qt
from reference import Reference_Dialog
from w_create_theory import Window_for_create_theory
from course_structure import CourseStructureW

DB_NAME = "test_db.sqlite"
BASE_DIR = ''
COURSES_DIR = 'Courses'

class Logic():
    def __init__(self):
        super().__init__()
        self.temp_course_name = None    # переменная хранения временного имени курса
        self.courseID = None

    def create_module(self, tree_widget):
        module_name, ok = QInputDialog.getText(tree_widget, "Создать модуль", "Введите название модуля:")
        if ok and module_name:
            # Добавляем модуль в QTreeWidget
            module_item = QTreeWidgetItem(tree_widget, [module_name])
            tree_widget.addTopLevelItem(module_item)

            if not self.temp_course_name:
                os.chdir('./Courses')
                self.temp_course_name = f'Unsaved_{random.randint(0, 10)}'
                while not os.path.exists(self.temp_course_name):
                    self.temp_course_name = f'Unsaved_{random.randint(0, 10)}'
                    os.mkdir(self.temp_course_name)
                os.chdir(self.temp_course_name)
            os.mkdir(module_name)

        # self.courseID = self.generate_courseID()

    def create_lesson(self, treeWidget):
        selected_items = treeWidget.selectedItems()
        print("Ты вместе с: ", '  '.join(os.listdir('.')))
        if not selected_items:
            # Если модуль не выбран, показываем сообщение об ошибке
            QMessageBox.warning(treeWidget, "Ошибка", "Сначала выберите модуль, чтобы создать урок.")
            return

        lesson_name, ok = QInputDialog.getText(treeWidget, "Создать урок", "Введите название урока:")
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

    def move_up(self, treeWidget):
        selected_item = treeWidget.currentItem()
        if selected_item is None:
            QMessageBox.warning(treeWidget, "Ошибка", "Пожалуйста, выберите объект для перемещения")
            return

        parent_item = selected_item.parent()
        if parent_item is None:
            index = treeWidget.indexOfTopLevelItem(selected_item)
            if index > 0:
                treeWidget.insertTopLevelItem(index - 1, treeWidget.takeTopLevelItem(index))
                treeWidget.setCurrentItem(selected_item)
        else:
            index = parent_item.indexOfChild(selected_item)
            if index > 0:
                parent_item.insertChild(index - 1, parent_item.takeChild(index))
                treeWidget.setCurrentItem(selected_item)

    def move_down(self, treeWidget):
        selected_item = treeWidget.currentItem()
        if selected_item is None:
            QMessageBox.warning(treeWidget, "Warning", "Please select an item to move.")
            return

        parent_item = selected_item.parent()
        if parent_item is None:
            index = treeWidget.indexOfTopLevelItem(selected_item)
            if index < treeWidget.topLevelItemCount() - 1:
                treeWidget.insertTopLevelItem(index + 1, treeWidget.takeTopLevelItem(index))
                treeWidget.setCurrentItem(selected_item)
        else:
            index = parent_item.indexOfChild(selected_item)
            if index < parent_item.childCount() - 1:
                parent_item.insertChild(index + 1, parent_item.takeChild(index))
                treeWidget.setCurrentItem(selected_item)

    def rename_item(self, item):
        new_name, ok = QInputDialog.getText(None, 'Переименовать', 'Введите новое имя:', text=item.text(0))
        if ok and new_name:
            item.setText(0, new_name)

    def delete_item(self, item):
        """Удаление элемента из QTreeWidget и из папки с курсом"""
        reply = QMessageBox.question(None, 'Удалить элемент', 'Вы уверены, что хотите удалить этот элемент?',
                                     QMessageBox.StandardButton.Yes |
                                     QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            if item.parent() is None:
                index = item.treeWidget().indexOfTopLevelItem(item)
                item.treeWidget().takeTopLevelItem(index)
            else:
                item.parent().removeChild(item)

    def show_reference(self):
        w_ref = Reference_Dialog()
        w_ref.exec()

    def show_courses_in_courses_tab(self, table):
        con = sqlite3.connect(DB_NAME)
        cur = con.cursor()
        courses_list = cur.execute(
            '''
            select
                courses.courseid,
                courses.Title,
                users.Name,
                courses.Description,
                courses.CreatedDate
            from 
                courses inner join users on courses.userid = users.UserID

            '''
        ).fetchall()
        con.close()

        row_quantity = len(courses_list)
        table.setRowCount(row_quantity)

        for index, course in enumerate(courses_list):
            courseID, course_name, course_author, course_description, course_created_date = course
            table.setItem(index, 0, QTableWidgetItem(str(courseID)))
            table.setItem(index, 1, QTableWidgetItem(course_name))
            table.setItem(index, 2, QTableWidgetItem(course_author))
            table.setItem(index, 3, QTableWidgetItem(course_description))
            table.setItem(index, 4, QTableWidgetItem(course_created_date))

        self.protect_table_from_changes(table, row_quantity)

    def show_courses_in_my_courses_tab(self, uid, table):
        print(uid)
        print(os.getcwd())
        con = sqlite3.connect(DB_NAME)
        cur = con.cursor()

        courses_list = cur.execute(
                f'''
                select 
                    courses.Title,
                    users.Name,
                    courses.Description,
                    courses.CreatedDate
                from 
                    courses inner join users on courses.userid = users.UserID
                where
                    courses.userid = {uid}
                '''
        ).fetchall()
        row_quantity = len(courses_list)
        table.setRowCount()
        for index, course in enumerate(courses_list):
            course_name, course_author, course_description, course_created_date = course
            table.setItem(index, 0, QTableWidgetItem(course_name))
            table.setItem(index, 1, QTableWidgetItem(course_author))
            table.setItem(index, 2, QTableWidgetItem(course_description))
            table.setItem(index, 3, QTableWidgetItem(course_created_date))

        con.close()
        self.protect_table_from_changes(table, row_quantity)

    def protect_table_from_changes(self, table, row_quantity):
        '''Убирает возможность редактирования ячеек таблиц'''

        for row in range(row_quantity):
            for col in range(5):
                item = table.item(row, col)
                item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)

    def on_cell_clicked(self, tw_all_courses, tw_my_courses, row, column):
        course_id = tw_all_courses.item(row, 0).text()
        course_name = tw_all_courses.item(row, 1).text()

        self.move_to_gnosi_folder()
        os.chdir(COURSES_DIR)

        if course_name in os.listdir('.'):
            os.chdir(course_name)
            courseStructureW = CourseStructureW()
            self.fill_treeWidget_in_course_structure_w(courseStructureW.TW_course_structure, course_name)
            return_code = courseStructureW.exec()
            if return_code == 1:
                self.show_message("Успешно!",
                                  f"Курс \"{course_name}\" добавлен во вкладку \"Мои курсы\"",
                                  "Information")
                return course_id
        else:
            self.show_message("Ошибка",
                              f"В папке курсов нет курса \"{course_name}\"")

        self.move_to_gnosi_folder()


    def add_course_to_my_courses(self, tw_my_courses, course_id):
        self.move_to_gnosi_folder()
        con = sqlite3.connect(DB_NAME)
        cur = con.cursor()
        course_data = cur.execute(
            f'''
            select
                courses.Title, users.Name, courses.Description, courses.CreatedDate
            from
                courses inner join users on users.UserID = courses.UserID
            where
                courses.CourseID = 123
            '''
        ).fetchall()[0]
        row_quantity = tw_my_courses.rowCount()
        course_name = course_data[0]
        course_author = course_data[1]
        course_description = course_data[2]
        course_created_date = course_data[3]
        tw_my_courses.setItem(tw_my_courses, row_quantity, 0, QTableWidgetItem(str(course_id)))
        tw_my_courses.setItem(tw_my_courses, row_quantity, 0, QTableWidgetItem(course_name))
        tw_my_courses.setItem(tw_my_courses, row_quantity, 0, QTableWidgetItem(course_author))
        tw_my_courses.setItem(tw_my_courses, row_quantity, 0, QTableWidgetItem(course_description))
        tw_my_courses.setItem(tw_my_courses, row_quantity, 0, QTableWidgetItem(course_created_date))



    def show_context_menu(self, tree_widget, pos):
        item = tree_widget.itemAt(pos)

        menu = QMenu(tree_widget)

        if item is not None:
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
            if level == 0:
                menu.addAction('Создать урок')
            # Добавляем действия, доступные для всех элементов
            menu.addAction('Переименовать')
            menu.addAction('Удалить элемент')

            # Отображаем контекстное меню и получаем выбранный элемент
            action = menu.exec(tree_widget.viewport().mapToGlobal(pos))

            # Обрабатываем выбранный элемент
            if action:
                if action.text() == 'Создать урок':
                    self.create_lesson(tree_widget)
                elif action.text() == 'Переименовать':
                    self.rename_item(item)
                elif action.text() == 'Удалить элемент':
                    self.delete_item(item)
                elif action.text() == 'Создать теорию':
                    self.create_theory(tree_widget, item)
                elif action.text() == 'Загрузить готовый материал':
                    self.load_material(tree_widget, item)

    def create_theory(self, tree_widget, item):
        """Создание теории"""
        ui = Window_for_create_theory()
        print("ТЫ хочаешь создать теорию в :", os.listdir('.'))
        if ui.exec() == 1:
            lesson_item_name, lesson_text = ui.get_article_info()

            selected_items = tree_widget.selectedItems()
            fs_lvl1, fs_lvl2 = self.get_item_hierarchy(item) # поиск элементов выше по иерархии
            lesson_item = selected_items[0]
            lesson_name = lesson_item.text(0)

            # print(lesson_name, lesson_text)
            lesson = QTreeWidgetItem(item, [lesson_item_name])
            lesson_item.addChild(lesson)

            with open(f"{fs_lvl1}/{lesson_name}/{lesson_item_name}", "w", encoding="utf-8") as f:
                f.write(lesson_text)

    def load_material(self, tree_widget, item):
        """Загрузка готового документа"""
        file_path, _ = QFileDialog.getOpenFileName(tree_widget, "Выберите файл", "", "Все файлы (*)")
        if file_path:
            QMessageBox. information(tree_widget, "Информация", f"Вы выбрали файл: {file_path}")
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
        """Получение обхектов иерархии"""
        hierarchy = []
        current_item = item
        # Сбор информации о родителях
        while current_item:
            hierarchy.insert(0, current_item.text(0))  # Добавляем текст элемента в начало списка
            current_item = current_item.parent()
        return hierarchy

    def get_selected_items_hierarchy(self):
        '''Отображение иерархии'''
        selected_items = self.treeWidget.selectedItems()
        for item in selected_items:
            hierarchy = self.get_item_hierarchy(item)

            print(" -> ".join(hierarchy))

    def create_course(self, tree_widget, course_params):
        '''Создание курса и занесение его в бд'''
        courseID = self.generate_courseID()
        title = course_params['course_name']
        userid = course_params['uid']
        description = course_params['course_description']
        complexity = ["Базовый", "Средний", "Продвинутый"].index(course_params['complexity']) + 1
        createdDate = datetime.datetime.now().strftime("%Y-%m-%d")
        print("БЫЛ:", os.getcwd())
        history_of_movements = self.move_to_gnosi_folder()
        print("ПЕРЕНЁССя:", os.getcwd())
        # print("DATA:", courseID, title, userid, description, complexity, createdDate)

        con = sqlite3.connect(DB_NAME)
        cur = con.cursor()
        _ = cur.execute(
            f'''
            insert into Courses
            (CourseID, Title, UserID, Description, Complexity, CreatedDate)
            values
            ({courseID}, '{title}', {userid}, '{description}', {complexity}, '{createdDate}')
            '''
        )
        con.commit()
        con.close()
        print("Переименовываю курс в ", os.getcwd())
        os.chdir("Courses")

        os.rename(self.temp_course_name, title)
        self.temp_course_name = title
        self.save_tree_to_json(tree_widget, self.temp_course_name)

# Преобразования с JSON
    def tree_to_dict(self, tree_widget):
        """Преобразует QTreeWidget в словарь."""
        tree_dict = {}

        for index in range(tree_widget.topLevelItemCount()):
            item = tree_widget.topLevelItem(index)
            tree_dict[item.text(0)] = self.item_to_dict(item)

        return tree_dict

    def item_to_dict(self, item):
        """Рекурсивно преобразует элемент QTreeWidgetItem в словарь"""
        item_dict = {}

        for index in range(item.childCount()):
            child_item = item.child(index)
            item_dict[child_item.text(0)] = self.item_to_dict(child_item)

        return item_dict

    def save_tree_to_json(self, tree_widget, course_name):
        """Сохраняет данные QTreeWidget в json-файл"""
        tree_data = self.tree_to_dict(tree_widget)
        self.move_to_gnosi_folder()
        os.chdir(COURSES_DIR)
        os.chdir(course_name)
        with open(f'{course_name}.json', 'w') as json_file:
            json.dump(tree_data, json_file, indent=4)




    def fill_treeWidget_in_course_structure_w(self, tree_widget, course_name):
        json_file_name = course_name + '.json'
        self.load_json_to_tree_widget(tree_widget, json_file_name)

    def load_json_to_tree_widget(self, tree_widget, json_file):
        """Загружает данные из JSON-файла в QTreeWidget"""

        with open(json_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
            # Стек для хранения элементов
            stack = [(tree_widget.invisibleRootItem(), data)]
            while stack:
                parent, current_data = stack.pop()
                if isinstance(current_data, dict):
                    for key, value in current_data.items():
                        item = QTreeWidgetItem(parent, [key])
                        stack.append((item, value))  # Добавляем новый элемент и его данные в стек
                elif isinstance(current_data, list):
                    for index, value in enumerate(current_data):
                        item = QTreeWidgetItem(parent, [f"Item {index}"])
                        stack.append((item, value))  # Добавляем новый элемент и его данные в стек
                else:
                    # Если это не dict и не list, добавляем значение как текст
                    QTreeWidgetItem(parent, [str(current_data)])



    def generate_courseID(self) -> int:
        # генерация courseID
        # выход из директории Courses
        print("БЫЛ:", os.getcwd())
        history_of_movements = self.move_to_gnosi_folder()
        print("ПЕРЕНЁССя:", os.getcwd())
        con = sqlite3.connect(DB_NAME)
        cur = con.cursor()
        all_id = cur.execute(
            '''
            select courseid
            from Courses
            '''
        ).fetchall()
        all_id = [item[0] for item in all_id]
        all_id = list(map(int, all_id))
        con.close()
        os.chdir("Courses")
        gen_courseID = random.randint(1, 1000)
        while gen_courseID in all_id:
            gen_courseID = random.randint(1, 1000)
        print("____ТЫ здесь", os.getcwd())
        os.chdir('./' + history_of_movements)
        return gen_courseID

    def move_to_gnosi_folder(self):
        history = []
        cur_dir = os.path.basename(os.getcwd())
        while DB_NAME not in os.listdir('.'):
            print("Now in", os.getcwd())

            history.insert(0, os.path.basename(os.getcwd()))
            os.chdir("..")

        return '/'.join(history[1:])

    def clearing_the_course_creation_window(self, tree_widget,  course_name, course_description):
        tree_widget.clear()
        course_name.setPlainText("")
        course_description.setPlainText("")

    def edit_user_name(self, uid,  le_name, new_name):
        # print("Зашёл в edit_user_name")
        le_name.setText(new_name)
        con = sqlite3.connect(DB_NAME)
        cur = con.cursor()
        _ = cur.execute(
            f'''
            update users
            set
                name = "{new_name}"
            where
                users.userid = {uid}
            '''
        )
        con.commit()
        cur.close()
        self.show_message("Уведомление",
                          f"Вы успешно изменили имя на {new_name}!",
                          "Information")

    @staticmethod
    def show_message(title, text_msg, icon_type="Critical"):
        # Создаем окно сообщения

        msg = QMessageBox()
        match icon_type:
            case "Critical":
                msg.setIcon(QMessageBox.Icon.Critical)  # Устанавливаем иконку ошибки
            case "Information":
                msg.setIcon(QMessageBox.Icon.Information)
        msg.setText(title)
        msg.setInformativeText(text_msg)
        msg.setWindowTitle("Уведомление")
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        # Показываем окно сообщения
        msg.exec()