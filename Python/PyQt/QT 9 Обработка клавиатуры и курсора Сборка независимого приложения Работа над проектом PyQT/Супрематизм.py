import sys
import random

from PyQt6.QtGui import QPainter, QColor, QCursor, QPolygonF
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtCore import Qt, QPointF, QRectF


class Suprematism(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(1000, 1000)
        self.shapes = []

    def paintEvent(self, event):
        painter = QPainter(self)

        for el in self.shapes:
            painter.setBrush(el['color'])
            if el['type'] == 'circle':
                painter.drawEllipse(QPointF(el['pos'].x(), el['pos'].y()), el['size'], el['size'])
            elif el['type'] == 'square':
                rect = QRectF(el['pos'].x() - el['size'] / 2, el['pos'].y() - el['size'] / 2, el['size'], el['size'])
                painter.drawRect(rect)
            elif el['type'] == 'triangle':
                radius = el['size']

                coords = [
                    QPointF(el['pos'].x(),
                            el['pos'].y() - radius * (3 ** 0.5) / 2),

                    QPointF(el['pos'].x() - radius / 2,
                            el['pos'].y() + radius * (3 ** 0.5) / 6),

                    QPointF(el['pos'].x() + radius / 2,
                            el['pos'].y() + radius * (3 ** 0.5) / 6)
                ]
                polygon = QPolygonF(coords)
                painter.drawPolygon(polygon)

    def mousePressEvent(self, event):
        """ Обработка кликов мыши. Рисование круга или квадрата. """
        if event.button() == Qt.MouseButton.LeftButton:
            size = random.randint(20, 100)
            color = self.get_random_color()

            shape_info = {'type': 'circle',
                          'pos': event.pos(),
                          'size': size,
                          'color': color}
            self.shapes.append(shape_info)

        elif event.button() == Qt.MouseButton.RightButton:
            size = random.randint(20, 100)
            color = self.get_random_color()

            shape_info = {'type': 'square',
                          'pos': event.pos(),
                          'size': size,
                          'color': color}
            self.shapes.append(shape_info)

        self.update()  # Обновление окна

    def keyPressEvent(self, event):
        """ Обработка нажатия пробела. Рисование треугольника. """
        if event.key() == Qt.Key.Key_Space:
            size = random.randint(20, 100)
            color = self.get_random_color()
            cursor_pos = self.mapFromGlobal(QCursor.pos())

            shape_info = {'type': 'triangle',
                          'pos': cursor_pos,
                          'size': size,
                          'color': color}
            self.shapes.append(shape_info)
            self.update()

    def get_random_color(self):
        """ Получение рандомного цвета. """
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = QColor(r, g, b)

        return color


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Suprematism()

    ui.show()
    sys.exit(app.exec())