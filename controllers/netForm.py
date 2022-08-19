from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from visuals.ui_netForm import Ui_formNet
from validator import validate
from services import net_service

class NetFormController(QDialog):
    def __init__(self, caller):
        super().__init__()

        #Construction
        self.ui = Ui_formNet()
        self.ui.setupUi(self)
        self.setModal(True)

        #Connections
        self.ui.acceptBtn.clicked.connect(lambda: self.createNetNode(caller))
        self.ui.cancelBtn.clicked.connect(self.close)

    def createNetNode(self, caller):
        nodename = self.ui.nodenameLineEdit.text()
        city = self.ui.cityLineEdit.text()

        request = {"nodename": nodename,
                   "city": city}
        rules = {"nodename": "required|min:3",
                 "city": "required|min:2"}
        result, _, errors = validate(request, rules, return_info=True)
        if(result):
            if(not net_service.checkNodenameExists(nodename)):
                net_service.create_netNode(nodename, city)
                caller.loadNetNodeTable()
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
            else:
                if("city" in errors):
                    if("Required" in errors["city"]):
                        msg = QMessageBox()
                        msg.setText("Ciudad requerida.")
                        msg.exec_()
                    else:
                        if("Min" in errors["city"]):
                            msg = QMessageBox()
                            msg.setText("La ciudad debe tener al menos 2 caracteres")
                            msg.exec_()

