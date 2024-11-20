import sys
from PyQt5 import QtWidgets
from window_ui import WindowUI
from logic import Logic

class MainApp:
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.window = WindowUI()
        self.logic = Logic()

    def run(self):
        self.window.show()
        sys.exit(self.app.exec_())

if __name__ == '__main__':
    main_app = MainApp()
    main_app.run()