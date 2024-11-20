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

from reference import Reference_Dialog
from w_create_theory import Window_for_create_theory


DB_NAME = "test_db.sqlite"


class Logic():
    def __init__(self):
        super().__init__()
        self.temp_course_name = None
        self.courseID = None


    def show_courses_in_courses_tab(self, table):
        con = sqlite3.connect(DB_NAME)
        cur = con.cursor()
        courses_list = cur.execute(
            '''
            select 
                courses.Title,
                users.Login,
                courses.Description,
                courses.CreatedDate
            from 
                courses inner join users on courses.userid = users.UserID

            '''
        ).fetchall()
        con.close()

        table.setRowCount(len(courses_list))
        for index, course in enumerate(courses_list):
            course_name, course_author, course_description, course_created_date = course
            table.setItem(index, 0, QTableWidgetItem(course_name))
            table.setItem(index, 1, QTableWidgetItem(course_author))
            table.setItem(index, 2, QTableWidgetItem(course_description))
            table.setItem(index, 3, QTableWidgetItem(course_created_date))
        ...

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

        table.setRowCount(len(courses_list))
        for index, course in enumerate(courses_list):
            course_name, course_author, course_description, course_created_date = course
            table.setItem(index, 0, QTableWidgetItem(course_name))
            table.setItem(index, 1, QTableWidgetItem(course_author))
            table.setItem(index, 2, QTableWidgetItem(course_description))
            table.setItem(index, 3, QTableWidgetItem(course_created_date))


        con.close()




    def create_module(self, tree_widget):
        module_name, ok = QInputDialog.getText(tree_widget, "Создать модуль", "Введите название модуля:")
        if ok and module_name:
            # Добавляем модуль в QTreeWidget
            module_item = QTreeWidgetItem(tree_widget, [module_name])
            tree_widget.addTopLevelItem(module_item)
            print(os.listdir('.'))

            if not self.temp_course_name:
                self.temp_course_name = f'Unsaved_{random.randint(0, 10)}'
                while not os.path.exists(self.temp_course_name):
                    self.temp_course_name = f'Unsaved_{random.randint(0, 10)}'
                    os.mkdir(self.temp_course_name)
                os.chdir(self.temp_course_name)
            os.mkdir(module_name)

        # self.courseID = self.generate_courseID()


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
            action = menu.exec(self.treeWidget.viewport().mapToGlobal(pos))

            # Обрабатываем выбранный элемент
            if action:
                if action.text() == 'Создать урок':
                    self.create_lesson()
                elif action.text() == 'Переименовать':
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

    def create_theory(self, item):
        """Создание теории"""
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
        """Загрузка готового документа"""
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

    def create_course(self, course_params):
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
        os.chdir("Courses")
        os.rename(self.temp_course_name, title)
        self.export_to_json()

    def export_to_json(self):
        data = self.tree_to_dict(self.treeWidget.invisibleRootItem())
        json_data = json.dumps(data, indent=4)
        print(json_data)  # Выводим в консоль, можно записать в файл

    def tree_to_dict(self, item):
        result = {"name": item.text(0), "children": []}
        for index in range(item.childCount()):
            child_item = item.child(index)
            result["children"].append(self.tree_to_dict(child_item))

        return result


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
        os.chdir(history_of_movements)
        return gen_courseID

    def move_to_gnosi_folder(self):
        history = []
        cur_dir = os.path.basename(os.getcwd())
        while DB_NAME not in os.listdir('.'):
            print("Now in", os.getcwd())

            history.insert(0, os.path.basename(os.getcwd()))
            os.chdir("..")

        return '/'.join(history[1:])

    def clearing_the_course_creation_window(self, course_name, course_description):
        self.treeWidget.clear()
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