import sys

from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton


class MorseCode(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 500, 550, 150)
        self.setWindowTitle("Азбука Морзе 2")
        self.alphabet_buttons = {}

        self.morse_dict = {
            "a": ".-",
            "b": "-...",
            "c": "-.-.",
            "d": "-..",
            "e": ".",
            "f": "..-.",
            "g": "--.",
            "h": "....",
            "i": "..",
            "j": ".---",
            "k": "-.-",
            "l": ".-..",
            "m": "--",
            "n": "-.",
            "o": "---",
            "p": ".--.",
            "q": "--.-",
            "r": ".-.",
            "s": "...",
            "t": "-",
            "u": "..-",
            "v": "...-",
            "w": ".--",
            "x": "-..-",
            "y": "-.--",
            "z": "--..",
        }

        new_line = False
        space = 1
        self.alphabet_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                               'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                               'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                               'y', 'z']

        for let in self.alphabet_lower:
            self.btn = QPushButton(let, self)
            self.alphabet_buttons[let] = self.btn
            if not new_line:
                self.btn.setGeometry(space, 10, 25, 25)
                if self.alphabet_lower.index(let) > 16:
                    new_line = True
            else:
                self.btn.setGeometry(
                    (self.alphabet_lower.index(let) * 30) - 16 * 30, 50, 25, 25
                )

            self.btn.clicked.connect(self.is_clicked)
            space += 30

        self.result = QLineEdit(self)
        self.result.setGeometry(70, 100, 200, 25)

    def is_clicked(self):
        let = self.sender().text()
        prev_text = self.result.text()

        self.result.setText(prev_text + self.morse_dict[let])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MorseCode()
    ex.show()
    sys.exit(app.exec())
