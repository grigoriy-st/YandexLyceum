import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QSlider, QLabel
from PIL import Image


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 500, 510)
        self.setWindowTitle('Изменение прозрачности')

        self.fname = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]
        self.save = 'save.png'
        self.slider = QSlider(Qt.Vertical, self)
        self.slider.resize(20, 380)
        self.slider.move(30, 40)
        self.slider.setMinimum(0)
        self.slider.setMaximum(255)
        self.slider.setValue(255)
        self.slider.valueChanged[int].connect(self.visibility)

        self.pixmap = QPixmap(self.fname)
        self.image = QLabel(self)
        self.image.resize(330, 330)
        self.image.move(100, 65)
        self.image.setPixmap(self.pixmap)

    def visibility(self, value):
        im = Image.open(self.fname)
        im = im.convert('RGBA')
        im.putalpha(value)
        im.save(self.save)
        self.pixmap = QPixmap(self.save)
        self.to_show = self.pixmap.copy()
        self.image.setPixmap(self.to_show)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())