from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from visuals.ui_rtForm import Ui_rtForm
from validator import validate
from services import rt_service

class RtUpdateFormController(QDialog):
    def __init__(self, caller):
        super().__init__()

        #Construction
        self.ui = Ui_rtForm()
        self.ui.setupUi(self)
        self.setModal(True)
        self.setWindowTitle("Net-Simulator")

        #Connections
        self.ui.acceptBtn.clicked.connect(lambda: self.updateRtNode(caller))
        self.ui.cancelBtn.clicked.connect(self.close)

    def updateRtNode(self, caller):
        nodename = self.ui.nodenameLineEdit.text()
        city = self.ui.cityComboBox.currentText()
        currentRow = caller.ui.rtNodeManagementTable.currentRow()
        item = caller.ui.rtNodeManagementTable.item(currentRow, 1)
        rtNode = item.data(Qt.UserRole+1)

        request = {"nodename": nodename}
        rules = {"nodename": "required|min:3"}
        result, _, errors = validate(request, rules, return_info=True)
        if(result):
            if(nodename != rtNode.nodename):
                if(not rt_service.checkNodenameExists(nodename)):
                    rtNode.nodename = nodename
                    rtNode.city = city
                    rt_service.update_RtNode(rtNode)
                    caller.loadRtManagementTable()
                    self.close()
                else:
                    msg = QMessageBox()
                    msg.setText("Ya existe ese nombre.")
                    msg.exec_()
            else:
                if(city != rtNode.city):
                    rtNode.nodename = nodename
                    rtNode.city = city
                    rt_service.update_RtNode(rtNode)
                    caller.loadRtManagementTable()
                    self.close()
                else:
                    self.close()
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

    def setLinesEditsValues(self, node):
        self.ui.nodenameLineEdit.setText(node.nodename)
        self.ui.cityComboBox.setCurrentText(node.city)