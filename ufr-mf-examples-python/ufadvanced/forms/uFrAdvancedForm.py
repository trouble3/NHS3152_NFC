# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uFrAdvanced.ui'
#
# Created by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(637, 710)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblReaderType = QtWidgets.QLabel(self.centralwidget)
        self.lblReaderType.setGeometry(QtCore.QRect(49, 12, 80, 16))
        self.lblReaderType.setObjectName("lblReaderType")
        self.txtReaderType = QtWidgets.QLineEdit(self.centralwidget)
        self.txtReaderType.setGeometry(QtCore.QRect(139, 9, 121, 24))
        self.txtReaderType.setFrame(True)
        self.txtReaderType.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.txtReaderType.setReadOnly(True)
        self.txtReaderType.setObjectName("txtReaderType")
        self.txtReaderSerial = QtWidgets.QLineEdit(self.centralwidget)
        self.txtReaderSerial.setGeometry(QtCore.QRect(139, 35, 121, 24))
        self.txtReaderSerial.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.txtReaderSerial.setReadOnly(True)
        self.txtReaderSerial.setObjectName("txtReaderSerial")
        self.lblReaderSerial = QtWidgets.QLabel(self.centralwidget)
        self.lblReaderSerial.setGeometry(QtCore.QRect(49, 38, 81, 16))
        self.lblReaderSerial.setObjectName("lblReaderSerial")
        self.txtCardSerial = QtWidgets.QLineEdit(self.centralwidget)
        self.txtCardSerial.setGeometry(QtCore.QRect(392, 35, 171, 24))
        self.txtCardSerial.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.txtCardSerial.setReadOnly(True)
        self.txtCardSerial.setObjectName("txtCardSerial")
        self.txtCardType = QtWidgets.QLineEdit(self.centralwidget)
        self.txtCardType.setGeometry(QtCore.QRect(392, 9, 51, 24))
        self.txtCardType.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.txtCardType.setReadOnly(True)
        self.txtCardType.setObjectName("txtCardType")
        self.lblCardType = QtWidgets.QLabel(self.centralwidget)
        self.lblCardType.setGeometry(QtCore.QRect(314, 12, 71, 16))
        self.lblCardType.setObjectName("lblCardType")
        self.lblCardSerial = QtWidgets.QLabel(self.centralwidget)
        self.lblCardSerial.setGeometry(QtCore.QRect(315, 38, 81, 16))
        self.lblCardSerial.setObjectName("lblCardSerial")
        self.lblCardUID = QtWidgets.QLabel(self.centralwidget)
        self.lblCardUID.setGeometry(QtCore.QRect(452, 12, 61, 16))
        self.lblCardUID.setObjectName("lblCardUID")
        self.txtUIDSize = QtWidgets.QLineEdit(self.centralwidget)
        self.txtUIDSize.setGeometry(QtCore.QRect(511, 9, 51, 24))
        self.txtUIDSize.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.txtUIDSize.setReadOnly(True)
        self.txtUIDSize.setObjectName("txtUIDSize")
        self.lblLightMode = QtWidgets.QLabel(self.centralwidget)
        self.lblLightMode.setGeometry(QtCore.QRect(50, 76, 80, 16))
        self.lblLightMode.setObjectName("lblLightMode")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(48, 58, 520, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.cboLightMode = QtWidgets.QComboBox(self.centralwidget)
        self.cboLightMode.setGeometry(QtCore.QRect(140, 72, 121, 30))
        self.cboLightMode.setObjectName("cboLightMode")
        self.cboLightMode.addItem("")
        self.cboLightMode.addItem("")
        self.cboLightMode.addItem("")
        self.cboLightMode.addItem("")
        self.cboLightMode.addItem("")
        self.lblSoundMode = QtWidgets.QLabel(self.centralwidget)
        self.lblSoundMode.setGeometry(QtCore.QRect(50, 106, 80, 16))
        self.lblSoundMode.setObjectName("lblSoundMode")
        self.cboSoundMode = QtWidgets.QComboBox(self.centralwidget)
        self.cboSoundMode.setGeometry(QtCore.QRect(140, 102, 121, 30))
        self.cboSoundMode.setObjectName("cboSoundMode")
        self.cboSoundMode.addItem("")
        self.cboSoundMode.addItem("")
        self.cboSoundMode.addItem("")
        self.cboSoundMode.addItem("")
        self.cboSoundMode.addItem("")
        self.cboSoundMode.addItem("")
        self.btnReaderUISignal = QtWidgets.QPushButton(self.centralwidget)
        self.btnReaderUISignal.setGeometry(QtCore.QRect(270, 75, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnReaderUISignal.setFont(font)
        self.btnReaderUISignal.setObjectName("btnReaderUISignal")
        self.btnReaderReset = QtWidgets.QPushButton(self.centralwidget)
        self.btnReaderReset.setGeometry(QtCore.QRect(446, 70, 120, 30))
        self.btnReaderReset.setObjectName("btnReaderReset")
        self.btnSoftRestart = QtWidgets.QPushButton(self.centralwidget)
        self.btnSoftRestart.setGeometry(QtCore.QRect(446, 100, 120, 30))
        self.btnSoftRestart.setObjectName("btnSoftRestart")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(47, 136, 521, 121))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        self.tabWidget.setFont(font)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tbCardKeys = QtWidgets.QWidget()
        self.tbCardKeys.setObjectName("tbCardKeys")
        self.lblKeyA = QtWidgets.QLabel(self.tbCardKeys)
        self.lblKeyA.setGeometry(QtCore.QRect(20, 12, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        self.lblKeyA.setFont(font)
        self.lblKeyA.setObjectName("lblKeyA")
        self.lblKeyB = QtWidgets.QLabel(self.tbCardKeys)
        self.lblKeyB.setGeometry(QtCore.QRect(20, 42, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        self.lblKeyB.setFont(font)
        self.lblKeyB.setObjectName("lblKeyB")
        self.chkHexCardKeys = QtWidgets.QCheckBox(self.tbCardKeys)
        self.chkHexCardKeys.setGeometry(QtCore.QRect(81, 70, 70, 17))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        self.chkHexCardKeys.setFont(font)
        self.chkHexCardKeys.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.chkHexCardKeys.setObjectName("chkHexCardKeys")
        self.btnFormatCardKeys = QtWidgets.QPushButton(self.tbCardKeys)
        self.btnFormatCardKeys.setGeometry(QtCore.QRect(300, 12, 181, 51))
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
        self.btnFormatCardKeys.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        self.btnFormatCardKeys.setFont(font)
        self.btnFormatCardKeys.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnFormatCardKeys.setAutoFillBackground(False)
        self.btnFormatCardKeys.setStyleSheet("background-color: rgb(223, 223, 223);")
        self.btnFormatCardKeys.setFlat(False)
        self.btnFormatCardKeys.setObjectName("btnFormatCardKeys")
        self.lblSectorsFormat = QtWidgets.QLabel(self.tbCardKeys)
        self.lblSectorsFormat.setGeometry(QtCore.QRect(300, 70, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        self.lblSectorsFormat.setFont(font)
        self.lblSectorsFormat.setObjectName("lblSectorsFormat")
        self.txtSectorFormating = QtWidgets.QLineEdit(self.tbCardKeys)
        self.txtSectorFormating.setGeometry(QtCore.QRect(428, 69, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.txtSectorFormating.setFont(font)
        self.txtSectorFormating.setStyleSheet("background-color: rgb(204, 204, 204);")
        self.txtSectorFormating.setAlignment(QtCore.Qt.AlignCenter)
        self.txtSectorFormating.setReadOnly(True)
        self.txtSectorFormating.setObjectName("txtSectorFormating")
        self.txtCardKeysA1 = QtWidgets.QLineEdit(self.tbCardKeys)
        self.txtCardKeysA1.setGeometry(QtCore.QRect(81, 12, 30, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.txtCardKeysA1.setFont(font)
        self.txtCardKeysA1.setMaxLength(3)
        self.txtCardKeysA1.setAlignment(QtCore.Qt.AlignCenter)
        self.txtCardKeysA1.setObjectName("txtCardKeysA1")
        self.txtCardKeysA2 = QtWidgets.QLineEdit(self.tbCardKeys)
        self.txtCardKeysA2.setGeometry(QtCore.QRect(113, 12, 30, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.txtCardKeysA2.setFont(font)
        self.txtCardKeysA2.setMaxLength(3)
        self.txtCardKeysA2.setAlignment(QtCore.Qt.AlignCenter)
        self.txtCardKeysA2.setObjectName("txtCardKeysA2")
        self.txtCardKeysA3 = QtWidgets.QLineEdit(self.tbCardKeys)
        self.txtCardKeysA3.setGeometry(QtCore.QRect(145, 12, 30, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.txtCardKeysA3.setFont(font)
        self.txtCardKeysA3.setMaxLength(3)
        self.txtCardKeysA3.setAlignment(QtCore.Qt.AlignCenter)
        self.txtCardKeysA3.setObjectName("txtCardKeysA3")
        self.txtCardKeysA4 = QtWidgets.QLineEdit(self.tbCardKeys)
        self.txtCardKeysA4.setGeometry(QtCore.QRect(177, 12, 30, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.txtCardKeysA4.setFont(font)
        self.txtCardKeysA4.setMaxLength(3)
        self.txtCardKeysA4.setAlignment(QtCore.Qt.AlignCenter)
        self.txtCardKeysA4.setObjectName("txtCardKeysA4")
        self.txtCardKeysA5 = QtWidgets.QLineEdit(self.tbCardKeys)
        self.txtCardKeysA5.setGeometry(QtCore.QRect(209, 12, 30, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.txtCardKeysA5.setFont(font)
        self.txtCardKeysA5.setMaxLength(3)
        self.txtCardKeysA5.setAlignment(QtCore.Qt.AlignCenter)
        self.txtCardKeysA5.setObjectName("txtCardKeysA5")
        self.txtCardKeysA6 = QtWidgets.QLineEdit(self.tbCardKeys)
        self.txtCardKeysA6.setGeometry(QtCore.QRect(241, 12, 31, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.txtCardKeysA6.setFont(font)
        self.txtCardKeysA6.setMaxLength(3)
        self.txtCardKeysA6.setAlignment(QtCore.Qt.AlignCenter)
        self.txtCardKeysA6.setObjectName("txtCardKeysA6")
        self.txtCardKeysB3 = QtWidgets.QLineEdit(self.tbCardKeys)
        self.txtCardKeysB3.setGeometry(QtCore.QRect(145, 41, 30, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.txtCardKeysB3.setFont(font)
        self.txtCardKeysB3.setMaxLength(3)
        self.txtCardKeysB3.setAlignment(QtCore.Qt.AlignCenter)
        self.txtCardKeysB3.setObjectName("txtCardKeysB3")
        self.txtCardKeysB1 = QtWidgets.QLineEdit(self.tbCardKeys)
        self.txtCardKeysB1.setGeometry(QtCore.QRect(81, 41, 30, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.txtCardKeysB1.setFont(font)
        self.txtCardKeysB1.setMaxLength(3)
        self.txtCardKeysB1.setAlignment(QtCore.Qt.AlignCenter)
        self.txtCardKeysB1.setObjectName("txtCardKeysB1")
        self.txtCardKeysB6 = QtWidgets.QLineEdit(self.tbCardKeys)
        self.txtCardKeysB6.setGeometry(QtCore.QRect(241, 41, 31, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.txtCardKeysB6.setFont(font)
        self.txtCardKeysB6.setMaxLength(3)
        self.txtCardKeysB6.setAlignment(QtCore.Qt.AlignCenter)
        self.txtCardKeysB6.setObjectName("txtCardKeysB6")
        self.txtCardKeysB2 = QtWidgets.QLineEdit(self.tbCardKeys)
        self.txtCardKeysB2.setGeometry(QtCore.QRect(113, 41, 30, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.txtCardKeysB2.setFont(font)
        self.txtCardKeysB2.setMaxLength(3)
        self.txtCardKeysB2.setAlignment(QtCore.Qt.AlignCenter)
        self.txtCardKeysB2.setObjectName("txtCardKeysB2")
        self.txtCardKeysB4 = QtWidgets.QLineEdit(self.tbCardKeys)
        self.txtCardKeysB4.setGeometry(QtCore.QRect(177, 41, 30, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.txtCardKeysB4.setFont(font)
        self.txtCardKeysB4.setMaxLength(3)
        self.txtCardKeysB4.setAlignment(QtCore.Qt.AlignCenter)
        self.txtCardKeysB4.setObjectName("txtCardKeysB4")
        self.txtCardKeysB5 = QtWidgets.QLineEdit(self.tbCardKeys)
        self.txtCardKeysB5.setGeometry(QtCore.QRect(209, 41, 30, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.txtCardKeysB5.setFont(font)
        self.txtCardKeysB5.setMaxLength(3)
        self.txtCardKeysB5.setAlignment(QtCore.Qt.AlignCenter)
        self.txtCardKeysB5.setObjectName("txtCardKeysB5")
        self.tabWidget.addTab(self.tbCardKeys, "")
        self.tbReaderKey = QtWidgets.QWidget()
        self.tbReaderKey.setObjectName("tbReaderKey")
        self.chkHexReaderKey = QtWidgets.QCheckBox(self.tbReaderKey)
        self.chkHexReaderKey.setGeometry(QtCore.QRect(69, 60, 70, 17))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        self.chkHexReaderKey.setFont(font)
        self.chkHexReaderKey.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.chkHexReaderKey.setObjectName("chkHexReaderKey")
        self.btnFormatReadKey = QtWidgets.QPushButton(self.tbReaderKey)
        self.btnFormatReadKey.setGeometry(QtCore.QRect(300, 21, 181, 51))
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
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.btnFormatReadKey.setFont(font)
        self.btnFormatReadKey.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnFormatReadKey.setAutoFillBackground(False)
        self.btnFormatReadKey.setStyleSheet("background-color: rgb(223, 223, 223);")
        self.btnFormatReadKey.setFlat(False)
        self.btnFormatReadKey.setObjectName("btnFormatReadKey")
        self.lblKeyIndex = QtWidgets.QLabel(self.tbReaderKey)
        self.lblKeyIndex.setGeometry(QtCore.QRect(149, 60, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        self.lblKeyIndex.setFont(font)
        self.lblKeyIndex.setObjectName("lblKeyIndex")
        self.txtKeyIndex = QtWidgets.QLineEdit(self.tbReaderKey)
        self.txtKeyIndex.setGeometry(QtCore.QRect(226, 59, 31, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.txtKeyIndex.setFont(font)
        self.txtKeyIndex.setAlignment(QtCore.Qt.AlignCenter)
        self.txtKeyIndex.setReadOnly(True)
        self.txtKeyIndex.setObjectName("txtKeyIndex")
        self.txtReaderKey5 = QtWidgets.QLineEdit(self.tbReaderKey)
        self.txtReaderKey5.setGeometry(QtCore.QRect(196, 22, 30, 20))
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
        self.txtReaderKey6.setGeometry(QtCore.QRect(228, 22, 31, 20))
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
        self.txtReaderKey3.setGeometry(QtCore.QRect(132, 22, 30, 20))
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
        self.txtReaderKey1.setGeometry(QtCore.QRect(68, 22, 30, 20))
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
        self.txtReaderKey4.setGeometry(QtCore.QRect(164, 22, 30, 20))
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
        self.txtReaderKey2.setGeometry(QtCore.QRect(100, 22, 30, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.txtReaderKey2.setFont(font)
        self.txtReaderKey2.setMaxLength(3)
        self.txtReaderKey2.setAlignment(QtCore.Qt.AlignCenter)
        self.txtReaderKey2.setObjectName("txtReaderKey2")
        self.tabWidget.addTab(self.tbReaderKey, "")
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
        self.mdiArea.setGeometry(QtCore.QRect(10, 288, 620, 370))
        self.mdiArea.setObjectName("mdiArea")
        self.lblCardStatus = QtWidgets.QLabel(self.centralwidget)
        self.lblCardStatus.setGeometry(QtCore.QRect(1, 668, 171, 21))
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
        self.lblCardFnExplain.setGeometry(QtCore.QRect(250, 668, 391, 21))
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
        self.lblCardFnResult.setGeometry(QtCore.QRect(172, 668, 80, 21))
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
        self.frmCaption = QtWidgets.QFrame(self.centralwidget)
        self.frmCaption.setGeometry(QtCore.QRect(10, 288, 621, 30))
        self.frmCaption.setAutoFillBackground(False)
        self.frmCaption.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frmCaption.setFrameShape(QtWidgets.QFrame.Box)
        self.frmCaption.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frmCaption.setObjectName("frmCaption")
        self.txtCaption = QtWidgets.QLineEdit(self.frmCaption)
        self.txtCaption.setGeometry(QtCore.QRect(5, 4, 611, 20))
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 637, 20))
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
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "uFr Advanced"))
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
        self.btnReaderUISignal.setText(_translate("MainWindow", "Reader UI Signal"))
        self.btnReaderReset.setText(_translate("MainWindow", "Reader Reset"))
        self.btnSoftRestart.setText(_translate("MainWindow", "Soft Restart"))
        self.lblKeyA.setText(_translate("MainWindow", "Key A"))
        self.lblKeyB.setText(_translate("MainWindow", "Key B"))
        self.chkHexCardKeys.setText(_translate("MainWindow", "Hex"))
        self.btnFormatCardKeys.setText(_translate("MainWindow", "FORMAT CARD KEYS"))
        self.lblSectorsFormat.setText(_translate("MainWindow", "Sectors Formatting"))
        self.txtCardKeysA1.setText(_translate("MainWindow", "255"))
        self.txtCardKeysA2.setText(_translate("MainWindow", "255"))
        self.txtCardKeysA3.setText(_translate("MainWindow", "255"))
        self.txtCardKeysA4.setText(_translate("MainWindow", "255"))
        self.txtCardKeysA5.setText(_translate("MainWindow", "255"))
        self.txtCardKeysA6.setText(_translate("MainWindow", "255"))
        self.txtCardKeysB3.setText(_translate("MainWindow", "255"))
        self.txtCardKeysB1.setText(_translate("MainWindow", "255"))
        self.txtCardKeysB6.setText(_translate("MainWindow", "255"))
        self.txtCardKeysB2.setText(_translate("MainWindow", "255"))
        self.txtCardKeysB4.setText(_translate("MainWindow", "255"))
        self.txtCardKeysB5.setText(_translate("MainWindow", "255"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tbCardKeys), _translate("MainWindow", "New Card Keys"))
        self.chkHexReaderKey.setText(_translate("MainWindow", "Hex"))
        self.btnFormatReadKey.setText(_translate("MainWindow", "FORMAT READER KEY"))
        self.lblKeyIndex.setText(_translate("MainWindow", "Key Index"))
        self.txtKeyIndex.setText(_translate("MainWindow", "0"))
        self.txtReaderKey5.setText(_translate("MainWindow", "255"))
        self.txtReaderKey6.setText(_translate("MainWindow", "255"))
        self.txtReaderKey3.setText(_translate("MainWindow", "255"))
        self.txtReaderKey1.setText(_translate("MainWindow", "255"))
        self.txtReaderKey4.setText(_translate("MainWindow", "255"))
        self.txtReaderKey2.setText(_translate("MainWindow", "255"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tbReaderKey), _translate("MainWindow", "New Reader Key"))
        self.lblCardStatus.setText(_translate("MainWindow", "CARD STATUS"))
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

