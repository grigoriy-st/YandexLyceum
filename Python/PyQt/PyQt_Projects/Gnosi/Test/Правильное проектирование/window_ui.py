from PyQt5 import QtWidgets

class WindowUI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('My Application')
        self.setGeometry(100, 100, 300, 200)
        self.button = QtWidgets.QPushButton('Click Me', self)
        self.button.clicked.connect(self.on_button_click)

    def on_button_click(self):
        print("Button clicked!")