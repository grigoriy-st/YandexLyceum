import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QComboBox, QLineEdit, QPushButton, QTableView, QVBoxLayout, QHBoxLayout)
from PyQt5.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow


class CoursesWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300, 300)
        self.setWindowTitle("Курсы")

        # Create labels and widgets
        self.label_courses = QLabel("Курсы")
        self.combobox_filters = QComboBox()
        self.combobox_filters.addItems(["Все", "Популярные", "Новинки"])
        self.lineedit_search = QLineEdit()
        self.button_search = QPushButton("Поиск")
        self.table_view = QTableView()

        # Create layouts
        hbox_top = QHBoxLayout()
        hbox_top.addWidget(self.label_courses)
        hbox_top.addWidget(self.combobox_filters)
        hbox_top.addWidget(self.lineedit_search)
        hbox_top.addWidget(self.button_search)

        vbox_main = QVBoxLayout()
        vbox_main.addLayout(hbox_top)
        vbox_main.addWidget(self.table_view)

        # Set layout
        self.setLayout(vbox_main)

        # Align elements
        self.label_courses.setAlignment(Qt.AlignLeft)
        self.combobox_filters.setAlignment(Qt.AlignLeft)
        self.lineedit_search.setAlignment(Qt.AlignLeft)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    courses_widget = CoursesWidget()
    courses_widget.show()
    sys.exit(app.exec_())