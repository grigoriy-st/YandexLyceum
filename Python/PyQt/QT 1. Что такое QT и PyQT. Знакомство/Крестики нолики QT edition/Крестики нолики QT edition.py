import sys

from PyQt6.QtWidgets import QApplication, QWidget, \
    QLabel, QRadioButton, QPushButton


class TicTacToe(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 500, 300, 350)
        self.setWindowTitle("Крестики нолики QT edition")

        self.is_x = True
        self.x_radio = QRadioButton(self)
        self.x_radio.setChecked(True)
        self.x_radio.setGeometry(120, 10, 30, 25)
        self.x_radio.setText("X")
        self.o_radio = QRadioButton(self)
        self.o_radio.setGeometry(160, 10, 30, 25)
        self.o_radio.setText("O")

        self.o_radio.clicked.connect(self.change_order)
        self.x_radio.clicked.connect(self.change_order)

        self.res = {'X': 0, 'O': 0}
        self.button_grid = [[]]
        self.res_list = [['-', '-', '-'] for i in range(3)]
        self.step_num = 0
        self.history = ['X']

        x_space = 50
        y_space = 50

        for i in range(3):
            for j in range(3):
                self.btn = QPushButton("", self)
                self.btn.setGeometry(x_space, y_space, 50, 50)

                if len(self.button_grid[-1]) == 3:
                    self.button_grid.append([self.btn])
                else:
                    self.button_grid[-1].append(self.btn)

                self.btn.clicked.connect(self.is_clicked)

                x_space += 70
            y_space += 60
            x_space = 50

        self.result = QLabel("", self)
        self.result.setGeometry(120, 250, 150, 30)
        self.result.setHidden(True)

        self.new_game_button = QPushButton("Новая игра", self)
        self.new_game_button.setGeometry(100, 280, 100, 30)
        self.new_game_button.clicked.connect(self.create_new_game)

    def is_clicked(self):
        if self.result.isVisible():
            return

        sender = self.sender()
        row_btn, col_btn = 0, 0

        for row in range(3):
            for col in range(3):
                if self.button_grid[row][col] == sender:
                    row_btn, col_btn = row, col
                    break

        if self.res_list[row_btn][col_btn] == '-':
            sign = 'X' if self.is_x else 'O'
            self.res_list[row_btn][col_btn] = sign
            self.button_grid[row_btn][col_btn].setText(sign)
            self.is_x = not self.is_x
            self.step_num += 1

            win_sign = self.tic_tac_toe(self.res_list)

            if win_sign in ['X', 'O', 'Ничья']:
                if win_sign in 'XO':
                    self.result.setText(f"Выиграл {win_sign.upper()}!")
                else:
                    self.result.setText("Ничья!")
                self.result.setVisible(True)
                for row in range(3):
                    for col in range(3):
                        self.button_grid[row][col].setDisabled(True)

    def change_order(self):
        if self.x_radio.isChecked() and self.history[-1] == 'O':
            self.x_radio.setChecked(True)
            self.o_radio.setChecked(False)
            self.is_x = True
            self.history.append('X')
            self.create_new_game()

        elif self.o_radio.isChecked() and self.history[-1] == 'X':
            self.x_radio.setChecked(False)
            self.o_radio.setChecked(True)
            self.is_x = False
            self.history.append('O')
            self.create_new_game()

    def create_new_game(self):
        self.res_list = [['-', '-', '-'] for i in range(3)]
        self.result.setHidden(True)
        self.res['X'] = 0
        self.res['O'] = 0
        self.step_num = 0
        if self.x_radio.isChecked():
            self.history = ['X']
            self.is_x = True
        elif self.o_radio.isChecked():
            self.history = ['O']
            self.is_x = False
        self.clear_game_field()
        self.result = QLabel("", self)

    def clear_game_field(self):
        for row in range(3):
            for col in range(3):
                self.button_grid[row][col].setText("")
                self.button_grid[row][col].setEnabled(True)

    def tic_tac_toe(self, field):
        ver_field = [[field[row][col] for row in range(3)]
                     for col in range(3)]

        main_dgnl = [field[row][row] for row in range(3)]
        side_dgnl = []

        col = 0
        for row in range(3 - 1, -1, -1):
            side_dgnl.append(field[col][row])
            col += 1
        col = 0

        for i in range(3):
            if len(set(field[i])) == 1 and str(*set(field[i])) in ['X', 'O']:
                self.res[str(*set(field[i]))] += 1

        for i in range(3):
            if len(set(ver_field[i])) == 1:
                if str(*set(ver_field[i])) in ['X', 'O']:
                    self.res[str(*set(ver_field[i]))] += 1

        if len(set(main_dgnl)) == 1 and str(*set(main_dgnl)) in ['X', 'O']:
            self.res[str(*set(main_dgnl))] += 1

        if len(set(side_dgnl)) == 1 and str(*set(side_dgnl)) in ['X', 'O']:
            self.res[str(*set(side_dgnl))] += 1

        if self.res['X'] < self.res['O']:
            return 'O'
        if self.res['X'] > self.res['O']:
            return 'X'
        if self.step_num == 9:
            return "Ничья"


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = TicTacToe()
    ex.show()
    sys.exit(app.exec())
