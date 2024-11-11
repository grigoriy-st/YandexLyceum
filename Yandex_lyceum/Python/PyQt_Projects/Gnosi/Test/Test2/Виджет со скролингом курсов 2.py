import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QGridLayout,
    QTableWidget,
    QTableWidgetItem,
)
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt

class CourseCard(QWidget):
    def __init__(self, title, author, description, difficulty, icon_path):
        super().__init__()
        self.title = title
        self.author = author
        self.description = description
        self.difficulty = difficulty
        self.icon_path = icon_path

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(5)

        # Icon
        icon_label = QLabel()
        pixmap = QPixmap(self.icon_path)
        icon_label.setPixmap(pixmap)
        layout.addWidget(icon_label)

        # Title
        title_label = QLabel(self.title)
        title_label.setFont(QFont("Arial", 14, QFont.Bold))
        layout.addWidget(title_label)

        # Author
        author_label = QLabel(f"Автор: {self.author}")
        layout.addWidget(author_label)

        # Description
        description_label = QLabel(self.description)
        description_label.setWordWrap(True)
        layout.addWidget(description_label)

        # Difficulty
        difficulty_label = QLabel(f"Сложность: {self.difficulty}")
        layout.addWidget(difficulty_label)

        self.setLayout(layout)


class CourseTable(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Список курсов")

        # Create QTableWidget
        self.table = QTableWidget()
        self.table.setColumnCount(1)
        self.table.setHorizontalHeaderLabels(["Курс"])
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)

        # Set up layout
        layout = QVBoxLayout()
        layout.addWidget(self.table)
        self.setLayout(layout)

        # Add course cards to the table
        self.populateTable()

    def populateTable(self):
        courses = [
            {
                "title": "Операционные системы",
                "author": "Андрей Буранов",
                "description": "Курс предназначен для студентов IT-специальностей.",
                "difficulty": "Легко",
                "icon_path": "path/to/icon.png"  # Replace with actual icon path
            },
            # Add more courses as needed
        ]

        self.table.setRowCount(len(courses))

        for row, course in enumerate(courses):
            card = CourseCard(course["title"], course["author"], course["description"], course["difficulty"], course["icon_path"])
            self.table.setCellWidget(row, 0, card)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    course_table = CourseTable()
    course_table.resize(400, 300)
    course_table.show()
    sys.exit(app.exec_())