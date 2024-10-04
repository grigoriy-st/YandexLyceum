import sys

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, \
    QLineEdit, QLabel, QTimeEdit, QCalendarWidget 


class SimplePlanner(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.timeEdit = QTimeEdit(self)
        self.calendarWidget = QCalendarWidget()
        
        # self.addEventBtn = QPushButton("Жобавить событие", self)
        # self.addEventBtn.clicked.connect(self.is_clicked)

    def is_clicked(self):
        ...


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SimplePlanner()
    ex.show()
    sys.exit(app.exec())
