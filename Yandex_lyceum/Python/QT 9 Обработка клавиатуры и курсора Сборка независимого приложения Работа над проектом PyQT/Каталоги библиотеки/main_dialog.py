# Form implementation generated from reading ui file 'main_dialog.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(410, 351)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.cb_filter = QtWidgets.QComboBox(parent=Dialog)
        self.cb_filter.setMinimumSize(QtCore.QSize(0, 0))
        self.cb_filter.setMaximumSize(QtCore.QSize(200, 16777215))
        self.cb_filter.setStyleSheet("QCheckBox { text-align: center; }")
        self.cb_filter.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.cb_filter.setObjectName("cb_filter")
        self.cb_filter.addItem("")
        self.cb_filter.addItem("")
        self.verticalLayout.addWidget(self.cb_filter)
        self.le_search_box = QtWidgets.QLineEdit(parent=Dialog)
        self.le_search_box.setObjectName("le_search_box")
        self.verticalLayout.addWidget(self.le_search_box)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.btn_find = QtWidgets.QPushButton(parent=Dialog)
        self.btn_find.setObjectName("btn_find")
        self.horizontalLayout.addWidget(self.btn_find)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.list_widget = QtWidgets.QListWidget(parent=Dialog)
        self.list_widget.setObjectName("list_widget")
        self.verticalLayout_2.addWidget(self.list_widget)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.cb_filter.setItemText(0, _translate("Dialog", "Название"))
        self.cb_filter.setItemText(1, _translate("Dialog", "Автор"))
        self.btn_find.setText(_translate("Dialog", "Искать"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
