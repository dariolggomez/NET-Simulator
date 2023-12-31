# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindowvaIHHt.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1090, 791)
        MainWindow.setStyleSheet(u"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(27, 29, 35, 160);\n"
"	border: 1px solid rgb(40, 40, 40);\n"
"	border-radius: 2px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background: transparent;\n"
"color: rgb(147, 148, 148);")
        self.central_widget_layout = QVBoxLayout(self.centralwidget)
        self.central_widget_layout.setSpacing(0)
        self.central_widget_layout.setObjectName(u"central_widget_layout")
        self.central_widget_layout.setContentsMargins(10, 10, 10, 10)
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setStyleSheet(u"/* LINE EDIT */\n"
"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* SCROLL BARS */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(0, 122, 204);\n"
"    min-width: 25px;\n"
"	border-radius: 7px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
""
                        "	border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(0, 122, 204);\n"
"    min-height: 25px;\n"
"	border-radius: 7px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63,"
                        " 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* CHECKBOX */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/16x16/icons/16x16/cil-check-alt.png);\n"
"}\n"
"\n"
"/* RADIO BUTTON */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius:"
                        " 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* COMBOBOX */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(8"
                        "5, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* SLIDERS */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 9px;\n"
"    height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 9px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertic"
                        "al {\n"
"    background-color: rgb(85, 170, 255);\n"
"	border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_main)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.frame_main)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMinimumSize(QSize(0, 65))
        self.frame_top.setMaximumSize(QSize(16777215, 65))
        self.frame_top.setStyleSheet(u"background-color: transparent;")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_top)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.frame_top)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 16777215))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(50, 50, 51);\n"
"border-top-left-radius: 10px;")
        self.frame_toggle.setFrameShape(QFrame.NoFrame)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_toggle_menu = QPushButton(self.frame_toggle)
        self.btn_toggle_menu.setObjectName(u"btn_toggle_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_toggle_menu.sizePolicy().hasHeightForWidth())
        self.btn_toggle_menu.setSizePolicy(sizePolicy)
        self.btn_toggle_menu.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/24x24/icons/24x24/cil-menu.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border: none;\n"
"	background-color: rgb(50, 50, 51);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(56, 56, 57);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(0, 122, 204);\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_toggle_menu)


        self.horizontalLayout.addWidget(self.frame_toggle)

        self.frame_top_right = QFrame(self.frame_top)
        self.frame_top_right.setObjectName(u"frame_top_right")
        self.frame_top_right.setStyleSheet(u"background: transparent;\n"
"")
        self.frame_top_right.setFrameShape(QFrame.NoFrame)
        self.frame_top_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_top_right)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_top_btns = QFrame(self.frame_top_right)
        self.frame_top_btns.setObjectName(u"frame_top_btns")
        self.frame_top_btns.setMaximumSize(QSize(16777215, 42))
        self.frame_top_btns.setStyleSheet(u"background-color: rgb(50, 50, 51);\n"
"border-top-right-radius: 10px;\n"
"")
        self.frame_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top_btns)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_label_top_btns = QFrame(self.frame_top_btns)
        self.frame_label_top_btns.setObjectName(u"frame_label_top_btns")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_label_top_btns.sizePolicy().hasHeightForWidth())
        self.frame_label_top_btns.setSizePolicy(sizePolicy1)
        self.frame_label_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_label_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_label_top_btns)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, 0, 10, 0)
        self.frame_icon_top_bar = QFrame(self.frame_label_top_btns)
        self.frame_icon_top_bar.setObjectName(u"frame_icon_top_bar")
        self.frame_icon_top_bar.setMaximumSize(QSize(30, 30))
        self.frame_icon_top_bar.setStyleSheet(u"background: transparent;\n"
"background-image: url(:/16x16/icons/16x16/cil-screen-desktop.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"")
        self.frame_icon_top_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_icon_top_bar.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.frame_icon_top_bar)

        self.label_title_bar_top = QLabel(self.frame_label_top_btns)
        self.label_title_bar_top.setObjectName(u"label_title_bar_top")
        font = QFont()
        font.setFamily(u"Segoe UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QFont.PreferAntialias)
        self.label_title_bar_top.setFont(font)
        self.label_title_bar_top.setStyleSheet(u"background: transparent;\n"
"")

        self.horizontalLayout_10.addWidget(self.label_title_bar_top)


        self.horizontalLayout_4.addWidget(self.frame_label_top_btns)

        self.frame_btns_right = QFrame(self.frame_top_btns)
        self.frame_btns_right.setObjectName(u"frame_btns_right")
        sizePolicy1.setHeightForWidth(self.frame_btns_right.sizePolicy().hasHeightForWidth())
        self.frame_btns_right.setSizePolicy(sizePolicy1)
        self.frame_btns_right.setMaximumSize(QSize(180, 16777215))
        self.frame_btns_right.setStyleSheet(u"")
        self.frame_btns_right.setFrameShape(QFrame.NoFrame)
        self.frame_btns_right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_btns_right)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_fullscreen = QPushButton(self.frame_btns_right)
        self.btn_fullscreen.setObjectName(u"btn_fullscreen")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_fullscreen.sizePolicy().hasHeightForWidth())
        self.btn_fullscreen.setSizePolicy(sizePolicy2)
        self.btn_fullscreen.setMinimumSize(QSize(40, 0))
        self.btn_fullscreen.setMaximumSize(QSize(40, 16777215))
        self.btn_fullscreen.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	border-top-right-radius: 0px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/20x20/icons/20x20/cil-fullscreen.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_fullscreen.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.btn_fullscreen)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.btn_minimize = QPushButton(self.frame_btns_right)
        self.btn_minimize.setObjectName(u"btn_minimize")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy3)
        self.btn_minimize.setMinimumSize(QSize(40, 0))
        self.btn_minimize.setMaximumSize(QSize(40, 16777215))
        self.btn_minimize.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	border-top-right-radius: 0px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/16x16/icons/16x16/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.btn_minimize)

        self.btn_maximize_restore = QPushButton(self.frame_btns_right)
        self.btn_maximize_restore.setObjectName(u"btn_maximize_restore")
        sizePolicy3.setHeightForWidth(self.btn_maximize_restore.sizePolicy().hasHeightForWidth())
        self.btn_maximize_restore.setSizePolicy(sizePolicy3)
        self.btn_maximize_restore.setMinimumSize(QSize(40, 0))
        self.btn_maximize_restore.setMaximumSize(QSize(40, 16777215))
        self.btn_maximize_restore.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	border-top-right-radius: 0px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/16x16/icons/16x16/cil-window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximize_restore.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.btn_maximize_restore)

        self.btn_close = QPushButton(self.frame_btns_right)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy3.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy3)
        self.btn_close.setMinimumSize(QSize(40, 0))
        self.btn_close.setMaximumSize(QSize(40, 16777215))
        self.btn_close.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 60, 63);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(217, 0, 0);\n"
