import sys

from PyQt6.QtWidgets import QApplication, QWidget, \
    QLabel, QPushButton, QButtonGroup, QRadioButton


class FlagMaker(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 430, 200)
        self.setWindowTitle('Арифмометр')
        self.setFixedSize(430, 200)
    # first_box
        self.text = QLabel("Цвет №1", self)
        self.text.move(60, 30)
        self.cs01 = QRadioButton("Синий", self)
        self.cs01.move(60, 70)

        self.cs02 = QRadioButton("Красный", self)
        self.cs02.move(60, 90)

        self.cs03 = QRadioButton("Зелёный", self)
        self.cs03.move(60, 110)

        self.color_group_1 = QButtonGroup(self)
        self.color_group_1.addButton(self.cs01)
        self.color_group_1.addButton(self.cs02)
        self.color_group_1.addButton(self.cs03)

    # second_box
        self.text = QLabel("Цвет №2", self)
        self.text.move(180, 30)
        self.cs11 = QRadioButton("Синий", self)
        self.cs11.move(180, 70)

        self.cs12 = QRadioButton("Красный", self)
        self.cs12.move(180, 90)

        self.cs13 = QRadioButton("Зелёный", self)
        self.cs13.move(180, 110)

        self.color_group_2 = QButtonGroup(self)
        self.color_group_2.addButton(self.cs11)
        self.color_group_2.addButton(self.cs12)
        self.color_group_2.addButton(self.cs13)

    # third_box
        self.text = QLabel("Цвет №3", self)
        self.text.move(300, 30)
        self.cs11 = QRadioButton("Синий", self)
        self.cs11.move(300, 70)

        self.cs12 = QRadioButton("Красный", self)
        self.cs12.move(300, 90)

        self.cs13 = QRadioButton("Зелёный", self)
        self.cs13.move(300, 110)

        self.color_group_3 = QButtonGroup(self)
        self.color_group_3.addButton(self.cs11)
        self.color_group_3.addButton(self.cs12)
        self.color_group_3.addButton(self.cs13)

        self.make_flag = QPushButton("Сделать флаг", self)
        self.make_flag.clicked.connect(self.is_clicked)
        self.make_flag.move(310, 150)

        self.result = QLabel(self)
        self.result.setStyleSheet("font-family: Arial;\
                                  font-size: 12px;\
                                  font-weight: normal;")
        self.result.move(30, 160)
        self.result.setVisible(False)

    def is_clicked(self):
        res_data = []

        for gtn_group in [self.color_group_1, self.color_group_2,
                          self.color_group_3]:
            for btn in gtn_group.buttons():
                if btn.isChecked():
                    res_data.append(btn.text())

        self.result.setText(f'Цвета: {res_data[0]}, \
{res_data[1]} и {res_data[2]}')
        self.result.setVisible(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet("QLabel { font-family: Arial;\
                      font-size: 20px;\
                      font-weight: bold;}")
    ex = FlagMaker()
    ex.show()
    sys.exit(app.exec())
