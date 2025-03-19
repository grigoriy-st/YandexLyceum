import sys
import os
import shutil
from datetime import datetime
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QVBoxLayout, QLabel


class BackupUtility(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Архивирование')
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        self.source_button = QPushButton('Выбрать каталог для резервного копирования', self)
        self.source_button.clicked.connect(self.select_source_directory)
        layout.addWidget(self.source_button)

        self.dest_button = QPushButton('Выбрать каталог для сохранения резервной копии', self)
        self.dest_button.clicked.connect(self.select_dest_directory)
        layout.addWidget(self.dest_button)

        self.backup_button = QPushButton('Создать резервную копию', self)
        self.backup_button.clicked.connect(self.make_reserve_arc)
        layout.addWidget(self.backup_button)

        self.status_label = QLabel('', self)
        layout.addWidget(self.status_label)

        self.setLayout(layout)

        self.source_path = ''
        self.dest_path = ''

    def select_source_directory(self):
        self.source_path = QFileDialog.getExistingDirectory(self, "Каталог для резервного копирования")
        if self.source_path:
            self.status_label.setText(f'Исходный каталог: {self.source_path}')

    def select_dest_directory(self):
        self.dest_path = QFileDialog.getExistingDirectory(self, "Каталог для сохранения резервной копии")
        if self.dest_path:
            self.status_label.setText(f'Каталог назначения: {self.dest_path}')

    def make_reserve_arc(self):
        if not self.source_path or not self.dest_path:
            self.status_label.setText('Ошибка: Каталоги неверно указаны')
            return

        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        archive_name = f"backup_{current_time}.zip"
        archive_path = os.path.join(self.dest_path, archive_name)

        shutil.make_archive(archive_path[:-4], 'zip', self.source_path)
        self.status_label.setText(f'Резервная копия успешно создана: {archive_path}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = BackupUtility()
    ex.show()
    sys.exit(app.exec())