"};\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/16x16/icons/16x16/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon3)

        self.horizontalLayout_5.addWidget(self.btn_close)


        self.horizontalLayout_4.addWidget(self.frame_btns_right, 0, Qt.AlignRight)


        self.verticalLayout_4.addWidget(self.frame_top_btns)

        self.frame_top_info = QFrame(self.frame_top_right)
        self.frame_top_info.setObjectName(u"frame_top_info")
        self.frame_top_info.setMaximumSize(QSize(16777215, 65))
        self.frame_top_info.setStyleSheet(u"background-color: rgb(37, 37, 38);")
        self.frame_top_info.setFrameShape(QFrame.NoFrame)
        self.frame_top_info.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_top_info)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(10, 0, 10, 0)
        self.label_top_info_1 = QLabel(self.frame_top_info)
        self.label_top_info_1.setObjectName(u"label_top_info_1")
        self.label_top_info_1.setMinimumSize(QSize(0, 20))
        self.label_top_info_1.setMaximumSize(QSize(16777215, 20))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        self.label_top_info_1.setFont(font1)
        self.label_top_info_1.setStyleSheet(u"color: rgb(98, 103, 111); ")
        self.label_top_info_1.setWordWrap(True)

        self.horizontalLayout_8.addWidget(self.label_top_info_1)

        self.label_top_info_2 = QLabel(self.frame_top_info)
        self.label_top_info_2.setObjectName(u"label_top_info_2")
        self.label_top_info_2.setMinimumSize(QSize(0, 0))
        self.label_top_info_2.setMaximumSize(QSize(250, 20))
        font2 = QFont()
        font2.setFamily(u"Segoe UI Semibold")
        font2.setBold(True)
        font2.setWeight(75)
        self.label_top_info_2.setFont(font2)
        self.label_top_info_2.setStyleSheet(u"color: rgb(0, 122, 204);")
        self.label_top_info_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_top_info_2)


        self.verticalLayout_4.addWidget(self.frame_top_info)


        self.horizontalLayout.addWidget(self.frame_top_right)


        self.verticalLayout_2.addWidget(self.frame_top)

        self.frame_center = QFrame(self.frame_main)
        self.frame_center.setObjectName(u"frame_center")
        self.frame_center.setStyleSheet(u"")
        self.frame_center.setFrameShape(QFrame.NoFrame)
        self.frame_center.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_center)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.frame_center)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_left_menu.sizePolicy().hasHeightForWidth())
        self.frame_left_menu.setSizePolicy(sizePolicy4)
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setLayoutDirection(Qt.LeftToRight)
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(50, 50, 51);")
        self.frame_left_menu.setFrameShape(QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_menus = QFrame(self.frame_left_menu)
        self.frame_menus.setObjectName(u"frame_menus")
        self.frame_menus.setFrameShape(QFrame.NoFrame)
        self.frame_menus.setFrameShadow(QFrame.Raised)
        self.layout_menus = QVBoxLayout(self.frame_menus)
        self.layout_menus.setSpacing(0)
        self.layout_menus.setObjectName(u"layout_menus")
        self.layout_menus.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_5.addWidget(self.frame_menus, 0, Qt.AlignTop)

        self.frame_extra_menus = QFrame(self.frame_left_menu)
        self.frame_extra_menus.setObjectName(u"frame_extra_menus")
        sizePolicy4.setHeightForWidth(self.frame_extra_menus.sizePolicy().hasHeightForWidth())
        self.frame_extra_menus.setSizePolicy(sizePolicy4)
        self.frame_extra_menus.setFrameShape(QFrame.NoFrame)
        self.frame_extra_menus.setFrameShadow(QFrame.Raised)
        self.layout_menu_bottom = QVBoxLayout(self.frame_extra_menus)
        self.layout_menu_bottom.setSpacing(10)
        self.layout_menu_bottom.setObjectName(u"layout_menu_bottom")
        self.layout_menu_bottom.setContentsMargins(0, 0, 0, 25)
        self.label_user_icon = QLabel(self.frame_extra_menus)
        self.label_user_icon.setObjectName(u"label_user_icon")
        sizePolicy5 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_user_icon.sizePolicy().hasHeightForWidth())
        self.label_user_icon.setSizePolicy(sizePolicy5)
        self.label_user_icon.setMinimumSize(QSize(60, 60))
        self.label_user_icon.setMaximumSize(QSize(60, 60))
        font3 = QFont()
        font3.setFamily(u"Segoe UI Semibold")
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_user_icon.setFont(font3)
        self.label_user_icon.setStyleSheet(u"QLabel {\n"
"	border-radius: 30px;\n"
"	background-color: rgb(30, 30, 30);\n"
"	border: 5px solid rgb(37, 37, 38);\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"}")
        self.label_user_icon.setAlignment(Qt.AlignCenter)

        self.layout_menu_bottom.addWidget(self.label_user_icon, 0, Qt.AlignHCenter)


        self.verticalLayout_5.addWidget(self.frame_extra_menus, 0, Qt.AlignBottom)


        self.horizontalLayout_3.addWidget(self.frame_left_menu)

        self.frame_content_right = QFrame(self.frame_center)
        self.frame_content_right.setObjectName(u"frame_content_right")
        self.frame_content_right.setStyleSheet(u"background-color: rgb(30, 30, 30);")
        self.frame_content_right.setFrameShape(QFrame.NoFrame)
        self.frame_content_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_content_right)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_content = QFrame(self.frame_content_right)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_content)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;\n"
