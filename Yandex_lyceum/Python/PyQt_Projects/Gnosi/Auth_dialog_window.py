# Form implementation generated from reading ui file 'Auth_dialog_window.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox, QDialog, QApplication
from enum import Enum
from Reg_dialog_window import Reg_Dialog

class Auth_Dialog(QDialog):
    class DialogCode(Enum):
        Accepted_for_Registration = 1001

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(300, 270)
        Dialog.setMaximumSize(QtCore.QSize(300, 300))
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(40, -1, 40, -1)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbl_login = QtWidgets.QLabel(parent=Dialog)
        self.lbl_login.setMaximumSize(QtCore.QSize(70, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_login.setFont(font)
        self.lbl_login.setObjectName("lbl_login")
        self.horizontalLayout.addWidget(self.lbl_login)
        self.lineE_login = QtWidgets.QLineEdit(parent=Dialog)
        self.lineE_login.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lineE_login.setObjectName("lineE_login")
        self.horizontalLayout.addWidget(self.lineE_login)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(30, -1, 35, -1)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lbl_password = QtWidgets.QLabel(parent=Dialog)
        self.lbl_password.setMaximumSize(QtCore.QSize(70, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_password.setFont(font)
        self.lbl_password.setObjectName("lbl_password")
        self.horizontalLayout_2.addWidget(self.lbl_password)
        self.lineE_password = QtWidgets.QLineEdit(parent=Dialog)
        self.lineE_password.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lineE_password.setObjectName("lineE_password")
        self.horizontalLayout_2.addWidget(self.lineE_password)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_enter = QtWidgets.QPushButton(parent=Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_enter.sizePolicy().hasHeightForWidth())
        self.btn_enter.setSizePolicy(sizePolicy)
        self.btn_enter.setMinimumSize(QtCore.QSize(0, 5))
        self.btn_enter.setMaximumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_enter.setFont(font)
        self.btn_enter.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.btn_enter.setDefault(False)
        self.btn_enter.setObjectName("btn_enter")
        self.horizontalLayout_3.addWidget(self.btn_enter)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.btn_registration = QtWidgets.QPushButton(parent=Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_registration.sizePolicy().hasHeightForWidth())
        self.btn_registration.setSizePolicy(sizePolicy)
        self.btn_registration.setMaximumSize(QtCore.QSize(16777215, 20))
        self.btn_registration.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.btn_registration.setFlat(True)
        self.btn_registration.setObjectName("btn_registration")
        self.verticalLayout.addWidget(self.btn_registration)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)

    # Signals
        self.btn_enter.clicked.connect(self.entry_auth_data)
        self.btn_registration.clicked.connect(self.registration_new_ac)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Авторизация"))
        self.lbl_login.setText(_translate("Dialog", "Логин:"))
        self.lbl_password.setText(_translate("Dialog", "Пароль:"))
        self.btn_enter.setText(_translate("Dialog", "Войти"))
        self.btn_registration.setText(_translate("Dialog", "Регистрация"))

    def entry_auth_data(self):
        login = self.lineE_login.text()
        password = self.lineE_password.text()
        if not login or not password:
            self.show_error_message("Ошибка", "Пожалуйста, введите корректное число.")
        else:
            self.accept()


    def show_error_message(self, title, message):
        dlg = QMessageBox()
        dlg.setWindowTitle("Ошибка!")
        dlg.setText("Вы неправильно ввели данные!")
        button = dlg.exec()

        if button == QMessageBox.StandardButton.Ok:
            print("OK!")

    def registration_new_ac(self):
        self.register_window = Reg_Dialog()  # Создаем экземпляр окна регистрации

        self.register_window.exec()