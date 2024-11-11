import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget, QPushButton, QInputDialog, QMessageBox
)


class CourseApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Course Module Manager")
        self.setGeometry(100, 100, 400, 300)

        self.tree_widget = QTreeWidget()
        self.tree_widget.setHeaderLabel("Course Structure")

        self.add_module_button = QPushButton("Add Module")
        self.add_lesson_button = QPushButton("Add Lesson")
        self.move_up_button = QPushButton("Move Up")
        self.move_down_button = QPushButton("Move Down")

        self.add_module_button.clicked.connect(self.add_module)
        self.add_lesson_button.clicked.connect(self.add_lesson)
        self.move_up_button.clicked.connect(self.move_up)
        self.move_down_button.clicked.connect(self.move_down)

        layout = QVBoxLayout()
        layout.addWidget(self.tree_widget)
        layout.addWidget(self.add_module_button)
        layout.addWidget(self.add_lesson_button)
        layout.addWidget(self.move_up_button)
        layout.addWidget(self.move_down_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def add_module(self):
        module_name, ok = QInputDialog.getText(self, "Add Module", "Enter module name:")
        if ok and module_name:
            QTreeWidgetItem(self.tree_widget, [module_name])

    def add_lesson(self):
        selected_item = self.tree_widget.currentItem()
        if selected_item is None or selected_item.parent() is None:
            QMessageBox.warning(self, "Warning", "Please select a module to add a lesson.")
            return

        lesson_name, ok = QInputDialog.getText(self, "Add Lesson", "Enter lesson name:")
        if ok and lesson_name:
            QTreeWidgetItem(selected_item, [lesson_name])

    def move_up(self):
        selected_item = self.tree_widget.currentItem()
        if selected_item is None:
            QMessageBox.warning(self, "Warning", "Please select an item to move.")
            return

        parent_item = selected_item.parent()
        if parent_item is None:
            index = self.tree_widget.indexOfTopLevelItem(selected_item)
            if index > 0:
                self.tree_widget.insertTopLevelItem(index - 1, self.tree_widget.takeTopLevelItem(index))
                self.tree_widget.setCurrentItem(selected_item)
        else:
            index = parent_item.indexOfChild(selected_item)
            if index > 0:
                parent_item.insertChild(index - 1, parent_item.takeChild(index))
                self.tree_widget.setCurrentItem(selected_item)

    def move_down(self):
        selected_item = self.tree_widget.currentItem()
        if selected_item is None:
            QMessageBox.warning(self, "Warning", "Please select an item to move.")
            return

        parent_item = selected_item.parent()
        if parent_item is None:
            index = self.tree_widget.indexOfTopLevelItem(selected_item)
            if index < self.tree_widget.topLevelItemCount() - 1:
                self.tree_widget.insertTopLevelItem(index + 1, self.tree_widget.takeTopLevelItem(index))
                self.tree_widget.setCurrentItem(selected_item)
        else:
            index = parent_item.indexOfChild(selected_item)
            if index < parent_item.childCount() - 1:
                parent_item.insertChild(index + 1, parent_item.takeChild(index))
                self.tree_widget.setCurrentItem(selected_item)

    def keyPressEvent(self, event):
        if event.key() == 16777223:  # Qt.Key_Delete
            self.delete_item()

    def delete_item(self):
        selected_item = self.tree_widget.currentItem()
        if selected_item is None:
            QMessageBox.warning(self, "Warning", "Please select an item to delete.")
            return

        reply = QMessageBox.question(self, "Confirm Delete", "Are you sure you want to delete this item?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            if selected_item.parent() is None:
                index = self.tree_widget.indexOfTopLevelItem(selected_item)
                self.tree_widget.takeTopLevelItem(index)
            else:
                parent_item = selected_item.parent()
                parent_item.removeChild(selected_item)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CourseApp()
    window.show()
    sys.exit(app.exec_())