"/*background-color: rgb(255, 255, 255);*/\n"
"color: rgb(210, 210, 210);")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout_10 = QVBoxLayout(self.page_home)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.page_home_content = QFrame(self.page_home)
        self.page_home_content.setObjectName(u"page_home_content")
        self.page_home_content.setFrameShape(QFrame.NoFrame)
        self.page_home_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.page_home_content)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.content_information = QFrame(self.page_home_content)
        self.content_information.setObjectName(u"content_information")
        self.content_information.setMaximumSize(QSize(16777215, 50))
        self.content_information.setStyleSheet(u"background-color: rgb(30, 30, 30);\n"
"border-radius: 0px;")
        self.content_information.setFrameShape(QFrame.NoFrame)
        self.content_information.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.content_information)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.net_node_in_use = QLabel(self.content_information)
        self.net_node_in_use.setObjectName(u"net_node_in_use")
        sizePolicy2.setHeightForWidth(self.net_node_in_use.sizePolicy().hasHeightForWidth())
        self.net_node_in_use.setSizePolicy(sizePolicy2)
        self.net_node_in_use.setMaximumSize(QSize(167777, 16777215))
        font4 = QFont()
        font4.setFamily(u"Segoe UI Semibold")
        font4.setPointSize(10)
        font4.setBold(True)
        font4.setWeight(75)
        self.net_node_in_use.setFont(font4)
        self.net_node_in_use.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.net_node_in_use.setWordWrap(True)

        self.horizontalLayout_11.addWidget(self.net_node_in_use)

        self.horizontalSpacer_6 = QSpacerItem(360, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_6)

        self.city_label = QLabel(self.content_information)
        self.city_label.setObjectName(u"city_label")
        self.city_label.setMaximumSize(QSize(105, 16777215))
        self.city_label.setFont(font4)
        self.city_label.setStyleSheet(u"")

        self.horizontalLayout_11.addWidget(self.city_label)

        self.net_node_city = QLabel(self.content_information)
        self.net_node_city.setObjectName(u"net_node_city")
        sizePolicy4.setHeightForWidth(self.net_node_city.sizePolicy().hasHeightForWidth())
        self.net_node_city.setSizePolicy(sizePolicy4)
        self.net_node_city.setMinimumSize(QSize(150, 0))
        self.net_node_city.setMaximumSize(QSize(200, 16777215))
        self.net_node_city.setFont(font4)
        self.net_node_city.setLayoutDirection(Qt.RightToLeft)
        self.net_node_city.setAlignment(Qt.AlignCenter)
        self.net_node_city.setWordWrap(True)

        self.horizontalLayout_11.addWidget(self.net_node_city)


        self.verticalLayout_18.addWidget(self.content_information)

        self.frame_4 = QFrame(self.page_home_content)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_4)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_table_header = QFrame(self.frame_4)
        self.frame_table_header.setObjectName(u"frame_table_header")
        self.frame_table_header.setMaximumSize(QSize(16777215, 50))
        self.frame_table_header.setStyleSheet(u"background-color: rgb(30, 30, 30);\n"
"border-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"border-bottom-right-radius: 0px;")
        self.frame_table_header.setFrameShape(QFrame.NoFrame)
        self.frame_table_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_table_header)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_table_info = QLabel(self.frame_table_header)
        self.label_table_info.setObjectName(u"label_table_info")
        self.label_table_info.setFont(font4)
        self.label_table_info.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_table_info)


        self.verticalLayout.addWidget(self.frame_table_header)

        self.frame_table = QFrame(self.frame_4)
        self.frame_table.setObjectName(u"frame_table")
        self.frame_table.setFrameShape(QFrame.NoFrame)
        self.frame_table.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_table)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.rtNodeStatusTable = QTableWidget(self.frame_table)
        self.rtNodeStatusTable.setObjectName(u"rtNodeStatusTable")
        self.rtNodeStatusTable.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.rtNodeStatusTable.sizePolicy().hasHeightForWidth())
        self.rtNodeStatusTable.setSizePolicy(sizePolicy4)
        self.rtNodeStatusTable.setMaximumSize(QSize(99999, 1000))
        palette = QPalette()
        brush = QBrush(QColor(210, 210, 210, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(30, 30, 30, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(210, 210, 210, 128))
        brush2.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush3 = QBrush(QColor(210, 210, 210, 128))
        brush3.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush4 = QBrush(QColor(210, 210, 210, 128))
        brush4.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.rtNodeStatusTable.setPalette(palette)
        self.rtNodeStatusTable.setFocusPolicy(Qt.NoFocus)
        self.rtNodeStatusTable.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(30, 30, 30);\n"
"	padding: 10px;\n"
"	border-radius: 0px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	/*border-bottom: 1px solid rgb(44, 49, 60);*/\n"
"	border-top-left-radius: 0px;\n"
"	border-top-right-radius: 0px;\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(50, 50, 51);\n"
"	color: rgb(219, 219, 219);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
""
                        "    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(30,30,30);\n"
"	background-color: rgb(0, 122, 204);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(0, 122, 204);\n"
"}\n"
"")
        self.rtNodeStatusTable.setFrameShape(QFrame.NoFrame)
        self.rtNodeStatusTable.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.rtNodeStatusTable.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.rtNodeStatusTable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.rtNodeStatusTable.setAutoScroll(True)
        self.rtNodeStatusTable.setAutoScrollMargin(16)
        self.rtNodeStatusTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.rtNodeStatusTable.setAlternatingRowColors(False)
        self.rtNodeStatusTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.rtNodeStatusTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.rtNodeStatusTable.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.rtNodeStatusTable.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.rtNodeStatusTable.setShowGrid(True)
        self.rtNodeStatusTable.setGridStyle(Qt.SolidLine)
        self.rtNodeStatusTable.setSortingEnabled(True)
        self.rtNodeStatusTable.setWordWrap(True)
        self.rtNodeStatusTable.setRowCount(0)
        self.rtNodeStatusTable.horizontalHeader().setVisible(False)
        self.rtNodeStatusTable.horizontalHeader().setCascadingSectionResizes(False)
        self.rtNodeStatusTable.horizontalHeader().setDefaultSectionSize(200)
        self.rtNodeStatusTable.horizontalHeader().setStretchLastSection(True)
        self.rtNodeStatusTable.verticalHeader().setVisible(False)
        self.rtNodeStatusTable.verticalHeader().setCascadingSectionResizes(False)
        self.rtNodeStatusTable.verticalHeader().setMinimumSectionSize(30)
        self.rtNodeStatusTable.verticalHeader().setDefaultSectionSize(30)
        self.rtNodeStatusTable.verticalHeader().setHighlightSections(False)
        self.rtNodeStatusTable.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_17.addWidget(self.rtNodeStatusTable)


        self.verticalLayout.addWidget(self.frame_table)

        self.frame_2 = QFrame(self.frame_4)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 50))
        self.frame_2.setStyleSheet(u"background-color: rgb(37, 37, 38);")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalSpacer_7 = QSpacerItem(729, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_7)

        self.disconnect_btn = QPushButton(self.frame_2)
        self.disconnect_btn.setObjectName(u"disconnect_btn")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.disconnect_btn.sizePolicy().hasHeightForWidth())
        self.disconnect_btn.setSizePolicy(sizePolicy6)
        self.disconnect_btn.setMinimumSize(QSize(105, 30))
        font5 = QFont()
        font5.setFamily(u"Segoe UI Semibold")
        font5.setPointSize(9)
        font5.setBold(True)
        font5.setWeight(75)
        self.disconnect_btn.setFont(font5)
        self.disconnect_btn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(50, 50, 51);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(50, 50, 51);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(56, 56, 57);\n"
