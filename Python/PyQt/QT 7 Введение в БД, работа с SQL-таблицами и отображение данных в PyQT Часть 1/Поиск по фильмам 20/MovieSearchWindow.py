import sys
import sqlite3

from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QTableWidgetItem, QMainWindow

DB_NAME = 'films_db.sqlite'


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(493, 385)
        self.setupUi()

    def setupUi(self):

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.label_3.setText("Год")
        self.verticalLayout_3.addWidget(self.label_3)
        self.year = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.year.setMaximumSize(QtCore.QSize(350, 16777215))
        self.year.setObjectName("year")
        self.verticalLayout_3.addWidget(self.year)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.label_4.setText("Название")
        self.verticalLayout_4.addWidget(self.label_4)
        self.title = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.title.setMaximumSize(QtCore.QSize(350, 16777215))
        self.title.setObjectName("title")
        self.verticalLayout_4.addWidget(self.title)
        self.verticalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.label_6.setText("Длина")
        self.verticalLayout_2.addWidget(self.label_6)
        self.duration = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.duration.setMaximumSize(QtCore.QSize(350, 16777215))
        self.duration.setObjectName("duration")
        self.verticalLayout_2.addWidget(self.duration)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.queryButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.queryButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.queryButton.setObjectName("queryButton")
        self.queryButton.setText("Поиск")
        self.queryButton.clicked.connect(self.find_films)

        self.horizontalLayout_2.addWidget(self.queryButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)

        headers = ['id', 'title', 'year', 'genre', 'duration']
        self.tableWidget.setHorizontalHeaderLabels(headers)
        self.horizontalLayout_3.addWidget(self.tableWidget)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 493, 21))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

    def find_films(self):
        year = self.year.text()
        title = self.title.text()
        duration = self.duration.text()

        qparams = []
        qp1 = qp2 = qp3 = ''
        if year:
            qp1 = f'(year {year})'  # т.к. знаки уже передаются
            qparams.append(qp1)
        if title:
            qp2 = f'(films.title {title})'  # т.к. доп. условие уже передаётся
            qparams.append(qp2)
        if duration:
            qp3 = f'(duration {duration})'  # т.к. знаки уже передаются
            qparams.append(qp3)

        q = f'''
                    select 
                        films.id, films.title, films.year, genres.title, films.duration
                    from
                        films
                    inner join
                        genres on genres.id = films.genre
                    where
                        {' and '.join(qparams)}
                '''

        con = sqlite3.connect(DB_NAME)
        cur = con.cursor()

        result = list(cur.execute(q).fetchall())
        rows = len(result)
        self.tableWidget.setRowCount(rows)

        self.fill_table(result)

    def fill_table(self, result):
        for row, entry in enumerate(result):
            id, title, year, genre, duration = entry
            self.tableWidget.setItem(row, 0, QTableWidgetItem(str(id)))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(title))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(str(year)))
            self.tableWidget.setItem(row, 3, QTableWidgetItem(str(genre)))
            self.tableWidget.setItem(row, 4, QTableWidgetItem(str(duration)))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = MyWidget()
    ui.show()
    sys.exit(app.exec())
