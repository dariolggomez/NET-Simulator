import sys
from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtWidgets import *
from controllers.mainWindow import MainWindow
if __name__ == "__main__":
    app = QtWidgets.QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.activateWindow()
    window.raise_()
    sys.exit(app.exec_())