"	border: 2px solid rgb(56, 56, 57);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(56, 56, 57);\n"
"	border: 1px solid rgb(0, 122, 204);\n"
"}")

        self.horizontalLayout_15.addWidget(self.disconnect_btn)

        self.connect_btn = QPushButton(self.frame_2)
        self.connect_btn.setObjectName(u"connect_btn")
        self.connect_btn.setMinimumSize(QSize(80, 30))
        self.connect_btn.setFont(font5)
        self.connect_btn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(50, 50, 51);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(50, 50, 51);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(56, 56, 57);\n"
"	border: 2px solid rgb(56, 56, 57);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(56, 56, 57);\n"
"	border: 1px solid rgb(0, 122, 204);\n"
"}")

        self.horizontalLayout_15.addWidget(self.connect_btn)


        self.verticalLayout.addWidget(self.frame_2)


        self.verticalLayout_18.addWidget(self.frame_4)


        self.verticalLayout_10.addWidget(self.page_home_content)

        self.stackedWidget.addWidget(self.page_home)
        self.page_rt_nodes = QWidget()
        self.page_rt_nodes.setObjectName(u"page_rt_nodes")
        self.verticalLayout_19 = QVBoxLayout(self.page_rt_nodes)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.page_rt_content = QFrame(self.page_rt_nodes)
        self.page_rt_content.setObjectName(u"page_rt_content")
        self.page_rt_content.setFrameShape(QFrame.NoFrame)
        self.page_rt_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.page_rt_content)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.page_rt_content)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 50))
        self.frame_3.setStyleSheet(u"background-color: rgb(30, 30, 30);")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(12, 0, 0, 0)
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setFont(font4)

        self.horizontalLayout_17.addWidget(self.label)


        self.verticalLayout_20.addWidget(self.frame_3)

        self.frame_5 = QFrame(self.page_rt_content)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_5)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.rtNodeManagementTable = QTableWidget(self.frame_5)
        self.rtNodeManagementTable.setObjectName(u"rtNodeManagementTable")
        self.rtNodeManagementTable.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.rtNodeManagementTable.sizePolicy().hasHeightForWidth())
        self.rtNodeManagementTable.setSizePolicy(sizePolicy4)
        self.rtNodeManagementTable.setMaximumSize(QSize(99999, 1000))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush5 = QBrush(QColor(210, 210, 210, 128))
        brush5.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush6 = QBrush(QColor(210, 210, 210, 128))
        brush6.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush7 = QBrush(QColor(210, 210, 210, 128))
        brush7.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.rtNodeManagementTable.setPalette(palette1)
        self.rtNodeManagementTable.setFocusPolicy(Qt.NoFocus)
        self.rtNodeManagementTable.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(30, 30, 30);\n"
"	padding: 10px;\n"
"	border-radius: 0px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	/*border-bottom: 1px solid rgb(44, 49, 60);*/\n"
"	border-top-left-radius: 0px;\n"
"	border-top-right-radius: 0px;\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(50, 50, 51);\n"
"	color: rgb(219, 219, 219);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
""
                        "    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(30,30,30);\n"
"	background-color: rgb(0, 122, 204);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(0, 122, 204);\n"
"}\n"
"")
        self.rtNodeManagementTable.setFrameShape(QFrame.NoFrame)
        self.rtNodeManagementTable.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.rtNodeManagementTable.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.rtNodeManagementTable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.rtNodeManagementTable.setAutoScroll(True)
        self.rtNodeManagementTable.setAutoScrollMargin(16)
        self.rtNodeManagementTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.rtNodeManagementTable.setAlternatingRowColors(False)
        self.rtNodeManagementTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.rtNodeManagementTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.rtNodeManagementTable.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.rtNodeManagementTable.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.rtNodeManagementTable.setShowGrid(True)
        self.rtNodeManagementTable.setGridStyle(Qt.SolidLine)
        self.rtNodeManagementTable.setSortingEnabled(True)
        self.rtNodeManagementTable.setWordWrap(True)
        self.rtNodeManagementTable.setRowCount(0)
        self.rtNodeManagementTable.horizontalHeader().setVisible(False)
        self.rtNodeManagementTable.horizontalHeader().setCascadingSectionResizes(False)
        self.rtNodeManagementTable.horizontalHeader().setDefaultSectionSize(200)
        self.rtNodeManagementTable.horizontalHeader().setStretchLastSection(True)
        self.rtNodeManagementTable.verticalHeader().setVisible(False)
        self.rtNodeManagementTable.verticalHeader().setCascadingSectionResizes(False)
        self.rtNodeManagementTable.verticalHeader().setMinimumSectionSize(30)
        self.rtNodeManagementTable.verticalHeader().setDefaultSectionSize(30)
        self.rtNodeManagementTable.verticalHeader().setHighlightSections(False)
        self.rtNodeManagementTable.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_26.addWidget(self.rtNodeManagementTable)


        self.verticalLayout_20.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.page_rt_content)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 50))
        self.frame_6.setStyleSheet(u"background-color: rgb(37, 37, 38);")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_16.setSpacing(8)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(12, 12, 12, 12)
        self.horizontalSpacer_8 = QSpacerItem(751, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_8)

        self.edit_rtnode_btn = QPushButton(self.frame_6)
        self.edit_rtnode_btn.setObjectName(u"edit_rtnode_btn")
        self.edit_rtnode_btn.setMinimumSize(QSize(65, 30))
        self.edit_rtnode_btn.setFont(font4)
        self.edit_rtnode_btn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(50, 50, 51);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(50, 50, 51);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(56, 56, 57);\n"
