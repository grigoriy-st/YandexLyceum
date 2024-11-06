# main.py
import sys
from PyQt5 import QtWidgets
from gui import MainWindow  # Импортируем главный класс GUI

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())