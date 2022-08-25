from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from visuals.ui_rtForm import Ui_rtForm
from validator import validate
from services import rt_service

class RtFormController(QDialog):
    def __init__(self, caller):
        super().__init__()

        #Construction
        self.ui = Ui_rtForm()
        self.ui.setupUi(self)
        self.setModal(True)
        self.setWindowTitle("Net-Simulator")

        #Connections
        self.ui.acceptBtn.clicked.connect(lambda: self.createRtNode(caller))
        self.ui.cancelBtn.clicked.connect(self.close)

    def createRtNode(self, caller):
        nodename = self.ui.nodenameLineEdit.text()
        city = self.ui.cityComboBox.currentText()

        request = {"nodename": nodename}
        rules = {"nodename": "required|min:3"}
        result, _, errors = validate(request, rules, return_info=True)
        if(result):
            if(not rt_service.checkNodenameExists(nodename)):
                rt_service.create_rtNode(nodename, city, caller.currentNetNode.id)
                caller.loadRtManagementTable()
                self.close()
            else:
                msg = QMessageBox()
                msg.setText("Ya existe ese nombre.")
                msg.exec_()
        else:
            print(str(errors))
            if("nodename" in errors):
                if("Required" in  errors["nodename"]):
                    msg = QMessageBox()
                    msg.setText("Nombre requerido.")
                    msg.exec_()
                else:
                    if("Min" in errors["nodename"]):
                        msg = QMessageBox()
                        msg.setText("El nombre debe tener al menos 3 caracteres")
                        msg.exec_()

