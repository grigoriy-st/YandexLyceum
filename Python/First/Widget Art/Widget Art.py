import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QGridLayout, \
    QPushButton, QWidget


class WidgetArt(QMainWindow):
    def __init__(self, matrix):
        super().__init__()
        self.matrix = matrix
        # uic.loadUi(f, self)
        self.initUI()

    def initUI(self):
        main_w = QWidget()
        self.setCentralWidget(main_w)
        self.setMinimumSize(400, 300)
        self.widgetArt = QGridLayout()
        main_w.setLayout(self.widgetArt)

        length_col = len(self.matrix[0])
        length_row = len(self.matrix)
        for row in range(length_row):
            for col in range(length_col):
                button = QPushButton("*" if self.matrix[row][col] else "")
                self.widgetArt.addWidget(button, row, col)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    matrix = [
        [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
        [0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
        [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    ]
    ex = WidgetArt(matrix)
    ex.show()
    sys.exit(app.exec())
