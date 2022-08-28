from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from visuals.ui_mainWindow import Ui_MainWindow
from styles.ui_styles import Style
from controllers import netNodeSelector, rtForm
from services import rt_service, net_service

GLOBAL_STATE = 0
GLOBAL_FULLSCREEN = 0

class MainWindow(QMainWindow):
    count = 1
    def __init__(self, currentNetNode):
        super().__init__()
        #Initialization
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.__currentNetNode = currentNetNode
        print(f"Los nodos rt relacionados son: {self.__currentNetNode.rt_nodes}")

        #Remove Default Title Bar
        self.removeTitleBar()

        #Load Ui Definitions
        self.uiDefinitions()

        ## SET ==> WINDOW TITLE
        self.setWindowTitle('NET-Simulator')
        self.labelTitle('NET-Simulator')
        self.labelDescription('Herramienta para la Simulación de los Nodos NET')

        ## WINDOW SIZE ==> DEFAULT SIZE
        startSize = QSize(1280, 900)
        self.resize(startSize)
        minSize = QSize(600, 500)
        self.setMinimumSize(minSize)

        ## ==> TOGGLE MENU SIZE
        self.ui.btn_toggle_menu.clicked.connect(lambda: self.toggleMenu(220, True))

        #Load Ui Settings
        self.ui.net_node_in_use.setText(currentNetNode.nodename)
        self.ui.net_node_city.setText(currentNetNode.city)

        #Add custom menu buttons
        self.ui.stackedWidget.setMinimumWidth(20)
        self.addNewMenu("Inicio", "btn_home", "url(:/16x16/icons/16x16/cil-home.png)", True)
        self.addNewMenu("Nodos RT", "btn_rt_nodes", "url(:/16x16/icons/16x16/cil-layers.png)", True)
        self.addNewMenu("Desconectar Nodo", "btn_disconnect", "url(:/16x16/icons/16x16/cil-account-logout.png)", False)
        
        #Select standard menu
        self.selectStandardMenu("btn_home")
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)

        #Events Connections
        self.ui.create_rtnode_btn.clicked.connect(self.showRtForm)
        self.ui.delete_rtnode_btn.clicked.connect(self.deleteRtCurrentTableItem)

    @property
    def currentNetNode(self):
        return self.__currentNetNode

    def removeTitleBar(self):
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def uiDefinitions(self):
        def doubleClickMaximizeRestore(event):
            # IF DOUBLE CLICK CHANGE STATUS
            if event.type() == QtCore.QEvent.MouseButtonDblClick:
                QtCore.QTimer.singleShot(250, self.maximize_restore)

        self.ui.frame_label_top_btns.mouseDoubleClickEvent = doubleClickMaximizeRestore

        ## SHOW ==> DROP SHADOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.ui.frame_main.setGraphicsEffect(self.shadow)

        ## ==> RESIZE WINDOW
        self.sizegrip = QSizeGrip(self.ui.frame_size_grip)
        self.sizegrip.setStyleSheet("width: 20px; height: 20px; margin 0px; padding: 0px;")

        ## ==> MINIMIZE
        self.ui.btn_minimize.clicked.connect(self.showMinimized)

        ## ==> MAXIMIZE/RESTORE
        self.ui.btn_maximize_restore.clicked.connect(self.maximize_restore)

        ## ==> CLOSE APPLICATION
        self.ui.btn_close.clicked.connect(self.close)

        ## ==> FULLSCREEN
        self.ui.btn_fullscreen.clicked.connect(self.winFullscreen)
        self.ui.btn_settings_fullscreen.clicked.connect(self.winFullscreen)

        ## MOVE WIDGET
        self.ui.frame_label_top_btns.mouseMoveEvent = self.moveWindow 

    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        if status == 0:
            self.showMaximized()
            GLOBAL_STATE = 1
            self.ui.central_widget_layout.setContentsMargins(0, 0, 0, 0)
            self.ui.btn_maximize_restore.setToolTip("Restaurar")
            self.ui.btn_maximize_restore.setIcon(QtGui.QIcon(u":/16x16/icons/16x16/cil-window-restore.png"))
            self.ui.frame_top_btns.setStyleSheet("background-color: rgb(50, 50, 51); border-top-right-radius: 0px;")
            self.ui.frame_toggle.setStyleSheet("background-color: rgb(50, 50, 51); border-top-left-radius: 0px;")
            self.ui.frame_grip.setStyleSheet("background-color: rgb(0, 122, 204); border-bottom-right-radius: 0px; border-bottom-left-radius: 0px;")
            self.ui.frame_size_grip.hide()
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            self.ui.central_widget_layout.setContentsMargins(10, 10, 10, 10)
            self.ui.btn_maximize_restore.setToolTip("Maximizar")
            self.ui.btn_maximize_restore.setIcon(QtGui.QIcon(u":/16x16/icons/16x16/cil-window-maximize.png"))
            self.ui.frame_top_btns.setStyleSheet("background-color: rgb(50, 50, 51); border-top-right-radius: 10px;")
            self.ui.frame_toggle.setStyleSheet("background-color: rgb(50, 50, 51); border-top-left-radius: 10px;")
            self.ui.frame_grip.setStyleSheet("background-color: rgb(0, 122, 204); border-bottom-right-radius: 10px; border-bottom-left-radius: 10px;")
            self.ui.frame_size_grip.show()

    def winFullscreen(self):
        global GLOBAL_FULLSCREEN
        global GLOBAL_STATE
        status = GLOBAL_FULLSCREEN
        if status == 0:
            self.showFullScreen()
            GLOBAL_FULLSCREEN = 1
            GLOBAL_STATE = 1
            self.ui.central_widget_layout.setContentsMargins(0,0,0,0)
            self.ui.frame_top_btns.setMaximumHeight(0)
            self.ui.frame_toggle.setStyleSheet("background-color: rgb(50, 50, 51); border-top-left-radius: 0px;")
            self.ui.frame_grip.setStyleSheet("background-color: rgb(0, 122, 204); border-bottom-right-radius: 0px; border-bottom-left-radius: 0px;")
            self.ui.frame_size_grip.hide()
        else:
            self.showNormal()
            GLOBAL_FULLSCREEN = 0
            GLOBAL_STATE = 0
            self.ui.central_widget_layout.setContentsMargins(10,10,10,10)
            self.ui.frame_top_btns.setMaximumHeight(42)
            self.ui.frame_toggle.setStyleSheet("background-color: rgb(50, 50, 51); border-top-left-radius: 10px;")
            self.ui.frame_grip.setStyleSheet("background-color: rgb(0, 122, 204); border-bottom-right-radius: 10px; border-bottom-left-radius: 10px;")
            self.ui.frame_size_grip.show()
            self.ui.btn_maximize_restore.setIcon(QtGui.QIcon(u":/16x16/icons/16x16/cil-window-maximize.png"))

    def moveWindow(self, event):
        # IF MAXIMIZED CHANGE TO NORMAL
        if self.returnStatus() == 1:
            self.maximize_restore()

        # MOVE WINDOW
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

    def returnStatus(self):
        return GLOBAL_STATE

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    # LABEL TITLE
    def labelTitle(self, text):
        self.ui.label_title_bar_top.setText(text)

    # LABEL DESCRIPTION
    def labelDescription(self, text):
        self.ui.label_top_info_1.setText(text)

    def toggleMenu(self, maxWidth, enable):
        if enable:
            # GET WIDTH
            width = self.ui.frame_left_menu.width()
            maxExtend = maxWidth
            standard = 70

            # SET MAX WIDTH
            if width == 70:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(300)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

    def Button(self):
        # GET BT CLICKED
        btnWidget = self.sender()

        # PAGE HOME
        if btnWidget.objectName() == "btn_home":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            self.resetStyle("btn_home")
            self.labelPage("Inicio")
            btnWidget.setStyleSheet(self.selectMenu(btnWidget.styleSheet()))

        # Disconnect Node
        if btnWidget.objectName() == "btn_disconnect":
            nodeSelector = netNodeSelector.NetSelectorController()
            nodeSelector.show()
            self.close()

        # Rt Nodes Management
        if btnWidget.objectName() == "btn_rt_nodes":
            self.loadRtManagementTable()
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_rt_nodes)
            self.resetStyle("btn_rt_nodes")
            self.labelPage("Nodos RT")
            btnWidget.setStyleSheet(self.selectMenu(btnWidget.styleSheet()))


    ## ==> SELECT/DESELECT MENU
    ########################################################################
    ## ==> SELECT
    def selectMenu(self, getStyle):
        select = getStyle + ("QPushButton { border-right: 5px solid rgb(30, 30, 30); }")
        return select
    
    ## ==> RESET SELECTION
    def resetStyle(self, widget):
        for w in self.ui.frame_left_menu.findChildren(QPushButton):
            if w.objectName() != widget:
                w.setStyleSheet(self.deselectMenu(w.styleSheet()))

    ## ==> START SELECTION
    def selectStandardMenu(self, widget):
        for w in self.ui.frame_left_menu.findChildren(QPushButton):
            if w.objectName() == widget:
                w.setStyleSheet(self.selectMenu(w.styleSheet()))

    ## ==> DESELECT
    def deselectMenu(self, getStyle):
        deselect = getStyle.replace("QPushButton { border-right: 5px solid rgb(30, 30, 30); }", "")
        return deselect

    ## ==> CHANGE PAGE LABEL TEXT
    def labelPage(self, text):
        newText = '| ' + text.upper()
        self.ui.label_top_info_2.setText(newText)

    
    ## ==> DYNAMIC MENUS
    ########################################################################
    def addNewMenu(self, name, objName, icon, isTopMenu):
        font = QFont()
        font.setFamily(u"Segoe UI")
        button = QPushButton(str(self.count),self)
        button.setObjectName(objName)
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(button.sizePolicy().hasHeightForWidth())
        button.setSizePolicy(sizePolicy3)
        button.setMinimumSize(QSize(0, 70))
        button.setLayoutDirection(Qt.LeftToRight)
        button.setFont(font)
        button.setStyleSheet(Style.style_bt_standard.replace('ICON_REPLACE', icon))
        button.setText(name)
        button.setToolTip(name)
        button.clicked.connect(self.Button)

        if isTopMenu:
            self.ui.layout_menus.addWidget(button)
        else:
            self.ui.layout_menu_bottom.addWidget(button)

    def loadRtManagementTable(self):
        self.ui.rtNodeManagementTable.sortByColumn(0, Qt.AscendingOrder)
        self.ui.rtNodeManagementTable.setRowCount(0)
        rows = []
        for rtNode in net_service.read_byID(self.currentNetNode.id).rt_nodes:
            rows.append((rtNode.id, rtNode.nodename, rtNode.city, rtNode.date_created))
        self.ui.rtNodeManagementTable.setColumnCount(4)
        self.ui.rtNodeManagementTable.setHorizontalHeaderLabels(("ID","Nombre","Ciudad","Fecha de Creación"))
        self.ui.rtNodeManagementTable.horizontalHeader().setVisible(True)
        self.ui.rtNodeManagementTable.setRowCount(len(rows))
        for row, cols in enumerate(rows):
            for col, text in enumerate(cols):
                if(col == 0 or col == 3):
                    if(col == 0):
                        table_item = QTableWidgetItem()
                        table_item.setData(QtCore.Qt.DisplayRole, text)
                    else:
                        table_item = QTableWidgetItem()
                        table_item.setData(QtCore.Qt.DisplayRole, QDateTime(text))
                else:
                    table_item = QTableWidgetItem(str(text))
                    table_item.setData(QtCore.Qt.UserRole+1, rt_service.read_byID(rows[row][0]))
                self.ui.rtNodeManagementTable.setItem(row, col, table_item)

    def showRtForm(self):
        rtFormController = rtForm.RtFormController(self)
        rtFormController.show()

    def deleteRtCurrentTableItem(self):
        currentRow = self.ui.rtNodeManagementTable.currentRow()
        item = self.ui.rtNodeManagementTable.item(currentRow, 1)
        if(item is not None):
            rtNode = item.data(Qt.UserRole+1)
            rt_service.delete_rtNode(rtNode)
            self.loadRtManagementTable()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("NET-Simulator")
            msg.setText("Debe seleccionar un nodo.")
            msg.exec_()