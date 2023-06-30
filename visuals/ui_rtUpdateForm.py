# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rtUpdateFormYwmNfz.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_rtUpdateForm(object):
    def setupUi(self, rtUpdateForm):
        if not rtUpdateForm.objectName():
            rtUpdateForm.setObjectName(u"rtUpdateForm")
        rtUpdateForm.resize(464, 431)
        rtUpdateForm.setStyleSheet(u"background-color: rgb(44, 49, 60);\n"
"color: rgb(85, 170, 255);")
        self.verticalLayout = QVBoxLayout(rtUpdateForm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.bg = QFrame(rtUpdateForm)
        self.bg.setObjectName(u"bg")
        self.bg.setStyleSheet(u"/* LINE EDIT */\n"
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
"    background: rgb(85, 170, 255);\n"
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
"	background: rgb(85, 170, 255);\n"
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
"    background: rgb(55, 63"
                        ", 77);\n"
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
"	border-radius"
                        ": 10px;\n"
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
"	color: rgb("
                        "85, 170, 255);	\n"
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
"QSlider::handle:verti"
                        "cal {\n"
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
        self.bg.setFrameShape(QFrame.StyledPanel)
        self.bg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.bg)
        self.verticalLayout_2.setSpacing(8)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(12, 12, 12, 12)
        self.contentFrame = QFrame(self.bg)
        self.contentFrame.setObjectName(u"contentFrame")
        self.contentFrame.setStyleSheet(u"")
        self.contentFrame.setFrameShape(QFrame.StyledPanel)
        self.contentFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentFrame)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.contentFrame)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setFamily(u"Segoe UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)

        self.verticalLayout_6.addWidget(self.label_4)

        self.frame_3 = QFrame(self.contentFrame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setFamily(u"Segoe UI Semibold")
        font1.setPointSize(9)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_3.setFont(font1)

        self.verticalLayout_5.addWidget(self.label_3)

        self.nodenameLineEdit = QLineEdit(self.frame_3)
        self.nodenameLineEdit.setObjectName(u"nodenameLineEdit")
        self.nodenameLineEdit.setFont(font1)
        self.nodenameLineEdit.setStyleSheet(u"QLineEdit {\n"
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

        self.verticalLayout_5.addWidget(self.nodenameLineEdit)


        self.verticalLayout_6.addWidget(self.frame_3)

        self.frame = QFrame(self.contentFrame)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 25))
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: rgb(85, 170, 255);")

        self.verticalLayout_3.addWidget(self.label)

        self.cityComboBox = QComboBox(self.frame)
        self.cityComboBox.addItem("")
        self.cityComboBox.addItem("")
        self.cityComboBox.addItem("")
        self.cityComboBox.addItem("")
        self.cityComboBox.addItem("")
        self.cityComboBox.addItem("")
        self.cityComboBox.addItem("")
        self.cityComboBox.addItem("")
        self.cityComboBox.addItem("")
        self.cityComboBox.addItem("")
        self.cityComboBox.addItem("")
        self.cityComboBox.addItem("")
        self.cityComboBox.addItem("")
        self.cityComboBox.addItem("")
        self.cityComboBox.addItem("")
        self.cityComboBox.setObjectName(u"cityComboBox")
        font2 = QFont()
        font2.setFamily(u"Segoe UI Semibold")
        font2.setBold(True)
        font2.setWeight(75)
        self.cityComboBox.setFont(font2)

        self.verticalLayout_3.addWidget(self.cityComboBox)


        self.verticalLayout_6.addWidget(self.frame)

        self.verticalSpacer = QSpacerItem(20, 31, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)


        self.verticalLayout_2.addWidget(self.contentFrame)

        self.btnsFrame = QFrame(self.bg)
        self.btnsFrame.setObjectName(u"btnsFrame")
        self.btnsFrame.setMinimumSize(QSize(0, 50))
        self.btnsFrame.setMaximumSize(QSize(16777215, 50))
        self.btnsFrame.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;\n"
"")
        self.btnsFrame.setFrameShape(QFrame.StyledPanel)
        self.btnsFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.btnsFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.horizontalSpacer = QSpacerItem(108, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.acceptBtn = QPushButton(self.btnsFrame)
        self.acceptBtn.setObjectName(u"acceptBtn")
        self.acceptBtn.setMinimumSize(QSize(80, 30))
        self.acceptBtn.setFont(font1)
        self.acceptBtn.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout.addWidget(self.acceptBtn)

        self.cancelBtn = QPushButton(self.btnsFrame)
        self.cancelBtn.setObjectName(u"cancelBtn")
        self.cancelBtn.setMinimumSize(QSize(80, 30))
        self.cancelBtn.setFont(font1)
        self.cancelBtn.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout.addWidget(self.cancelBtn)


        self.verticalLayout_2.addWidget(self.btnsFrame)

        self.verticalLayout_2.setStretch(0, 5)
        self.verticalLayout_2.setStretch(1, 1)

        self.verticalLayout.addWidget(self.bg)


        self.retranslateUi(rtUpdateForm)

        QMetaObject.connectSlotsByName(rtUpdateForm)
    # setupUi

    def retranslateUi(self, rtUpdateForm):
        rtUpdateForm.setWindowTitle(QCoreApplication.translate("rtUpdateForm", u"Dialog", None))
        self.label_4.setText(QCoreApplication.translate("rtUpdateForm", u"Crear Nodo", None))
        self.label_3.setText(QCoreApplication.translate("rtUpdateForm", u"Nombre", None))
        self.label.setText(QCoreApplication.translate("rtUpdateForm", u"Municipio", None))
        self.cityComboBox.setItemText(0, QCoreApplication.translate("rtUpdateForm", u"Cerro", None))
        self.cityComboBox.setItemText(1, QCoreApplication.translate("rtUpdateForm", u"Playa", None))
        self.cityComboBox.setItemText(2, QCoreApplication.translate("rtUpdateForm", u"Plaza de la Revoluci\u00f3n", None))
        self.cityComboBox.setItemText(3, QCoreApplication.translate("rtUpdateForm", u"Centro Habana", None))
        self.cityComboBox.setItemText(4, QCoreApplication.translate("rtUpdateForm", u"La Habana Vieja", None))
        self.cityComboBox.setItemText(5, QCoreApplication.translate("rtUpdateForm", u"Regla", None))
        self.cityComboBox.setItemText(6, QCoreApplication.translate("rtUpdateForm", u"La Habana del Este", None))
        self.cityComboBox.setItemText(7, QCoreApplication.translate("rtUpdateForm", u"Guanabacoa", None))
        self.cityComboBox.setItemText(8, QCoreApplication.translate("rtUpdateForm", u"San Miguel del Padr\u00f3n", None))
        self.cityComboBox.setItemText(9, QCoreApplication.translate("rtUpdateForm", u"Diez de Octubre", None))
        self.cityComboBox.setItemText(10, QCoreApplication.translate("rtUpdateForm", u"Marianao", None))
        self.cityComboBox.setItemText(11, QCoreApplication.translate("rtUpdateForm", u"La Lisa", None))
        self.cityComboBox.setItemText(12, QCoreApplication.translate("rtUpdateForm", u"Boyeros", None))
        self.cityComboBox.setItemText(13, QCoreApplication.translate("rtUpdateForm", u"Arroyo Naranjo", None))
        self.cityComboBox.setItemText(14, QCoreApplication.translate("rtUpdateForm", u"Cotorro", None))

        self.acceptBtn.setText(QCoreApplication.translate("rtUpdateForm", u"Aceptar", None))
        self.cancelBtn.setText(QCoreApplication.translate("rtUpdateForm", u"Cancelar", None))
    # retranslateUi

