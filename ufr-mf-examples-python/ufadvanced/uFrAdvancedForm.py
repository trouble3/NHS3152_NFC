# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uFrAdvanced.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(639, 723)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblReaderType = QtWidgets.QLabel(self.centralwidget)
        self.lblReaderType.setGeometry(QtCore.QRect(49, 31, 80, 16))
        self.lblReaderType.setObjectName("lblReaderType")
        self.txtReaderType = QtWidgets.QLineEdit(self.centralwidget)
        self.txtReaderType.setGeometry(QtCore.QRect(139, 28, 121, 24))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.txtReaderType.setFont(font)
        self.txtReaderType.setAutoFillBackground(True)
        self.txtReaderType.setFrame(True)
        self.txtReaderType.setAlignment(QtCore.Qt.AlignCenter)
        self.txtReaderType.setReadOnly(True)
        self.txtReaderType.setObjectName("txtReaderType")
        self.txtReaderSerial = QtWidgets.QLineEdit(self.centralwidget)
        self.txtReaderSerial.setGeometry(QtCore.QRect(139, 54, 121, 24))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.txtReaderSerial.setFont(font)
        self.txtReaderSerial.setAutoFillBackground(True)
        self.txtReaderSerial.setAlignment(QtCore.Qt.AlignCenter)
        self.txtReaderSerial.setReadOnly(True)
        self.txtReaderSerial.setObjectName("txtReaderSerial")
        self.lblReaderSerial = QtWidgets.QLabel(self.centralwidget)
        self.lblReaderSerial.setGeometry(QtCore.QRect(49, 57, 81, 16))
        self.lblReaderSerial.setObjectName("lblReaderSerial")
        self.txtCardSerial = QtWidgets.QLineEdit(self.centralwidget)
        self.txtCardSerial.setGeometry(QtCore.QRect(392, 54, 171, 24))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.txtCardSerial.setFont(font)
        self.txtCardSerial.setAutoFillBackground(True)
        self.txtCardSerial.setAlignment(QtCore.Qt.AlignCenter)
        self.txtCardSerial.setReadOnly(True)
        self.txtCardSerial.setObjectName("txtCardSerial")
        self.txtCardType = QtWidgets.QLineEdit(self.centralwidget)
        self.txtCardType.setGeometry(QtCore.QRect(392, 28, 51, 24))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.txtCardType.setFont(font)
        self.txtCardType.setAutoFillBackground(True)
        self.txtCardType.setAlignment(QtCore.Qt.AlignCenter)
        self.txtCardType.setReadOnly(True)
        self.txtCardType.setObjectName("txtCardType")
        self.lblCardType = QtWidgets.QLabel(self.centralwidget)
        self.lblCardType.setGeometry(QtCore.QRect(314, 31, 71, 16))
        self.lblCardType.setObjectName("lblCardType")
        self.lblCardSerial = QtWidgets.QLabel(self.centralwidget)
        self.lblCardSerial.setGeometry(QtCore.QRect(315, 57, 81, 16))
        self.lblCardSerial.setObjectName("lblCardSerial")
        self.lblCardUID = QtWidgets.QLabel(self.centralwidget)
        self.lblCardUID.setGeometry(QtCore.QRect(452, 31, 61, 16))
        self.lblCardUID.setObjectName("lblCardUID")
        self.txtUIDSize = QtWidgets.QLineEdit(self.centralwidget)
        self.txtUIDSize.setGeometry(QtCore.QRect(511, 28, 51, 24))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.txtUIDSize.setFont(font)
        self.txtUIDSize.setAutoFillBackground(True)
        self.txtUIDSize.setAlignment(QtCore.Qt.AlignCenter)
        self.txtUIDSize.setReadOnly(True)
        self.txtUIDSize.setObjectName("txtUIDSize")
        self.lblLightMode = QtWidgets.QLabel(self.centralwidget)
        self.lblLightMode.setGeometry(QtCore.QRect(50, 95, 80, 16))
        self.lblLightMode.setObjectName("lblLightMode")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(48, 77, 520, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.cboLightMode = QtWidgets.QComboBox(self.centralwidget)
        self.cboLightMode.setGeometry(QtCore.QRect(140, 91, 121, 30))
        self.cboLightMode.setObjectName("cboLightMode")
        self.cboLightMode.addItem("")
        self.cboLightMode.addItem("")
        self.cboLightMode.addItem("")
        self.cboLightMode.addItem("")
        self.cboLightMode.addItem("")
        self.lblSoundMode = QtWidgets.QLabel(self.centralwidget)
        self.lblSoundMode.setGeometry(QtCore.QRect(50, 125, 80, 16))
        self.lblSoundMode.setObjectName("lblSoundMode")
        self.cboSoundMode = QtWidgets.QComboBox(self.centralwidget)
        self.cboSoundMode.setGeometry(QtCore.QRect(140, 121, 121, 30))
        self.cboSoundMode.setObjectName("cboSoundMode")
        self.cboSoundMode.addItem("")
        self.cboSoundMode.addItem("")
        self.cboSoundMode.addItem("")
        self.cboSoundMode.addItem("")
        self.cboSoundMode.addItem("")
        self.cboSoundMode.addItem("")
        self.btnReaderUISignal = QtWidgets.QPushButton(self.centralwidget)
        self.btnReaderUISignal.setGeometry(QtCore.QRect(270, 94, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnReaderUISignal.setFont(font)
        self.btnReaderUISignal.setObjectName("btnReaderUISignal")
        self.btnReaderReset = QtWidgets.QPushButton(self.centralwidget)
        self.btnReaderReset.setGeometry(QtCore.QRect(446, 89, 120, 30))
        self.btnReaderReset.setObjectName("btnReaderReset")
        self.btnSoftRestart = QtWidgets.QPushButton(self.centralwidget)
        self.btnSoftRestart.setGeometry(QtCore.QRect(446, 119, 120, 30))
        self.btnSoftRestart.setObjectName("btnSoftRestart")
        self.tabUserDataRKey = QtWidgets.QTabWidget(self.centralwidget)
        self.tabUserDataRKey.setGeometry(QtCore.QRect(47, 158, 521, 100))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        self.tabUserDataRKey.setFont(font)
        self.tabUserDataRKey.setAutoFillBackground(False)
        self.tabUserDataRKey.setObjectName("tabUserDataRKey")
        self.tbReaderKey = QtWidgets.QWidget()
        self.tbReaderKey.setObjectName("tbReaderKey")
        self.chkHexReaderKey = QtWidgets.QCheckBox(self.tbReaderKey)
        self.chkHexReaderKey.setGeometry(QtCore.QRect(46, 42, 70, 17))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        self.chkHexReaderKey.setFont(font)
        self.chkHexReaderKey.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.chkHexReaderKey.setObjectName("chkHexReaderKey")
        self.btnFormatReadKey = QtWidgets.QPushButton(self.tbReaderKey)
        self.btnFormatReadKey.setGeometry(QtCore.QRect(277, 12, 201, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(223, 223, 223))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(223, 223, 223))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(223, 223, 223))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(223, 223, 223))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(223, 223, 223))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(223, 223, 223))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(223, 223, 223))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(223, 223, 223))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(223, 223, 223))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.btnFormatReadKey.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btnFormatReadKey.setFont(font)
        self.btnFormatReadKey.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnFormatReadKey.setAutoFillBackground(False)
        self.btnFormatReadKey.setStyleSheet("background-color: rgb(223, 223, 223);")
        self.btnFormatReadKey.setFlat(False)
        self.btnFormatReadKey.setObjectName("btnFormatReadKey")
        self.lblKeyIndex = QtWidgets.QLabel(self.tbReaderKey)
        self.lblKeyIndex.setGeometry(QtCore.QRect(116, 42, 60, 16))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        self.lblKeyIndex.setFont(font)
        self.lblKeyIndex.setObjectName("lblKeyIndex")
        self.txtReaderKey5 = QtWidgets.QLineEdit(self.tbReaderKey)
        self.txtReaderKey5.setGeometry(QtCore.QRect(173, 14, 30, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.txtReaderKey5.setFont(font)
        self.txtReaderKey5.setMaxLength(3)
        self.txtReaderKey5.setAlignment(QtCore.Qt.AlignCenter)
        self.txtReaderKey5.setObjectName("txtReaderKey5")
        self.txtReaderKey6 = QtWidgets.QLineEdit(self.tbReaderKey)
        self.txtReaderKey6.setGeometry(QtCore.QRect(205, 14, 31, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.txtReaderKey6.setFont(font)
        self.txtReaderKey6.setMaxLength(3)
        self.txtReaderKey6.setAlignment(QtCore.Qt.AlignCenter)
        self.txtReaderKey6.setObjectName("txtReaderKey6")
        self.txtReaderKey3 = QtWidgets.QLineEdit(self.tbReaderKey)
        self.txtReaderKey3.setGeometry(QtCore.QRect(109, 14, 30, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.txtReaderKey3.setFont(font)
        self.txtReaderKey3.setMaxLength(3)
        self.txtReaderKey3.setAlignment(QtCore.Qt.AlignCenter)
        self.txtReaderKey3.setObjectName("txtReaderKey3")
        self.txtReaderKey1 = QtWidgets.QLineEdit(self.tbReaderKey)
        self.txtReaderKey1.setGeometry(QtCore.QRect(45, 14, 30, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.txtReaderKey1.setFont(font)
        self.txtReaderKey1.setMaxLength(3)
        self.txtReaderKey1.setAlignment(QtCore.Qt.AlignCenter)
        self.txtReaderKey1.setObjectName("txtReaderKey1")
        self.txtReaderKey4 = QtWidgets.QLineEdit(self.tbReaderKey)
        self.txtReaderKey4.setGeometry(QtCore.QRect(141, 14, 30, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.txtReaderKey4.setFont(font)
        self.txtReaderKey4.setMaxLength(3)
        self.txtReaderKey4.setAlignment(QtCore.Qt.AlignCenter)
        self.txtReaderKey4.setObjectName("txtReaderKey4")
        self.txtReaderKey2 = QtWidgets.QLineEdit(self.tbReaderKey)
        self.txtReaderKey2.setGeometry(QtCore.QRect(77, 14, 30, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.txtReaderKey2.setFont(font)
        self.txtReaderKey2.setMaxLength(3)
        self.txtReaderKey2.setAlignment(QtCore.Qt.AlignCenter)
        self.txtReaderKey2.setObjectName("txtReaderKey2")
        self.cboKeyIndex = QtWidgets.QComboBox(self.tbReaderKey)
        self.cboKeyIndex.setGeometry(QtCore.QRect(185, 39, 50, 22))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.cboKeyIndex.setFont(font)
        self.cboKeyIndex.setObjectName("cboKeyIndex")
        self.tabUserDataRKey.addTab(self.tbReaderKey, "")
        self.tbUserData = QtWidgets.QWidget()
        self.tbUserData.setObjectName("tbUserData")
        self.lblUserData = QtWidgets.QLabel(self.tbUserData)
        self.lblUserData.setGeometry(QtCore.QRect(20, 10, 80, 16))
        self.lblUserData.setObjectName("lblUserData")
        self.txtUserData = QtWidgets.QLineEdit(self.tbUserData)
        self.txtUserData.setGeometry(QtCore.QRect(20, 30, 170, 24))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.txtUserData.setFont(font)
        self.txtUserData.setAutoFillBackground(False)
        self.txtUserData.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.txtUserData.setFrame(True)
        self.txtUserData.setAlignment(QtCore.Qt.AlignCenter)
        self.txtUserData.setReadOnly(True)
        self.txtUserData.setObjectName("txtUserData")
        self.txtNewUserData = QtWidgets.QLineEdit(self.tbUserData)
        self.txtNewUserData.setGeometry(QtCore.QRect(195, 30, 170, 24))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.txtNewUserData.setFont(font)
        self.txtNewUserData.setAutoFillBackground(True)
        self.txtNewUserData.setFrame(True)
        self.txtNewUserData.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.txtNewUserData.setReadOnly(False)
        self.txtNewUserData.setObjectName("txtNewUserData")
        self.lblNewUserData = QtWidgets.QLabel(self.tbUserData)
        self.lblNewUserData.setGeometry(QtCore.QRect(195, 10, 91, 16))
        self.lblNewUserData.setObjectName("lblNewUserData")
        self.btnSaveUserData = QtWidgets.QPushButton(self.tbUserData)
        self.btnSaveUserData.setGeometry(QtCore.QRect(374, 19, 131, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnSaveUserData.setFont(font)
        self.btnSaveUserData.setAutoFillBackground(True)
        self.btnSaveUserData.setFlat(False)
        self.btnSaveUserData.setObjectName("btnSaveUserData")
        self.tabUserDataRKey.addTab(self.tbUserData, "")
        self.lblCONN = QtWidgets.QLabel(self.centralwidget)
        self.lblCONN.setGeometry(QtCore.QRect(11, 262, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lblCONN.setFont(font)
        self.lblCONN.setFrameShape(QtWidgets.QFrame.Box)
        self.lblCONN.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lblCONN.setText("")
        self.lblCONN.setAlignment(QtCore.Qt.AlignCenter)
        self.lblCONN.setObjectName("lblCONN")
        self.lblFnExplain = QtWidgets.QLabel(self.centralwidget)
        self.lblFnExplain.setGeometry(QtCore.QRect(243, 262, 390, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.lblFnExplain.setFont(font)
        self.lblFnExplain.setFrameShape(QtWidgets.QFrame.Box)
        self.lblFnExplain.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lblFnExplain.setText("")
        self.lblFnExplain.setAlignment(QtCore.Qt.AlignCenter)
        self.lblFnExplain.setObjectName("lblFnExplain")
        self.lblFnResult = QtWidgets.QLabel(self.centralwidget)
        self.lblFnResult.setGeometry(QtCore.QRect(172, 262, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.lblFnResult.setFont(font)
        self.lblFnResult.setFrameShape(QtWidgets.QFrame.Box)
        self.lblFnResult.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lblFnResult.setText("")
        self.lblFnResult.setAlignment(QtCore.Qt.AlignCenter)
        self.lblFnResult.setObjectName("lblFnResult")
        self.mdiArea = QtWidgets.QMdiArea(self.centralwidget)
        self.mdiArea.setGeometry(QtCore.QRect(10, 288, 620, 390))
        self.mdiArea.setObjectName("mdiArea")
        self.lblCardStatus = QtWidgets.QLabel(self.centralwidget)
        self.lblCardStatus.setGeometry(QtCore.QRect(4, 681, 170, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lblCardStatus.setFont(font)
        self.lblCardStatus.setFrameShape(QtWidgets.QFrame.Box)
        self.lblCardStatus.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lblCardStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.lblCardStatus.setObjectName("lblCardStatus")
        self.lblCardFnExplain = QtWidgets.QLabel(self.centralwidget)
        self.lblCardFnExplain.setGeometry(QtCore.QRect(253, 681, 380, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.lblCardFnExplain.setFont(font)
        self.lblCardFnExplain.setFrameShape(QtWidgets.QFrame.Box)
        self.lblCardFnExplain.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lblCardFnExplain.setText("")
        self.lblCardFnExplain.setAlignment(QtCore.Qt.AlignCenter)
        self.lblCardFnExplain.setObjectName("lblCardFnExplain")
        self.lblCardFnResult = QtWidgets.QLabel(self.centralwidget)
        self.lblCardFnResult.setGeometry(QtCore.QRect(175, 681, 79, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.lblCardFnResult.setFont(font)
        self.lblCardFnResult.setFrameShape(QtWidgets.QFrame.Box)
        self.lblCardFnResult.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lblCardFnResult.setText("")
        self.lblCardFnResult.setAlignment(QtCore.Qt.AlignCenter)
        self.lblCardFnResult.setObjectName("lblCardFnResult")
        self.fCaption = QtWidgets.QFrame(self.centralwidget)
        self.fCaption.setGeometry(QtCore.QRect(10, 287, 621, 30))
        self.fCaption.setAutoFillBackground(False)
        self.fCaption.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.fCaption.setFrameShape(QtWidgets.QFrame.Box)
        self.fCaption.setFrameShadow(QtWidgets.QFrame.Plain)
        self.fCaption.setObjectName("fCaption")
        self.txtCaption = QtWidgets.QLineEdit(self.fCaption)
        self.txtCaption.setGeometry(QtCore.QRect(5, 5, 611, 21))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.txtCaption.setFont(font)
        self.txtCaption.setAutoFillBackground(False)
        self.txtCaption.setFrame(False)
        self.txtCaption.setAlignment(QtCore.Qt.AlignCenter)
        self.txtCaption.setReadOnly(True)
        self.txtCaption.setObjectName("txtCaption")
        self.linkLabel = QtWidgets.QLabel(self.centralwidget)
        self.linkLabel.setGeometry(QtCore.QRect(50, 5, 271, 16))
        self.linkLabel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.linkLabel.setStyleSheet("color: rgb(0, 0, 255);")
        self.linkLabel.setObjectName("linkLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 639, 21))
        self.menubar.setStyleSheet("")
        self.menubar.setObjectName("menubar")
        self.menuFunctions = QtWidgets.QMenu(self.menubar)
        self.menuFunctions.setObjectName("menuFunctions")
        MainWindow.setMenuBar(self.menubar)
        self.actionLinear_Read_Write = QtWidgets.QAction(MainWindow)
        self.actionLinear_Read_Write.setObjectName("actionLinear_Read_Write")
        self.actionBlock_Read_Write = QtWidgets.QAction(MainWindow)
        self.actionBlock_Read_Write.setObjectName("actionBlock_Read_Write")
        self.actionBlockInSector_Read_Write = QtWidgets.QAction(MainWindow)
        self.actionBlockInSector_Read_Write.setObjectName("actionBlockInSector_Read_Write")
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.actionValueBlock_Read_Write = QtWidgets.QAction(MainWindow)
        self.actionValueBlock_Read_Write.setObjectName("actionValueBlock_Read_Write")
        self.actionValueBlock_Increment_Decrement = QtWidgets.QAction(MainWindow)
        self.actionValueBlock_Increment_Decrement.setObjectName("actionValueBlock_Increment_Decrement")
        self.actionValueBlockInSector_Read_Write = QtWidgets.QAction(MainWindow)
        self.actionValueBlockInSector_Read_Write.setObjectName("actionValueBlockInSector_Read_Write")
        self.actionValueBlockInSector_Increment_Decrement = QtWidgets.QAction(MainWindow)
        self.actionValueBlockInSector_Increment_Decrement.setObjectName("actionValueBlockInSector_Increment_Decrement")
        self.actionSector_Trailer_Write = QtWidgets.QAction(MainWindow)
        self.actionSector_Trailer_Write.setObjectName("actionSector_Trailer_Write")
        self.actionLinearFormat_Card = QtWidgets.QAction(MainWindow)
        self.actionLinearFormat_Card.setObjectName("actionLinearFormat_Card")
        self.actionReader_Hardware_Firmvare_version = QtWidgets.QAction(MainWindow)
        self.actionReader_Hardware_Firmvare_version.setObjectName("actionReader_Hardware_Firmvare_version")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionView_All = QtWidgets.QAction(MainWindow)
        self.actionView_All.setObjectName("actionView_All")
        self.menuFunctions.addAction(self.actionLinear_Read_Write)
        self.menuFunctions.addSeparator()
        self.menuFunctions.addAction(self.actionBlock_Read_Write)
        self.menuFunctions.addAction(self.actionBlockInSector_Read_Write)
        self.menuFunctions.addSeparator()
        self.menuFunctions.addAction(self.actionValueBlock_Read_Write)
        self.menuFunctions.addAction(self.actionValueBlock_Increment_Decrement)
        self.menuFunctions.addSeparator()
        self.menuFunctions.addAction(self.actionValueBlockInSector_Read_Write)
        self.menuFunctions.addAction(self.actionValueBlockInSector_Increment_Decrement)
        self.menuFunctions.addSeparator()
        self.menuFunctions.addAction(self.actionSector_Trailer_Write)
        self.menuFunctions.addAction(self.actionLinearFormat_Card)
        self.menuFunctions.addSeparator()
        self.menuFunctions.addAction(self.actionReader_Hardware_Firmvare_version)
        self.menuFunctions.addSeparator()
        self.menuFunctions.addAction(self.actionView_All)
        self.menuFunctions.addSeparator()
        self.menuFunctions.addAction(self.actionExit)
        self.menubar.addAction(self.menuFunctions.menuAction())

        self.retranslateUi(MainWindow)
        self.tabUserDataRKey.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "uFr Coder Advanced"))
        self.lblReaderType.setText(_translate("MainWindow", "Reader Type"))
        self.lblReaderSerial.setText(_translate("MainWindow", "Reader Serial"))
        self.lblCardType.setText(_translate("MainWindow", "Card Type"))
        self.lblCardSerial.setText(_translate("MainWindow", "Card Serial"))
        self.lblCardUID.setText(_translate("MainWindow", "Card UID"))
        self.lblLightMode.setText(_translate("MainWindow", "Light Mode"))
        self.cboLightMode.setItemText(0, _translate("MainWindow", "None"))
        self.cboLightMode.setItemText(1, _translate("MainWindow", "Long Green"))
        self.cboLightMode.setItemText(2, _translate("MainWindow", "Long Red"))
        self.cboLightMode.setItemText(3, _translate("MainWindow", "Alternation"))
        self.cboLightMode.setItemText(4, _translate("MainWindow", "Flash"))
        self.lblSoundMode.setText(_translate("MainWindow", "Sound Mode"))
        self.cboSoundMode.setItemText(0, _translate("MainWindow", "None"))
        self.cboSoundMode.setItemText(1, _translate("MainWindow", "Short"))
        self.cboSoundMode.setItemText(2, _translate("MainWindow", "Long"))
        self.cboSoundMode.setItemText(3, _translate("MainWindow", "Double Short"))
        self.cboSoundMode.setItemText(4, _translate("MainWindow", "Tripple Short"))
        self.cboSoundMode.setItemText(5, _translate("MainWindow", "Tripplet Melody"))
        self.btnReaderUISignal.setText(_translate("MainWindow", "READER UI SIGNAL"))
        self.btnReaderReset.setText(_translate("MainWindow", "Reader Reset"))
        self.btnSoftRestart.setText(_translate("MainWindow", "Soft Restart"))
        self.chkHexReaderKey.setText(_translate("MainWindow", "Hex"))
        self.btnFormatReadKey.setText(_translate("MainWindow", "FORMAT READER KEY"))
        self.lblKeyIndex.setText(_translate("MainWindow", "Key Index"))
        self.txtReaderKey5.setText(_translate("MainWindow", "255"))
        self.txtReaderKey6.setText(_translate("MainWindow", "255"))
        self.txtReaderKey3.setText(_translate("MainWindow", "255"))
        self.txtReaderKey1.setText(_translate("MainWindow", "255"))
        self.txtReaderKey4.setText(_translate("MainWindow", "255"))
        self.txtReaderKey2.setText(_translate("MainWindow", "255"))
        self.tabUserDataRKey.setTabText(self.tabUserDataRKey.indexOf(self.tbReaderKey), _translate("MainWindow", "New Reader Key"))
        self.lblUserData.setText(_translate("MainWindow", "User Data"))
        self.lblNewUserData.setText(_translate("MainWindow", "New User Data"))
        self.btnSaveUserData.setText(_translate("MainWindow", "SAVE USER DATA"))
        self.tabUserDataRKey.setTabText(self.tabUserDataRKey.indexOf(self.tbUserData), _translate("MainWindow", "User Data"))
        self.lblCardStatus.setText(_translate("MainWindow", "CARD STATUS"))
        self.linkLabel.setText(_translate("MainWindow", "http://www.d-logic.net/nfc-rfid-reader-sdk/"))
        self.menuFunctions.setTitle(_translate("MainWindow", "Functions"))
        self.actionLinear_Read_Write.setText(_translate("MainWindow", "Linear Read/Write"))
        self.actionBlock_Read_Write.setText(_translate("MainWindow", "Block Read/Write"))
        self.actionBlockInSector_Read_Write.setText(_translate("MainWindow", "BlockInSector Read/Write"))
        self.action.setText(_translate("MainWindow", "-"))
        self.actionValueBlock_Read_Write.setText(_translate("MainWindow", "ValueBlock  Read/Write"))
        self.actionValueBlock_Increment_Decrement.setText(_translate("MainWindow", "ValueBlock Increment/Decrement"))
        self.actionValueBlockInSector_Read_Write.setText(_translate("MainWindow", "ValueBlockInSector Read/Write"))
        self.actionValueBlockInSector_Increment_Decrement.setText(_translate("MainWindow", "ValueBlockInSector Increment/Decrement"))
        self.actionSector_Trailer_Write.setText(_translate("MainWindow", "Sector Trailer Write"))
        self.actionLinearFormat_Card.setText(_translate("MainWindow", "LinearFormat Card"))
        self.actionReader_Hardware_Firmvare_version.setText(_translate("MainWindow", "Reader Hardware/Firmvare version"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionView_All.setText(_translate("MainWindow", "View All"))

