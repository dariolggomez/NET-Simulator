from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from visuals.ui_netSelector import Ui_NetSelector

class NetSelectorController(QWidget):
    def __init__(self):
        super().__init__()
        
        #Initialization
        self.ui = Ui_NetSelector()
        self.ui.setupUi(self)
        
        #Borderless Window
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)