"	border: 2px solid rgb(56, 56, 57);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(56, 56, 57);\n"
"	border: 1px solid rgb(0, 122, 204);\n"
"}")

        self.horizontalLayout_16.addWidget(self.edit_rtnode_btn)

        self.create_rtnode_btn = QPushButton(self.frame_6)
        self.create_rtnode_btn.setObjectName(u"create_rtnode_btn")
        self.create_rtnode_btn.setMinimumSize(QSize(60, 30))
        self.create_rtnode_btn.setFont(font4)
        self.create_rtnode_btn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(50, 50, 51);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(50, 50, 51);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(56, 56, 57);\n"
"	border: 2px solid rgb(56, 56, 57);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(56, 56, 57);\n"
"	border: 1px solid rgb(0, 122, 204);\n"
"}")

        self.horizontalLayout_16.addWidget(self.create_rtnode_btn)

        self.delete_rtnode_btn = QPushButton(self.frame_6)
        self.delete_rtnode_btn.setObjectName(u"delete_rtnode_btn")
        self.delete_rtnode_btn.setMinimumSize(QSize(85, 30))
        self.delete_rtnode_btn.setFont(font4)
        self.delete_rtnode_btn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(50, 50, 51);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(50, 50, 51);\n"
"	color: rgb(255, 84, 87);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(193, 59, 59);\n"
"	border: 1px solid rgb(193, 59, 59);\n"
"	color: rgb(210, 210, 210);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(220, 67, 67);\n"
"	border: 1px solid rgb(220, 67, 67);\n"
"}")

        self.horizontalLayout_16.addWidget(self.delete_rtnode_btn)


        self.verticalLayout_20.addWidget(self.frame_6)


        self.verticalLayout_19.addWidget(self.page_rt_content)

        self.stackedWidget.addWidget(self.page_rt_nodes)
        self.page_rt_graphics = QWidget()
        self.page_rt_graphics.setObjectName(u"page_rt_graphics")
        self.verticalLayout_27 = QVBoxLayout(self.page_rt_graphics)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.rt_graphics_content = QFrame(self.page_rt_graphics)
        self.rt_graphics_content.setObjectName(u"rt_graphics_content")
        self.rt_graphics_content.setFrameShape(QFrame.StyledPanel)
        self.rt_graphics_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.rt_graphics_content)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.upsideGraphics = QFrame(self.rt_graphics_content)
        self.upsideGraphics.setObjectName(u"upsideGraphics")
        self.upsideGraphics.setFrameShape(QFrame.StyledPanel)
        self.upsideGraphics.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.upsideGraphics)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frame_waveform = QFrame(self.upsideGraphics)
        self.frame_waveform.setObjectName(u"frame_waveform")
        self.frame_waveform.setFrameShape(QFrame.StyledPanel)
        self.frame_waveform.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_waveform)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.waveform_layout = QVBoxLayout()
        self.waveform_layout.setObjectName(u"waveform_layout")

        self.verticalLayout_31.addLayout(self.waveform_layout)


        self.horizontalLayout_18.addWidget(self.frame_waveform)

        self.frame_fft_transform = QFrame(self.upsideGraphics)
        self.frame_fft_transform.setObjectName(u"frame_fft_transform")
        self.frame_fft_transform.setFrameShape(QFrame.StyledPanel)
        self.frame_fft_transform.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_fft_transform)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.fft_transform_layout = QVBoxLayout()
        self.fft_transform_layout.setObjectName(u"fft_transform_layout")

        self.verticalLayout_34.addLayout(self.fft_transform_layout)


        self.horizontalLayout_18.addWidget(self.frame_fft_transform)


        self.verticalLayout_28.addWidget(self.upsideGraphics)

        self.downsideGraphics = QFrame(self.rt_graphics_content)
        self.downsideGraphics.setObjectName(u"downsideGraphics")
        self.downsideGraphics.setFrameShape(QFrame.StyledPanel)
        self.downsideGraphics.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.downsideGraphics)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.spectrogram_frame = QFrame(self.downsideGraphics)
        self.spectrogram_frame.setObjectName(u"spectrogram_frame")
        self.spectrogram_frame.setFrameShape(QFrame.StyledPanel)
        self.spectrogram_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.spectrogram_frame)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.spectrogram_layout = QHBoxLayout()
        self.spectrogram_layout.setObjectName(u"spectrogram_layout")

        self.verticalLayout_30.addLayout(self.spectrogram_layout)


        self.horizontalLayout_19.addWidget(self.spectrogram_frame)

        self.frame_interactions_btns = QFrame(self.downsideGraphics)
        self.frame_interactions_btns.setObjectName(u"frame_interactions_btns")
        self.frame_interactions_btns.setMaximumSize(QSize(200, 16777215))
        self.frame_interactions_btns.setFrameShape(QFrame.NoFrame)
        self.frame_interactions_btns.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_interactions_btns)
        self.verticalLayout_29.setSpacing(2)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(-1, 0, -1, 30)
        self.label_receptor = QLabel(self.frame_interactions_btns)
        self.label_receptor.setObjectName(u"label_receptor")
        self.label_receptor.setMaximumSize(QSize(16777215, 25))
        self.label_receptor.setFont(font4)

        self.verticalLayout_29.addWidget(self.label_receptor)

        self.input_devices = QComboBox(self.frame_interactions_btns)
        self.input_devices.setObjectName(u"input_devices")

        self.verticalLayout_29.addWidget(self.input_devices)

        self.start_btn = QPushButton(self.frame_interactions_btns)
        self.start_btn.setObjectName(u"start_btn")
        self.start_btn.setMinimumSize(QSize(65, 30))
        self.start_btn.setFont(font4)
        self.start_btn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(50, 50, 51);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(50, 50, 51);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(56, 56, 57);\n"
