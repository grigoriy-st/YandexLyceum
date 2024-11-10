# Form implementation generated from reading ui file 'Reg_dialog_window.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.
from PyQt5.QtCore.QUrl import password
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QDialog


class Reg_Dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(299, 262)
        Dialog.setMaximumSize(QtCore.QSize(300, 300))
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
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
        self.lineE_pasword = QtWidgets.QLineEdit(parent=Dialog)
        self.lineE_pasword.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lineE_pasword.setObjectName("lineE_pasword")
        self.horizontalLayout_2.addWidget(self.lineE_pasword)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lbl_account = QtWidgets.QLabel(parent=Dialog)
        self.lbl_account.setMaximumSize(QtCore.QSize(140, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_account.setFont(font)
        self.lbl_account.setObjectName("lbl_account")
        self.horizontalLayout_4.addWidget(self.lbl_account)
        self.CB_change_ac_type = QtWidgets.QComboBox(parent=Dialog)
        self.CB_change_ac_type.setObjectName("CB_change_ac_type")
        self.CB_change_ac_type.addItem("")
        self.CB_change_ac_type.addItem("")
        self.horizontalLayout_4.addWidget(self.CB_change_ac_type)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_enter = QtWidgets.QPushButton(parent=Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_enter.sizePolicy().hasHeightForWidth())
        self.btn_enter.setSizePolicy(sizePolicy)
        self.btn_enter.setMinimumSize(QtCore.QSize(0, 5))
        self.btn_enter.setMaximumSize(QtCore.QSize(160, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_enter.setFont(font)
        self.btn_enter.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.btn_enter.setDefault(False)
        self.btn_enter.setObjectName("btn_enter")
        self.horizontalLayout_3.addWidget(self.btn_enter)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5.addLayout(self.verticalLayout)

    # Signals
        self.btn_enter.clicke.connect(self.registration_ac)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", " Регистрация"))
        self.lbl_login.setText(_translate("Dialog", "Логин:"))
        self.lbl_password.setText(_translate("Dialog", "Пароль:"))
        self.lbl_account.setText(_translate("Dialog", "Тип уч. записи:"))
        self.CB_change_ac_type.setItemText(0, _translate("Dialog", "Ученик"))
        self.CB_change_ac_type.setItemText(1, _translate("Dialog", "Учитель"))
        self.btn_enter.setText(_translate("Dialog", "Зарегистрироваться"))

    def registration_ac(self):
        # Проверка на правильность водимых данных

        login = self.lineE_login.text()
        password = self.lineE_pasword.text()


        ...