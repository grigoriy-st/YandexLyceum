import io
import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow


class MyNotes(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.initUI()

    def initUI(self):
        self.addContactBtn.clicked.connect(self.add_contact)

    def add_contact(self):
        if self.contactName.text() and self.contactNumber.text():
            contact = f'{self.contactName.text()} {self.contactNumber.text()}'
            self.contactList.addItem(contact)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyNotes()
    ex.show()
    sys.exit(app.exec())