"	border: 2px solid rgb(56, 56, 57);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(56, 56, 57);\n"
"	border: 1px solid rgb(0, 122, 204);\n"
"}")

        self.verticalLayout_29.addWidget(self.start_btn)

        self.stop_btn = QPushButton(self.frame_interactions_btns)
        self.stop_btn.setObjectName(u"stop_btn")
        self.stop_btn.setMinimumSize(QSize(65, 30))
        self.stop_btn.setFont(font4)
        self.stop_btn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(50, 50, 51);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(50, 50, 51);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(56, 56, 57);\n"
"	border: 2px solid rgb(56, 56, 57);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(56, 56, 57);\n"
"	border: 1px solid rgb(0, 122, 204);\n"
"}")

        self.verticalLayout_29.addWidget(self.stop_btn)


        self.horizontalLayout_19.addWidget(self.frame_interactions_btns)


        self.verticalLayout_28.addWidget(self.downsideGraphics)


        self.verticalLayout_27.addWidget(self.rt_graphics_content)

        self.stackedWidget.addWidget(self.page_rt_graphics)
        self.page_users = QWidget()
        self.page_users.setObjectName(u"page_users")
        self.verticalLayout_16 = QVBoxLayout(self.page_users)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.page_users)
        self.content.setObjectName(u"content")
        self.content.setStyleSheet(u"")
        self.content.setFrameShape(QFrame.StyledPanel)
        self.content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.content)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_9 = QFrame(self.content)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_9)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.labelHeaderUser = QLabel(self.frame_9)
        self.labelHeaderUser.setObjectName(u"labelHeaderUser")
        self.labelHeaderUser.setMaximumSize(QSize(16777215, 25))
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(10)
        font6.setBold(True)
        font6.setWeight(75)
        self.labelHeaderUser.setFont(font6)
        self.labelHeaderUser.setStyleSheet(u"")

        self.verticalLayout_13.addWidget(self.labelHeaderUser)

        self.userTableWidget = QTableWidget(self.frame_9)
        self.userTableWidget.setObjectName(u"userTableWidget")
        self.userTableWidget.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.userTableWidget.sizePolicy().hasHeightForWidth())
        self.userTableWidget.setSizePolicy(sizePolicy4)
        self.userTableWidget.setMaximumSize(QSize(99999, 1000))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush8 = QBrush(QColor(39, 44, 54, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush8)
        brush9 = QBrush(QColor(210, 210, 210, 128))
        brush9.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush8)
        brush10 = QBrush(QColor(210, 210, 210, 128))
        brush10.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush10)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush8)
        brush11 = QBrush(QColor(210, 210, 210, 128))
        brush11.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        self.userTableWidget.setPalette(palette2)
        self.userTableWidget.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
