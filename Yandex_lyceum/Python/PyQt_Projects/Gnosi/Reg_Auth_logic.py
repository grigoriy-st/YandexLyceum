# Reg and Auth logic
import sqlite3
import random
from PyQt6.QtWidgets import QMessageBox
from django.core.checks import Critical
from pysss import password


class RegAuthLogic:
    def __init__(self):
        super().__init__()
        
    def regestration_ac(self, login, password, ac_type=1):
          # + 1 так как индексация типов с нуля

        if not login or not password:
            self.show_message("Ошибка", "Пожалуйста, введите корректное число.")

        try:
            con = sqlite3.connect("test_db.sqlite")
            cur = con.cursor()
            user_data = dict(cur.execute(f'''
                        select
                            users.login,
                            users.password
                        from users
                        where 
                            users.login = "{login}" and users.password = "{password}"
                    ''').fetchall())

            if login in user_data.keys():
                if password == user_data[login]:
                    self.show_message("Ошибка", "Такой пользователь уже есть.")
                    return
            all_userIDs = sorted(cur.execute(f'''
                                            select users.userID
                                            from users
                                    ''').fetchall())
            userID = self.generate_userID(all_userIDs)
            try:
                _ = cur.execute(f'''
                                    insert into users
                                        (userid, name,  login, password, accounttypeid)
                                        values
                                        ({userID}, "Пользователь", "{login}", "{password}", {ac_type})
                                ''')
                self.show_message(f"Поздравляем, {login}!", "Вы зарегистрированы!", "Information")
            except Exception as e:
                self.show_message("Error!", e)


            con.commit()
            

        except Exception as e:
            print(e)
        else:
            con.close()

        ...

    def generate_userID(self, all_userIDs):
        id = random.randint(1, 1000)
        while id in all_userIDs:
            id = random.randint(1, 1000)
        return id

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