from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from visuals.ui_netForm import Ui_formNet

class NetFormController(QDialog):
    def __init__(self, caller):
        super().__init__()
        self.ui = Ui_formNet()
        self.ui.setupUi(self)
