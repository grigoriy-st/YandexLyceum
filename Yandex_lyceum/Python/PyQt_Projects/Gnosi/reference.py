import sys

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QDialog


class Reference_Dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(631, 513)

        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.TE_reference = QtWidgets.QTextEdit(parent=Dialog)
        self.TE_reference.setObjectName("TE_reference")
        self.verticalLayout.addWidget(self.TE_reference)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_close_ref = QtWidgets.QPushButton(parent=Dialog)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_close_ref.sizePolicy().hasHeightForWidth())
        self.btn_close_ref.setSizePolicy(sizePolicy)
        self.btn_close_ref.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.btn_close_ref.setDefault(True)
        self.btn_close_ref.setObjectName("btn_close_ref")
        self.btn_close_ref.clicked.connect(self.close_window)

        self.horizontalLayout_2.addWidget(self.btn_close_ref)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Справка"))
        self.TE_reference.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Ubuntu Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Добро пожаловать в конструктор курсов!</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Здесь вы можете создать модули и уроки.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Для управления конструктора элементами воспользуйтесь <span style=\" font-weight:700;\">правой кнопкой мыши или нижними кнопками</span>.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.btn_close_ref.setText(_translate("Dialog", "Закрыть"))

    def close_window(self):
        self.close()

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Reference_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
