import os
import sys
import datetime
import zipfile

from PyQt6.QtWidgets import (
    QApplication, QPushButton,
    QLabel, QVBoxLayout,
    QLineEdit, QTextEdit, QFileDialog, QWidget
)


class Main_Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300, 300)
        self.init_ui()

    def init_ui(self):
        v_layout = QVBoxLayout()

        self.source_label = QLabel("Каталог для архивирования:")
        self.source_input = QLineEdit()
        self.source_btn = QPushButton('Выбрать')
        self.source_btn.clicked.connect(self.select_source)

        self.dest_label = QLabel("Каталог назначения:")
        self.dest_input = QLineEdit()
        self.dest_btn = QPushButton('Выбрать')
        self.dest_btn.clicked.connect(self.select_dest)

        self.main_btn = QPushButton('Архивировать')
        self.main_btn.clicked.connect(self.create_backup)
        self.status_text = QTextEdit()
        self.status_text.setReadOnly(True)

        widgets = [self.source_label, self.source_input,
                   self.source_btn, self.dest_label,
                   self.dest_input, self.dest_btn,
                   self.main_btn, self.status_text]

        for widget in widgets:
            v_layout.addWidget(widget)
        self.setLayout(v_layout)

    def select_source(self):
        dir = QFileDialog.getExistingDirectory(self)
        if dir:
            self.source_input.setText(dir)

    def select_dest(self):
        dir = QFileDialog.getExistingDirectory(self)
        if dir:
            self.dest_input.setText(dir)

    def create_backup(self):
        source = self.source_input.text()
        dest = self.dest_input.text()
        result = self.make_backup(source, dest)
        self.status_text.append(result)

    def make_backup(self, source, dest):
        if not os.path.isdir(source):
            return f"Исходгого каталога {source} не существует."

        if not os.path.isdir(dest):
            return f'Каталога назначения {dest} не существует.'

        now_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        arch_name = f'backup_{now_time}.zip'
        arch_path = os.path.join(dest, arch_name)

        with zipfile.ZipFile(arch_path, 'w') as out_file:
            for root, dirs, files in os.walk(source):
                for file in files:
                    file_path = os.path.join(root, file)
                    out_file.write(file_path, os.path.relpath(file_path, os.path.dirname(source)))

        return "Архивирование прошло успешно"


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main_Window()
    window.show()
    sys.exit(app.exec())
