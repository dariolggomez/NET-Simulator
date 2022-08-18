from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from visuals.ui_netSelector import Ui_NetSelector
from services import net_service

GLOBAL_STATE = 0

class NetSelectorController(QMainWindow):
    def __init__(self):
        super().__init__()
        
        #Initialization
        self.ui = Ui_NetSelector()
        self.ui.setupUi(self)
        
        #Borderless Window
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        ## WINDOW SIZE ==> DEFAULT SIZE
        startSize = QSize(1100, 900)
        self.resize(startSize)
        self.setMinimumSize(startSize)

        #Load Ui Definitions
        self.uiDefinitions()

        #Load Node Table
        self.loadNetNodeTable()

    def uiDefinitions(self):
        def doubleClickMaximizeRestore(event):
            # IF DOUBLE CLICK CHANGE STATUS
            if event.type() == QtCore.QEvent.MouseButtonDblClick:
                QtCore.QTimer.singleShot(250, self.maximize_restore)

        self.ui.frame_labels_top_btns.mouseDoubleClickEvent = doubleClickMaximizeRestore

        ## SHOW ==> DROP SHADOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.ui.frame_bg.setGraphicsEffect(self.shadow)

        ## ==> RESIZE WINDOW
        self.sizegrip = QSizeGrip(self.ui.frame_size_grip)
        self.sizegrip.setStyleSheet("width: 20px; height: 20px; margin 0px; padding: 0px;")

        ## ==> MINIMIZE
        self.ui.btn_minimize.clicked.connect(self.showMinimized)

        ## ==> MAXIMIZE/RESTORE
        self.ui.btn_maximize_restore.clicked.connect(self.maximize_restore)

        ## ==> CLOSE APPLICATION
        self.ui.btn_close.clicked.connect(self.close)

        ## MOVE WIDGET
        self.ui.frame_labels_top_btns.mouseMoveEvent = self.moveWindow 

    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        if status == 0:
            self.showMaximized()
            GLOBAL_STATE = 1
            self.ui.central_widget_layout.setContentsMargins(0, 0, 0, 0)
            self.ui.btn_maximize_restore.setToolTip("Restaurar")
            self.ui.btn_maximize_restore.setIcon(QtGui.QIcon(u":/16x16/icons/16x16/cil-window-restore.png"))
            self.ui.frame_top_btns.setStyleSheet("background-color: rgb(27, 29, 35)")
            self.ui.frame_size_grip.hide()
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            self.ui.central_widget_layout.setContentsMargins(10, 10, 10, 10)
            self.ui.btn_maximize_restore.setToolTip("Maximizar")
            self.ui.btn_maximize_restore.setIcon(QtGui.QIcon(u":/16x16/icons/16x16/cil-window-maximize.png"))
            self.ui.frame_top_btns.setStyleSheet("background-color: rgba(27, 29, 35, 200)")
            self.ui.frame_size_grip.show()

    def moveWindow(self, event):
        # IF MAXIMIZED CHANGE TO NORMAL
        if self.returnStatus() == 1:
            self.maximize_restore()

        # MOVE WINDOW
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def returnStatus(self):
        return GLOBAL_STATE

    def loadNetNodeTable(self):
        rows = []
        for netNode in net_service.read_all():
            rows.append((netNode.id, netNode.nodename, netNode.city, netNode.date_created.date()))
        self.ui.netNodeTableWidget.setColumnCount(4)
        self.ui.netNodeTableWidget.setHorizontalHeaderLabels(("ID","Nodo","Ciudad","Fecha de Creación"))
        self.ui.netNodeTableWidget.horizontalHeader().setVisible(True)
        self.ui.netNodeTableWidget.setRowCount(len(rows))
        for row, cols in enumerate(rows):
            for col, text in enumerate(cols):
                table_item = QTableWidgetItem(str(text))
                table_item.setData(QtCore.Qt.UserRole+1, net_service.read_byID(rows[row][0]))
                self.ui.netNodeTableWidget.setItem(row, col, table_item)