""
                        "QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        self.userTableWidget.setFrameShape(QFrame.NoFrame)
        self.userTableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.userTableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.userTableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.userTableWidget.setAutoScroll(True)
        self.userTableWidget.setAutoScrollMargin(16)
        self.userTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.userTableWidget.setAlternatingRowColors(False)
        self.userTableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.userTableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.userTableWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.userTableWidget.setShowGrid(True)
        self.userTableWidget.setGridStyle(Qt.SolidLine)
        self.userTableWidget.setSortingEnabled(False)
        self.userTableWidget.setWordWrap(True)
        self.userTableWidget.setRowCount(0)
        self.userTableWidget.horizontalHeader().setVisible(False)
        self.userTableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.userTableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.userTableWidget.horizontalHeader().setStretchLastSection(True)
        self.userTableWidget.verticalHeader().setVisible(False)
        self.userTableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.userTableWidget.verticalHeader().setMinimumSectionSize(30)
        self.userTableWidget.verticalHeader().setDefaultSectionSize(30)
        self.userTableWidget.verticalHeader().setHighlightSections(False)
        self.userTableWidget.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_13.addWidget(self.userTableWidget)

        self.verticalLayout_13.setStretch(0, 5)

        self.verticalLayout_12.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.content)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(351, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.editBtn = QPushButton(self.frame_10)
        self.editBtn.setObjectName(u"editBtn")
        self.editBtn.setMinimumSize(QSize(80, 30))
        font7 = QFont()
        font7.setPointSize(9)
        self.editBtn.setFont(font7)
        self.editBtn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")

        self.horizontalLayout_2.addWidget(self.editBtn)

        self.createBtn = QPushButton(self.frame_10)
        self.createBtn.setObjectName(u"createBtn")
        self.createBtn.setMinimumSize(QSize(80, 30))
        self.createBtn.setFont(font7)
        self.createBtn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")

        self.horizontalLayout_2.addWidget(self.createBtn)

        self.eliminateBtn = QPushButton(self.frame_10)
        self.eliminateBtn.setObjectName(u"eliminateBtn")
        self.eliminateBtn.setEnabled(True)
        self.eliminateBtn.setMinimumSize(QSize(80, 30))
        self.eliminateBtn.setFont(font7)
        self.eliminateBtn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")

        self.horizontalLayout_2.addWidget(self.eliminateBtn)


        self.verticalLayout_12.addWidget(self.frame_10)


        self.verticalLayout_16.addWidget(self.content)

        self.stackedWidget.addWidget(self.page_users)
        self.page_widgets = QWidget()
        self.page_widgets.setObjectName(u"page_widgets")
        self.verticalLayout_7 = QVBoxLayout(self.page_widgets)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame = QFrame(self.page_widgets)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"border-radius: 5px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_1 = QFrame(self.frame)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;\n"
"")
        self.frame_div_content_1.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_title_wid_1.setObjectName(u"frame_title_wid_1")
        self.frame_title_wid_1.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_1.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_title_wid_1.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_title_wid_1)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(-1, 0, -1, 0)
        self.labelBoxHeaderSettings = QLabel(self.frame_title_wid_1)
        self.labelBoxHeaderSettings.setObjectName(u"labelBoxHeaderSettings")
        self.labelBoxHeaderSettings.setMinimumSize(QSize(0, 20))
        self.labelBoxHeaderSettings.setMaximumSize(QSize(16777215, 25))
        self.labelBoxHeaderSettings.setFont(font6)
        self.labelBoxHeaderSettings.setStyleSheet(u"")
        self.labelBoxHeaderSettings.setWordWrap(True)

        self.verticalLayout_14.addWidget(self.labelBoxHeaderSettings)


        self.verticalLayout_8.addWidget(self.frame_title_wid_1)

        self.frame_content_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.btn_settings_fullscreen = QPushButton(self.frame_content_wid_1)
        self.btn_settings_fullscreen.setObjectName(u"btn_settings_fullscreen")
        self.btn_settings_fullscreen.setMinimumSize(QSize(200, 30))
        font8 = QFont()
        font8.setFamily(u"Segoe UI")
        font8.setPointSize(9)
        self.btn_settings_fullscreen.setFont(font8)
        self.btn_settings_fullscreen.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")

        self.horizontalLayout_9.addWidget(self.btn_settings_fullscreen)

        self.backupCheckBox = QCheckBox(self.frame_content_wid_1)
        self.backupCheckBox.setObjectName(u"backupCheckBox")
        self.backupCheckBox.setAutoFillBackground(False)
        self.backupCheckBox.setStyleSheet(u"")

        self.horizontalLayout_9.addWidget(self.backupCheckBox)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_5)


        self.verticalLayout_8.addWidget(self.frame_content_wid_1)


        self.verticalLayout_11.addWidget(self.frame_div_content_1)


        self.verticalLayout_7.addWidget(self.frame)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_3)

        self.stackedWidget.addWidget(self.page_widgets)
        self.page_network = QWidget()
        self.page_network.setObjectName(u"page_network")
        self.verticalLayout_22 = QVBoxLayout(self.page_network)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.content_network = QFrame(self.page_network)
        self.content_network.setObjectName(u"content_network")
        self.content_network.setStyleSheet(u"")
        self.content_network.setFrameShape(QFrame.StyledPanel)
        self.content_network.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.content_network)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_network_1 = QFrame(self.content_network)
        self.frame_network_1.setObjectName(u"frame_network_1")
        self.frame_network_1.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;")
        self.frame_network_1.setFrameShape(QFrame.StyledPanel)
        self.frame_network_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_network_1)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.labelHeaderUser_2 = QLabel(self.frame_network_1)
        self.labelHeaderUser_2.setObjectName(u"labelHeaderUser_2")
        self.labelHeaderUser_2.setMaximumSize(QSize(16777215, 30))
        font9 = QFont()
        font9.setFamily(u"Segoe UI")
        font9.setPointSize(12)
        font9.setBold(True)
        font9.setWeight(75)
        self.labelHeaderUser_2.setFont(font9)
        self.labelHeaderUser_2.setStyleSheet(u"")

        self.verticalLayout_24.addWidget(self.labelHeaderUser_2)

        self.frame_11 = QFrame(self.frame_network_1)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.frame_12 = QFrame(self.frame_11)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_12)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.labelHeaderUser_3 = QLabel(self.frame_12)
        self.labelHeaderUser_3.setObjectName(u"labelHeaderUser_3")
        self.labelHeaderUser_3.setMaximumSize(QSize(16777215, 25))
        font10 = QFont()
        font10.setFamily(u"Segoe UI")
        font10.setPointSize(9)
        font10.setBold(True)
        font10.setWeight(75)
        self.labelHeaderUser_3.setFont(font10)
        self.labelHeaderUser_3.setStyleSheet(u"")

        self.verticalLayout_21.addWidget(self.labelHeaderUser_3)

        self.hostLineEdit = QLineEdit(self.frame_12)
        self.hostLineEdit.setObjectName(u"hostLineEdit")
        self.hostLineEdit.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.verticalLayout_21.addWidget(self.hostLineEdit)

        self.verticalSpacer = QSpacerItem(20, 331, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer)


        self.horizontalLayout_14.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.frame_11)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_13)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.labelHeaderUser_4 = QLabel(self.frame_13)
        self.labelHeaderUser_4.setObjectName(u"labelHeaderUser_4")
        self.labelHeaderUser_4.setMaximumSize(QSize(16777215, 25))
        self.labelHeaderUser_4.setFont(font10)
        self.labelHeaderUser_4.setStyleSheet(u"")

        self.verticalLayout_23.addWidget(self.labelHeaderUser_4)

        self.hostPortLineEdit = QLineEdit(self.frame_13)
        self.hostPortLineEdit.setObjectName(u"hostPortLineEdit")
        self.hostPortLineEdit.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.hostPortLineEdit.setInputMethodHints(Qt.ImhNone)

        self.verticalLayout_23.addWidget(self.hostPortLineEdit)

        self.verticalSpacer_2 = QSpacerItem(20, 331, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_23.addItem(self.verticalSpacer_2)


        self.horizontalLayout_14.addWidget(self.frame_13)

        self.horizontalSpacer_3 = QSpacerItem(256, 38, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_3)


        self.verticalLayout_24.addWidget(self.frame_11)


        self.verticalLayout_15.addWidget(self.frame_network_1)

        self.frame_network_2 = QFrame(self.content_network)
        self.frame_network_2.setObjectName(u"frame_network_2")
        self.frame_network_2.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;")
        self.frame_network_2.setFrameShape(QFrame.StyledPanel)
        self.frame_network_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_network_2)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_2 = QSpacerItem(351, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_2)

        self.connectBtn = QPushButton(self.frame_network_2)
        self.connectBtn.setObjectName(u"connectBtn")
        self.connectBtn.setEnabled(True)
        self.connectBtn.setMinimumSize(QSize(80, 30))
        self.connectBtn.setFont(font7)
        self.connectBtn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")

        self.horizontalLayout_13.addWidget(self.connectBtn)


        self.verticalLayout_15.addWidget(self.frame_network_2)


        self.verticalLayout_22.addWidget(self.content_network)

        self.stackedWidget.addWidget(self.page_network)

        self.verticalLayout_9.addWidget(self.stackedWidget)


        self.verticalLayout_6.addWidget(self.frame_content)

        self.frame_console = QFrame(self.frame_content_right)
        self.frame_console.setObjectName(u"frame_console")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.frame_console.sizePolicy().hasHeightForWidth())
        self.frame_console.setSizePolicy(sizePolicy7)
        self.frame_console.setMinimumSize(QSize(0, 130))
        self.frame_console.setMaximumSize(QSize(16777215, 150))
        self.frame_console.setStyleSheet(u"color: rgb(210, 210, 210);")
        self.frame_console.setFrameShape(QFrame.NoFrame)
        self.frame_console.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_console)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.console = QPlainTextEdit(self.frame_console)
        self.console.setObjectName(u"console")
        sizePolicy8 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Ignored)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.console.sizePolicy().hasHeightForWidth())
        self.console.setSizePolicy(sizePolicy8)
        self.console.setMinimumSize(QSize(0, 0))
        font11 = QFont()
        font11.setFamily(u"Cascadia Code")
        font11.setPointSize(10)
        self.console.setFont(font11)
        self.console.setFocusPolicy(Qt.NoFocus)
        self.console.setStyleSheet(u"QPlainTextEdit {\n"
"	background-color: rgb(30, 30, 30);\n"
"	border-radius: 0px;\n"
"	padding: 10px;\n"
"}\n"
"QPlainTextEdit:hover {\n"
"	border-top: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border-top: 2px solid rgb(91, 101, 124);\n"
"}")
        self.console.setFrameShape(QFrame.NoFrame)
        self.console.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.console.setReadOnly(True)
        self.console.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_25.addWidget(self.console)


        self.verticalLayout_6.addWidget(self.frame_console)


        self.horizontalLayout_3.addWidget(self.frame_content_right)


        self.verticalLayout_2.addWidget(self.frame_center)

        self.frame_grip = QFrame(self.frame_main)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(0, 25))
        self.frame_grip.setMaximumSize(QSize(16777215, 25))
        self.frame_grip.setStyleSheet(u"background-color: rgb(0, 122, 204);\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;")
        self.frame_grip.setFrameShape(QFrame.NoFrame)
        self.frame_grip.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_grip)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 2, 0)
        self.frame_label_bottom = QFrame(self.frame_grip)
        self.frame_label_bottom.setObjectName(u"frame_label_bottom")
        self.frame_label_bottom.setStyleSheet(u"color: rgb(210, 210, 210);")
        self.frame_label_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_label_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_label_bottom)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 0, 10, 0)
        self.label_credits = QLabel(self.frame_label_bottom)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setFont(font1)
        self.label_credits.setStyleSheet(u"")

        self.horizontalLayout_7.addWidget(self.label_credits)

        self.label_version = QLabel(self.frame_label_bottom)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setMaximumSize(QSize(100, 16777215))
        font12 = QFont()
        font12.setFamily(u"Segoe UI")
        font12.setPointSize(8)
        font12.setBold(True)
        font12.setWeight(75)
        self.label_version.setFont(font12)
        self.label_version.setStyleSheet(u"")
        self.label_version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_version)


        self.horizontalLayout_6.addWidget(self.frame_label_bottom)

        self.frame_size_grip = QFrame(self.frame_grip)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMaximumSize(QSize(20, 20))
        self.frame_size_grip.setStyleSheet(u"QSizeGrip {\n"
"	background-image: url(:/16x16/icons/16x16/cil-size-grip.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_size_grip)


        self.verticalLayout_2.addWidget(self.frame_grip)


        self.central_widget_layout.addWidget(self.frame_main)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_toggle_menu.setText("")
        self.label_title_bar_top.setText(QCoreApplication.translate("MainWindow", u"Main Window", None))
#if QT_CONFIG(tooltip)
        self.btn_fullscreen.setToolTip(QCoreApplication.translate("MainWindow", u"Pantalla Completa", None))
#endif // QT_CONFIG(tooltip)
        self.btn_fullscreen.setText("")
#if QT_CONFIG(shortcut)
        self.btn_fullscreen.setShortcut(QCoreApplication.translate("MainWindow", u"F11", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimizar", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_maximize_restore.setToolTip(QCoreApplication.translate("MainWindow", u"Maximizar", None))
#endif // QT_CONFIG(tooltip)
        self.btn_maximize_restore.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Cerrar", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.label_top_info_1.setText("")
        self.label_top_info_2.setText(QCoreApplication.translate("MainWindow", u"| INICIO", None))
        self.label_user_icon.setText(QCoreApplication.translate("MainWindow", u"NET", None))
        self.net_node_in_use.setText(QCoreApplication.translate("MainWindow", u"Nodo en uso", None))
        self.city_label.setText(QCoreApplication.translate("MainWindow", u"Municipio:", None))
        self.net_node_city.setText(QCoreApplication.translate("MainWindow", u"Text", None))
        self.label_table_info.setText(QCoreApplication.translate("MainWindow", u"Nodos RT", None))
        self.disconnect_btn.setText(QCoreApplication.translate("MainWindow", u"Desconectar", None))
        self.connect_btn.setText(QCoreApplication.translate("MainWindow", u"Conectar", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Gesti\u00f3n de Nodos RT", None))
        self.edit_rtnode_btn.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.create_rtnode_btn.setText(QCoreApplication.translate("MainWindow", u"Crear", None))
        self.delete_rtnode_btn.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.label_receptor.setText(QCoreApplication.translate("MainWindow", u"Receptor:", None))
        self.start_btn.setText(QCoreApplication.translate("MainWindow", u"Iniciar", None))
        self.stop_btn.setText(QCoreApplication.translate("MainWindow", u"Detener", None))
        self.labelHeaderUser.setText(QCoreApplication.translate("MainWindow", u"Usuarios", None))
        self.editBtn.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.createBtn.setText(QCoreApplication.translate("MainWindow", u"Crear", None))
        self.eliminateBtn.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.labelBoxHeaderSettings.setText(QCoreApplication.translate("MainWindow", u"Configuraci\u00f3n", None))
        self.btn_settings_fullscreen.setText(QCoreApplication.translate("MainWindow", u"Pantalla Completa    F11", None))
        self.backupCheckBox.setText(QCoreApplication.translate("MainWindow", u"Salvas Peri\u00f3dicas", None))
        self.labelHeaderUser_2.setText(QCoreApplication.translate("MainWindow", u"Configuraci\u00f3n del Cliente", None))
        self.labelHeaderUser_3.setText(QCoreApplication.translate("MainWindow", u"Direcci\u00f3n del Servidor", None))
        self.labelHeaderUser_4.setText(QCoreApplication.translate("MainWindow", u"Puerto del Servidor", None))
        self.connectBtn.setText(QCoreApplication.translate("MainWindow", u"Conectar", None))
        self.label_credits.setText("")
        self.label_version.setText(QCoreApplication.translate("MainWindow", u"v1.0.0", None))
    # retranslateUi

