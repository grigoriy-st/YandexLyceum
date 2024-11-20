# Main_Window_UI.py
from PyQt5.QtWidgets import QShortcut
from PyQt6 import QtCore, QtGui, QtWidgets

from PyQt6.QtWidgets import QInputDialog, QTreeWidgetItem, QMessageBox, QWidget
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QKeySequence
from logic import Logic


class Ui_MainWindow(object):
    def __init__(self):
        self.UID = None
        self.treeWidget = None
        self.logic = Logic()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1183, 820)

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")

        self.create_tab_widget()
        self.create_tab_profile_info()
        self.create_tab_home()
        self.create_tab_my_courses()
        self.create_tab_for_create_courses()
        self.create_tab_management_account()


        self.horizontalLayout_5.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1183, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_7.setText(_translate("MainWindow", "Мой профиль"))
        self.label_8.setText(_translate("MainWindow", "Логин:"))
        self.label_9.setText(_translate("MainWindow", "Тип учётной записи:"))
        self.label_11.setText(_translate("MainWindow", "UID:"))
        self.label_12.setText(_translate("MainWindow", "Имя:"))

        self.label.setText(_translate("MainWindow", "Курсы"))
        self.CB_change_filter.setItemText(0, _translate("MainWindow", "По умолчанию"))
        self.CB_change_filter.setItemText(1, _translate("MainWindow", "Новые"))
        self.CB_change_filter.setItemText(2, _translate("MainWindow", "Старые"))
        self.btn_search_courses.setText(_translate("MainWindow", "Поиск"))
        self.btn_search_courses.setShortcut(_translate("MainWindow", "Return"))
        self.label_2.setText(_translate("MainWindow", "Мои курсы"))
        self.label_4.setText(_translate("MainWindow", "Программма курса"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Обзор"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)


        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.btn_create_module.setText(_translate("MainWindow", "Создать модуль"))
        self.btn_create_lesson.setText(_translate("MainWindow", "Создать урок"))
        self.btn_move_up.setText(_translate("MainWindow", "Переместить выше"))
        self.pbt_move_down.setText(_translate("MainWindow", "Переместить ниже"))
        self.pbt_reference.setText(_translate("MainWindow", "Справка"))
        self.label_5.setText(_translate("MainWindow", "Название курса"))
        self.label_6.setText(_translate("MainWindow", "Описание"))
        self.btn_create_course.setText(_translate("MainWindow", "Создать курс"))
        self.label_3.setText(_translate("MainWindow", "Создание курса"))



    def create_tab_widget(self):
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.TabPosition.West)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(40, 50))
        self.tabWidget.setElideMode(QtCore.Qt.TextElideMode.ElideNone)
        self.tabWidget.setObjectName("tabWidget")

    def create_tab_profile_info(self):
        self.tab_image_account = QtWidgets.QWidget()
        self.tab_image_account.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.tab_image_account.setAutoFillBackground(False)
        self.tab_image_account.setStyleSheet("")
        self.tab_image_account.setObjectName("tab_image_account")

        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab_image_account)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")

        self.label_7 = QtWidgets.QLabel(parent=self.tab_image_account)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.verticalLayout_8.addWidget(self.label_7)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setContentsMargins(350, 50, 350, -1)
        self.verticalLayout_9.setSpacing(10)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")

        self.label_12 = QtWidgets.QLabel(parent=self.tab_image_account)
        self.label_12.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight |
            QtCore.Qt.AlignmentFlag.AlignTrailing |
            QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_10.addWidget(self.label_12)
        self.LE_name = QtWidgets.QLineEdit(parent=self.tab_image_account)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LE_name.sizePolicy().hasHeightForWidth())

        self.LE_name.setSizePolicy(sizePolicy)
        self.LE_name.setMinimumSize(QtCore.QSize(200, 0))
        self.LE_name.setMaximumSize(QtCore.QSize(250, 16777215))
        self.LE_name.setReadOnly(False)
        self.LE_name.setObjectName("LE_name")

        self.horizontalLayout_10.addWidget(self.LE_name)
        self.btn_change_name = QtWidgets.QPushButton(parent=self.tab_image_account)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_change_name.sizePolicy().hasHeightForWidth())
        self.btn_change_name.setSizePolicy(sizePolicy)
        self.btn_change_name.setObjectName("btn_change_name")
        self.btn_change_name.setText("Изменить имя")
        self.horizontalLayout_10.addWidget(self.btn_change_name)
        self.btn_change_name.clicked.connect(self.edit_user_name)

        self.verticalLayout_9.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_8 = QtWidgets.QLabel(parent=self.tab_image_account)
        self.label_8.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight |
            QtCore.Qt.AlignmentFlag.AlignTrailing |
            QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_7.addWidget(self.label_8)
        self.LE_profile_login = QtWidgets.QLineEdit(parent=self.tab_image_account)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LE_profile_login.sizePolicy().hasHeightForWidth())

        self.LE_profile_login.setSizePolicy(sizePolicy)
        self.LE_profile_login.setMinimumSize(QtCore.QSize(200, 0))
        self.LE_profile_login.setMaximumSize(QtCore.QSize(250, 16777215))
        self.LE_profile_login.setInputMask("")
        self.LE_profile_login.setReadOnly(True)
        self.LE_profile_login.setObjectName("LE_profile_login")

        self.horizontalLayout_7.addWidget(self.LE_profile_login)
        self.verticalLayout_9.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_9 = QtWidgets.QLabel(parent=self.tab_image_account)
        self.label_9.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight |
            QtCore.Qt.AlignmentFlag.AlignTrailing |
            QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_4.addWidget(self.label_9)

        self.LE_profile_type = QtWidgets.QLineEdit(parent=self.tab_image_account)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LE_profile_type.sizePolicy().hasHeightForWidth())
        self.LE_profile_type.setSizePolicy(sizePolicy)
        self.LE_profile_type.setMinimumSize(QtCore.QSize(200, 0))
        self.LE_profile_type.setMaximumSize(QtCore.QSize(250, 16777215))
        self.LE_profile_type.setReadOnly(True)
        self.LE_profile_type.setObjectName("LE_profile_type")
        self.horizontalLayout_4.addWidget(self.LE_profile_type)
        self.verticalLayout_9.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_11 = QtWidgets.QLabel(parent=self.tab_image_account)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight |
            QtCore.Qt.AlignmentFlag.AlignTrailing |
            QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_9.addWidget(self.label_11)
        self.LE_profileID = QtWidgets.QLineEdit(parent=self.tab_image_account)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LE_profileID.sizePolicy().hasHeightForWidth())
        self.LE_profileID.setSizePolicy(sizePolicy)
        self.LE_profileID.setMinimumSize(QtCore.QSize(200, 0))
        self.LE_profileID.setMaximumSize(QtCore.QSize(250, 16777215))
        self.LE_profileID.setObjectName("LE_profileID")
        self.horizontalLayout_9.addWidget(self.LE_profileID)
        self.verticalLayout_9.addLayout(self.horizontalLayout_9)
        self.verticalLayout_8.addLayout(self.verticalLayout_9)
        spacerItem = QtWidgets.QSpacerItem(20, 500, QtWidgets.QSizePolicy.Policy.Minimum,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_8.addItem(spacerItem)
        self.verticalLayout_8.setStretch(0, 1)
        self.verticalLayout_7.addLayout(self.verticalLayout_8)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UI/icons/For Left bar/profile-anonymous2.png"), QtGui.QIcon.Mode.Normal,
                       QtGui.QIcon.State.On)

        self.tabWidget.addTab(self.tab_image_account, icon, "")

    def create_tab_home(self):
        print(self.UID)
        self.tab_home = QtWidgets.QWidget()
        self.tab_home.setObjectName("tab_home")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab_home)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.tab_home)
        self.tabWidget.setCurrentIndex(1)

        font = QtGui.QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.CB_change_filter = QtWidgets.QComboBox(parent=self.tab_home)
        self.CB_change_filter.setMaximumSize(QtCore.QSize(120, 16777215))
        self.CB_change_filter.setObjectName("CB_change_filter")
        self.CB_change_filter.addItem("")
        self.CB_change_filter.addItem("")
        self.CB_change_filter.addItem("")
        self.horizontalLayout_2.addWidget(self.CB_change_filter)
        self.LE_search_string = QtWidgets.QLineEdit(parent=self.tab_home)
        self.LE_search_string.setMaximumSize(QtCore.QSize(600, 16777215))
        self.LE_search_string.setObjectName("LE_search_string")
        self.horizontalLayout_2.addWidget(self.LE_search_string)
        self.btn_search_courses = QtWidgets.QPushButton(parent=self.tab_home)
        self.btn_search_courses.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btn_search_courses.setObjectName("btn_search_courses")
        self.horizontalLayout_2.addWidget(self.btn_search_courses)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.TW_all_courses = QtWidgets.QTableWidget(parent=self.tab_home)
        self.TW_all_courses.setMaximumSize(QtCore.QSize(1010, 16777215))
        self.TW_all_courses.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.TW_all_courses.setColumnCount(4)
        headers = ['Название', 'Автор', 'Описание', 'Опубликован']
        self.TW_all_courses.setHorizontalHeaderLabels(headers)
        self.TW_all_courses.horizontalHeader().setDefaultSectionSize(248)
        self.TW_all_courses.setObjectName("TW_all_courses")
        self.TW_all_courses.setRowCount(0)
        self.TW_all_courses.cellClicked.connect(self.on_cell_clicked)

        self.horizontalLayout_6.addWidget(self.TW_all_courses)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 8)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("UI/icons/For Left bar/Домой.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.tabWidget.addTab(self.tab_home, icon1, "")
        self.show_courses_in_courses_tab()




    def create_tab_my_courses(self):

        self.tab_my_courses = QtWidgets.QWidget()
        self.tab_my_courses.setObjectName("tab_my_courses")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab_my_courses)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout_2.addItem(spacerItem1)
        self.label_2 = QtWidgets.QLabel(parent=self.tab_my_courses)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(50, 0, 50, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.TW_my_courses = QtWidgets.QTableWidget(parent=self.tab_my_courses)
        self.TW_my_courses.setColumnCount(4)
        self.TW_my_courses.setMaximumSize(QtCore.QSize(1010, 16777215))
        self.TW_my_courses.setObjectName("TW_my_courses")
        self.TW_my_courses.setRowCount(0)
        self.TW_my_courses.horizontalHeader().setVisible(True)
        self.TW_my_courses.horizontalHeader().setDefaultSectionSize(245)
        headers = ['Название', 'Автор', 'Описание', 'Опубликован']
        self.TW_my_courses.setHorizontalHeaderLabels(headers)
        self.verticalLayout_3.addWidget(self.TW_my_courses)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 10)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.show_courses_in_my_courses_tab()

        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("UI/icons/For Left bar/Курс.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.tabWidget.addTab(self.tab_my_courses, icon2, "")

    def create_tab_for_create_courses(self):
        self.tab_create_cource = QtWidgets.QWidget()
        self.tab_create_cource.setObjectName("tab_create_cource")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_create_cource)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.VL_tab_create_cource = QtWidgets.QVBoxLayout()
        self.VL_tab_create_cource.setObjectName("VL_tab_create_cource")
        spacerItem2 = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.VL_tab_create_cource.addItem(spacerItem2)
        self.label_3 = QtWidgets.QLabel(parent=self.tab_create_cource)

        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.VL_tab_create_cource.addWidget(self.label_3)
        self.HL_bottom_part = QtWidgets.QHBoxLayout()
        self.HL_bottom_part.setObjectName("HL_bottom_part")
        self.HL_left_bottom_part = QtWidgets.QVBoxLayout()
        self.HL_left_bottom_part.setObjectName("HL_left_bottom_part")
        self.label_4 = QtWidgets.QLabel(parent=self.tab_create_cource)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.HL_left_bottom_part.addWidget(self.label_4)
    # treeWidget
        self.treeWidget = QtWidgets.QTreeWidget(parent=self.tab_create_cource)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.treeWidget.setFont(font)
        self.treeWidget.setObjectName("treeWidget")

        self.HL_left_bottom_part.addWidget(self.treeWidget)

        self.treeWidget.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.treeWidget.customContextMenuRequested.connect(self.show_context_menu)

        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.btn_create_module = QtWidgets.QPushButton(parent=self.tab_create_cource)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_create_module.sizePolicy().hasHeightForWidth())
    # btn_create_module
        self.btn_create_module.setSizePolicy(sizePolicy)
        self.btn_create_module.setMinimumSize(QtCore.QSize(0, 0))
        self.btn_create_module.setObjectName("btn_create_module")
        self.horizontalLayout_8.addWidget(self.btn_create_module)
        self.btn_create_module.clicked.connect(self.create_module)
    # btn_create_lesson
        self.btn_create_lesson = QtWidgets.QPushButton(parent=self.tab_create_cource)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_create_lesson.sizePolicy().hasHeightForWidth())
        self.btn_create_lesson.setSizePolicy(sizePolicy)
        self.btn_create_lesson.setObjectName("btn_create_lesson")
        self.horizontalLayout_8.addWidget(self.btn_create_lesson)
        self.btn_create_lesson.clicked.connect(self.create_lesson)
    # btn_move_up
        self.btn_move_up = QtWidgets.QPushButton(parent=self.tab_create_cource)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_move_up.sizePolicy().hasHeightForWidth())
        self.btn_move_up.setSizePolicy(sizePolicy)
        self.btn_move_up.setObjectName("btn_move_up")
        self.horizontalLayout_8.addWidget(self.btn_move_up)
        self.btn_move_up.clicked.connect(self.move_up)
    # pbt_move_down
        self.pbt_move_down = QtWidgets.QPushButton(parent=self.tab_create_cource)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbt_move_down.sizePolicy().hasHeightForWidth())
        self.pbt_move_down.setSizePolicy(sizePolicy)
        self.pbt_move_down.setObjectName("pbt_move_down")
        self.horizontalLayout_8.addWidget(self.pbt_move_down)
        self.pbt_move_down.clicked.connect(self.move_down)
    # pbt_reference
        self.pbt_reference = QtWidgets.QPushButton(parent=self.tab_create_cource)
        self.pbt_reference.clicked.connect(self.show_reference)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbt_reference.sizePolicy().hasHeightForWidth())
        self.pbt_reference.setSizePolicy(sizePolicy)
        self.pbt_reference.setFlat(True)
        self.pbt_reference.setObjectName("pbt_reference")
        self.horizontalLayout_8.addWidget(self.pbt_reference)

        self.HL_left_bottom_part.addLayout(self.horizontalLayout_8)
        self.HL_bottom_part.addLayout(self.HL_left_bottom_part)
        self.HL_right_bottom_part = QtWidgets.QVBoxLayout()
        self.HL_right_bottom_part.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.HL_right_bottom_part.setSpacing(0)
        self.HL_right_bottom_part.setObjectName("HL_right_bottom_part")
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Maximum)
        self.HL_right_bottom_part.addItem(spacerItem3)
        self.label_5 = QtWidgets.QLabel(parent=self.tab_create_cource)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.HL_right_bottom_part.addWidget(self.label_5)
        self.PTE_course_name = QtWidgets.QPlainTextEdit(parent=self.tab_create_cource)
        self.PTE_course_name.setMaximumSize(QtCore.QSize(16777215, 50))
        self.PTE_course_name.setObjectName("PTE_course_name")
        self.HL_right_bottom_part.addWidget(self.PTE_course_name)
        spacerItem4 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Maximum)
        self.HL_right_bottom_part.addItem(spacerItem4)
        self.label_6 = QtWidgets.QLabel(parent=self.tab_create_cource)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.HL_right_bottom_part.addWidget(self.label_6)
        self.PTE_description_course = QtWidgets.QPlainTextEdit(parent=self.tab_create_cource)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PTE_description_course.sizePolicy().hasHeightForWidth())
        self.PTE_description_course.setSizePolicy(sizePolicy)
        self.PTE_description_course.setMinimumSize(QtCore.QSize(0, 200))
        self.PTE_description_course.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.PTE_description_course.setObjectName("PTE_description_course")
        self.HL_right_bottom_part.addWidget(self.PTE_description_course)

        self.label_10 = QtWidgets.QLabel(parent=self.tab_create_cource)
        self.label_10.setText("Уровень сложности")
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.HL_right_bottom_part.addWidget(self.label_10)
        self.cB_choose_complexity = QtWidgets.QComboBox(parent=self.tab_create_cource)
        self.cB_choose_complexity.setObjectName("cB_choose_complexity")
        self.cB_choose_complexity.addItem("Базовый")
        self.cB_choose_complexity.addItem("Средний")
        self.cB_choose_complexity.addItem("Продвинутый")
        self.HL_right_bottom_part.addWidget(self.cB_choose_complexity)

        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Maximum)
        self.HL_right_bottom_part.addItem(spacerItem5)
        self.btn_create_course = QtWidgets.QPushButton(parent=self.tab_create_cource)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_create_course.sizePolicy().hasHeightForWidth())
        self.btn_create_course.setSizePolicy(sizePolicy)
        self.btn_create_course.setMaximumSize(QtCore.QSize(16777215, 30))
        self.btn_create_course.setBaseSize(QtCore.QSize(0, 0))
        self.btn_create_course.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.btn_create_course.setAutoFillBackground(False)
        self.btn_create_course.setAutoDefault(False)
        self.btn_create_course.setDefault(False)
        self.btn_create_course.setObjectName("btn_create_course")
        self.btn_create_course.clicked.connect(self.create_course)

        self.HL_right_bottom_part.addWidget(self.btn_create_course)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Maximum)
        self.HL_right_bottom_part.addItem(spacerItem6)
        self.HL_right_bottom_part.setStretch(5, 5)
        self.HL_right_bottom_part.setStretch(6, 1)
        self.HL_bottom_part.addLayout(self.HL_right_bottom_part)
        self.HL_bottom_part.setStretch(0, 5)
        self.VL_tab_create_cource.addLayout(self.HL_bottom_part)
        self.verticalLayout_6.addLayout(self.VL_tab_create_cource)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("UI/icons/For Left bar/Создание курса.png"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.On)
        self.tabWidget.addTab(self.tab_create_cource, icon3, "")

    def create_tab_management_account(self):
        self.tab_my_students = QtWidgets.QWidget()
        self.tab_my_students.setObjectName("tab_my_students")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("UI/icons/For Left bar/Учетные записи.png"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.On)
        self.tabWidget.addTab(self.tab_my_students, icon4, "")

    def create_course(self):
        course_params = {
            'uid': int(self.LE_profileID.text()),
            'course_name': self.PTE_course_name.toPlainText(),
            'course_description': self.PTE_description_course.toPlainText(),
            'complexity': self.cB_choose_complexity.currentText(),
        }

        self.logic.create_course(self.treeWidget, course_params)
        self.clearing_the_course_creation_window()

    def create_module(self):
        self.logic.create_module(self.treeWidget)

    def create_lesson(self):
        self.logic.create_lesson(self.treeWidget)

    def move_up(self):
        self.logic.move_up(self.treeWidget)

    def move_down(self):
        self.logic.move_down(self.treeWidget)

    def show_reference(self):
        self.logic.show_reference()

    def show_courses_in_courses_tab(self):
        self.logic.show_courses_in_courses_tab(self.TW_all_courses)

    def show_courses_in_my_courses_tab(self):
        print("Зашёл в show_courses_in_my_courses_tab")
        uid = self.UID
        if uid:
            self.logic.show_courses_in_my_courses_tab(uid, self.TW_my_courses)

    def show_context_menu(self, item):
        self.logic.show_context_menu(self.treeWidget, item)

    def clearing_the_course_creation_window(self):
        self.logic.clearing_the_course_creation_window(self.treeWidget,
                                                       self.PTE_course_name,
                                                       self.PTE_description_course)

    def edit_user_name(self):
        new_name = self.LE_name.text()
        uid = self.UID
        if uid and new_name:
            self.logic.edit_user_name(uid, self.LE_name, new_name)
        self.logic.show_courses_in_courses_tab(self.TW_all_courses) # обновление записей в таблице, т.к. измененно имя

    def course_filter(self):
        '''Фильтрация курсов в таблице TW_all_courses'''
        ...

    def search_for_course(self):
        '''Функция поиска нужных курсов по названию'''
        data_in_search_bar = self.LE_search_string.text()
        ...

    def on_cell_clicked(self, row, col):
        self.logic.on_cell_clicked(self.TW_all_courses, row, col)


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec())
