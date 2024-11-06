from PyQt5 import QtWidgets, QtGui, QtCore
import sys

class CourseCatalog(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Каталог курсов")
        self.setGeometry(100, 100, 400, 300)

        # Создаем вертикальный layout
        layout = QtWidgets.QVBoxLayout(self)

        # Создаем QScrollArea
        self.scroll_area = QtWidgets.QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)  # Позволяет автоматически изменять размер виджета
        layout.addWidget(self.scroll_area)

        # Создаем виджет для размещения курсов
        self.course_widget = QtWidgets.QWidget()
        self.course_layout = QtWidgets.QVBoxLayout(self.course_widget)

        # Добавляем курсы в layout
        self.add_courses()

        # Устанавливаем курсорный виджет в QScrollArea
        self.scroll_area.setWidget(self.course_widget)

    def add_courses(self):
        # Пример курсов
        courses = [
            "Курс 1: Основы Python",
            "Курс 2: Продвинутый Python",
            "Курс 3: Разработка веб-приложений",
            "Курс 4: Мобильная разработка",
            "Курс 5: Машинное обучение",
            "Курс 6: Анализ данных",
            "Курс 7: Искусственный интеллект",
            "Курс 8: Разработка игр",
            "Курс 9: Кибербезопасность",
            "Курс 10: Базы данных",
            # Добавьте больше курсов для демонстрации прокрутки
        ]

        for course in courses:
            course_label = QtWidgets.QLabel(course)
            course_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
            self.course_layout.addWidget(course_label)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = CourseCatalog()
    window.show()
    sys.exit(app.exec_())