"""
 @author: Vladan S
 @organization: D-Logic  
 @version: 2.5
"""

import sys
import os
import threading
import time
import re
from ctypes import *
import platform
import webbrowser

from Constants import *
from ErrCodes import *
from Functions import * 
from uFrAdvancedForm import*

from LinearReadWrite import*
from BlockReadWrite import*
from BlockInSectorReadWrite import *
from ValueBlockReadWrite import*
from ValueBlockInSectorReadWrite import*
from ValueBlockIncrDecr import*
from ValueBlockInSectorIncrDecr import *
from LinearFormatCard import *
from SectorTrailerWrite import*
from ViewAll import*


from PyQt5.QtWidgets import QMainWindow,QDialog, QAction, QApplication,QCheckBox,QComboBox,QMessageBox
from PyQt5.QtCore import QCoreApplication,Qt
from PyQt5.Qt import QLineEdit,QEvent
from PyQt5 import  QtGui



class uFAdvanced(QMainWindow,threading.Thread):
    """
     main class
    
    """
     
    def __init__(self):
        super().__init__()
        self.__conn = False       
        self.__dlogicCardType = c_uint8()
        self.__functionOn = False
        self.__readerOn = False
        self.mySO = Functions.GetPlatform()
        self.initUI()
        
        self.LR = LinearRW()
        self.BRW = BlockRW()
        self.BRWInS = BlockRWInSector()
        self.VBRW = ValueBlockReadWrite()
        self.VBISRW = ValueBlockInSectorReadWrite()
        self.VBINCDEC = ValueBlockIncrDecr()
        self.VBINSINCDEC = ValueBlockIncrDecr()
        self.LFC = LinearFormatCard()
        self.STW = SectorTrailerWrite()
        self.VALL = ViewAll()
        
        self.sub = QtWidgets.QMdiSubWindow()
        self.sub.setMinimumSize(620, 400)
        
        self.FillKeyIndex(KEY_INDEX_MAX)
        
        t = threading.Thread(target=self.ThreadStart)
        t.daemon = True
        t.start()
        
    def initUI(self):        
        self.ui = Ui_MainWindow()
        self.center()
        self.ui.setupUi(self)
        self.ui.btnReaderUISignal.clicked.connect(self.GetReaderUISignal)
        self.ui.btnFormatReadKey.clicked.connect(self.FormatReaderKey)        
        self.ui.btnSaveUserData.clicked.connect(self.SaveUserData)
        self.ui.btnReaderReset.clicked.connect(self.ReaderReset)
        self.ui.btnReaderReset.clicked.connect(self.SoftRestart)
        
        self.ui.actionLinear_Read_Write.triggered.connect(self.LinearReadWrite)
        self.ui.actionBlock_Read_Write.triggered.connect(self.BlockReadWrite)
        self.ui.actionBlockInSector_Read_Write.triggered.connect(self.BlockInSectorReadWrite)
        self.ui.actionValueBlock_Read_Write.triggered.connect(self.ValueBlockReadWrite)
        self.ui.actionValueBlockInSector_Read_Write.triggered.connect(self.ValueBlockInSectorReadWrite)
        self.ui.actionValueBlock_Increment_Decrement.triggered.connect(self.ValueBlockIncrDecr)
        self.ui.actionValueBlockInSector_Increment_Decrement.triggered.connect(self.ValueBlockInSectorIncrDecr)
        self.ui.actionLinearFormat_Card.triggered.connect(self.LinearFormatCard)
        self.ui.actionSector_Trailer_Write.triggered.connect(self.SectorTrailerWrite)
        self.ui.actionView_All.triggered.connect(self.ViewAll)
        
        
        
        self.ui.actionReader_Hardware_Firmvare_version.triggered.connect(self.ReaderHFversion)
        self.ui.actionExit.triggered.connect(self.myclose)
        
        
        self.ui.chkHexReaderKey.stateChanged.connect(self.ReaderKeyCheckBoxToHex)
        
        self.ui.txtReaderKey1.textEdited.connect(self.ReaderRegKey)
        self.ui.txtReaderKey1.installEventFilter(self)        
        self.ui.txtReaderKey2.textEdited.connect(self.ReaderRegKey)
        self.ui.txtReaderKey2.installEventFilter(self)
        self.ui.txtReaderKey3.textEdited.connect(self.ReaderRegKey)
        self.ui.txtReaderKey3.installEventFilter(self)
        self.ui.txtReaderKey4.textEdited.connect(self.ReaderRegKey)
        self.ui.txtReaderKey4.installEventFilter(self)
        self.ui.txtReaderKey5.textEdited.connect(self.ReaderRegKey)
        self.ui.txtReaderKey5.installEventFilter(self)
        self.ui.txtReaderKey6.textEdited.connect(self.ReaderRegKey)
        self.ui.txtReaderKey6.installEventFilter(self)
        
        self.ui.linkLabel.mousePressEvent = self.OpenURL
 
    def myclose(self):
        QApplication.closeAllWindows()
            
    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())    
    
    def CloseSubWin(self):
        self.ui.mdiArea.removeSubWindow(self.sub)
    
    def OpenURL(self, event):
        webbrowser.open(self.ui.linkLabel.text())
        
    
    def FillKeyIndex(self,count):
        for n in range(0,count):
            self.ui.cboKeyIndex.addItem(str(n))
    
    def ReaderHFversion(self):
        """
          Reader hardware and firmware version
        """
        if  Functions.FunctionOn == True or Functions.ReaderOn == True:return
        Functions.FunctionOn = True
        try: 
            readerHardVerMinor = c_byte()
            readerHardVerMajor = c_byte()
            readerFirmVerMinor = c_byte()
            readerFirmVerMajor = c_byte()
            self.mySO.GetReaderHardwareVersion(byref(readerHardVerMajor),byref(readerHardVerMinor));
            self.mySO.GetReaderFirmwareVersion(byref(readerFirmVerMajor),byref(readerFirmVerMinor));
            info = "Hardware version :" + str(readerHardVerMajor.value) + '.' + str(readerHardVerMinor.value) + '\n' + \
                   "Firmware version :" + str(readerFirmVerMajor.value) + '.' + str(readerFirmVerMinor.value)
            
            QtWidgets.QMessageBox.information(self,'Info',info,QtWidgets.QMessageBox.Ok)
         
        finally:
            Functions.FunctionOn = False
        
    
    
    
    
    def ReaderReset(self):
        """
          Reader Reset
        """
        if  Functions.FunctionOn == True or Functions.ReaderOn == True:return
        Functions.FunctionOn = True
        try:            
            self.mySO.ReaderReset         
        finally:
            Functions.FunctionOn = False
           
    
   
    def SoftRestart(self):
        """
          Soft Restart
        """
        if  Functions.FunctionOn == True or Functions.ReaderOn == True:return
        Functions.FunctionOn = True
        try:      
            self.mySO.ReaderSoftRestart            
        finally:
            Functions.FunctionOn = False
            
                    
        
        
        
    def SaveUserData(self):
        """
          Save user Data
        """
        if  Functions.FunctionOn == True or Functions.ReaderOn == True:return
        Functions.FunctionOn = True
        try:            
            fnResult = c_ulong()
            userData = self.ui.txtNewUserData.text()
            userDataConv = str.encode(userData)
        
            fnResult = self.mySO.WriteUserData(userDataConv)
            if fnResult == DL_OK:            
                Functions.ReaderUISignal(FUNCT_LIGHT_OK,FUNCT_SOUND_OK)
            else:                           
                Functions.ReaderUISignal(FUNCT_LIGHT_ERROR,FUNCT_SOUND_ERROR) 
        finally:
            Functions.FunctionOn = False
    
    
    
    def DecHexCheckBox(self,txtName,QWidget,state):
        myLE = QLineEdit()
        nO   = 1
        if state == Qt.Checked:                  
            for le in QWidget.children():
                if isinstance(myLE, QLineEdit) and le.objectName() == txtName + str(nO) :
                    le.setText(str('%0.2X' % int(le.text())))
                    nO +=1
        
        if state == Qt.Unchecked:
            for le in QWidget.children():
                if isinstance(myLE, QLineEdit) and le.objectName() == txtName + str(nO) :
                    le.setText(str(int(le.text(),16)))
                    nO +=1    
    
    
    
    def ReaderKeyCheckBoxToHex(self,state):        
        self.DecHexCheckBox("txtReaderKey", self.ui.tbReaderKey, state)
            
   
     
    def eventFilter(self, o, ev): 
        if ev.type() == QEvent.FocusIn:                            
            if self.ui.chkHexReaderKey.checkState() == Qt.Checked: 
                o.setMaxLength(2)
            else:
                o.setMaxLength(3)
            return False            
        if ev.type() == QEvent.FocusOut: 
            if o.text() == '' : o.undo()                
            if self.ui.chkHexReaderKey.checkState() == Qt.Checked :return False 
            elif int(o.text())>255 :                                    
                o.undo()                                        
                #o.setMaxLength(3)                                                    
            return False                                                             
        return QtCore.QObject.eventFilter(self, o,ev)    
        
        
  
    
    def ReaderRegKey(self):        
        sender  = self.sender()             
        sendText = sender.text()
        if (self.ui.chkHexReaderKey.checkState() == Qt.Unchecked or self.ui.chkHexReaderKey.checkState() == Qt.Unchecked):             
            match = re.search('[a-zA-Z]',sendText)
            if match:                 
                sender.backspace()  
    
    
    def ReadKeys(self,txtName,QWidget,state):
        le = QLineEdit()        
        i  = 1        
        lek = [] 
        if state == Qt.Checked:       
            for le in QWidget.children():                        
                if isinstance(le,QLineEdit) and le.objectName() == txtName + str(i):                
                    lek.append(int(le.text(),16))                                    
                    i+=1
                   
        if state == Qt.Unchecked:
            for le in QWidget.children():                        
                if isinstance(le,QLineEdit) and le.objectName() == txtName + str(i):                                  
                    lek.append(int(le.text()))                                        
                    i+=1
        return lek
                     
   
            
    
    def FormatReaderKey(self):
        """
          Format reader keys
        """
        if  Functions.FunctionOn == True or Functions.ReaderOn == True:return
        Functions.FunctionOn = True
        
        keyR = (c_uint8 *6)()
        pReaderKey = POINTER(c_uint8)
        keyIndex   = c_ubyte()
        c   = 0        
        fnResult   = c_ulong()
        
        try:             
            lKeyR = self.ReadKeys("txtReaderKey", self.ui.tbReaderKey,self.ui.chkHexReaderKey.checkState())                        
            for n in lKeyR:
                keyR[c] = n                                                                             
                c+=1                   
            pReaderKey = keyR                                                     
          
            fnResult = self.mySO.ReaderKeyWrite(pReaderKey,keyIndex)            
            if fnResult == DL_OK:                
                #self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_OK,FUNCT_SOUND_OK)
            else:                
                #self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_ERROR,FUNCT_SOUND_ERROR)
        finally:
            Functions.FunctionOn = False
    
    def ThreadStart(self):
        
        while True:               
            self.MainLoop()
            time.sleep(TIME_SLEEP)
    

    
    def SetReaderStatus(self,connValue,errCodeValue,errExplain):
        self.ui.lblCONN.setText(connValue)
        self.ui.lblFnResult.setText(errCodeValue)
        self.ui.lblFnExplain.setText(errExplain)
    
    def SetCardStatus(self,errCodeValue,errExplain):
        self.ui.lblCardFnResult.setText(hex(errCodeValue))
        self.ui.lblCardFnExplain.setText(errExplain) 
        
    
   
    
    def GetReaderUISignal(self):
        lightValue = self.ui.cboLightMode.currentIndex()
        soundValue = self.ui.cboSoundMode.currentIndex()
        Functions.ReaderUISignal(lightValue, soundValue)
    
    
    def closeEvent(self,event):
        reply = QtWidgets.QMessageBox.question(self,'Message',"Are you sure you want to quit?",QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if(reply == QtWidgets.QMessageBox.Yes):
            event.accept()
            sys.exit(0)
        else:
            event.ignore()
    
    def SetMyMenuItems(self,AValue):
        #self.ui.actionLinear_Read_Write.setEnabled(AValue)
        #self.ui.actionBlock_Read_Write.setEnabled(AValue)
        self.ui.actionBlockInSector_Read_Write.setEnabled(AValue)
        self.ui.actionValueBlock_Read_Write.setEnabled(AValue)
        self.ui.actionValueBlockInSector_Read_Write.setEnabled(AValue)
        self.ui.actionValueBlock_Increment_Decrement.setEnabled(AValue)
        self.ui.actionValueBlockInSector_Increment_Decrement.setEnabled(AValue)
        self.ui.actionLinearFormat_Card.setEnabled(AValue)
        self.ui.actionSector_Trailer_Write.setEnabled(AValue)
        #self.ui.actionView_All.triggered.connect(self.ViewAll)
    
    
    def MainLoop(self):
        
        if Functions.FunctionOn == True : return
        
        readerType = c_uint32()
        readerSerial = c_uint32()
        cardType = c_uint8()
        #cardSerial = c_uint32()
        cardUID = (c_ubyte * 9)()
        cardUIDSize = c_uint8()
        userData = (c_uint8 * 15)() 
        #pUserData = POINTER(c_char)       
        fnResult = c_ulong()
        c = str()
        
                    
        
        Functions.ReaderOn = True 
        
        if self.__conn != True:
            fnResult = self.mySO.ReaderOpen()
            if fnResult == DL_OK:
                self.__conn = True
                self.SetReaderStatus('CONNECTED', hex(fnResult),UFCODER_ERROR_CODES[fnResult])
            else:
                self.__conn = False
                self.ui.txtReaderType.setText(None)
                self.ui.txtReaderSerial.setText(None)
                self.ui.txtCardType.setText(None)
                self.ui.txtCardSerial.setText(None)
                self.ui.txtUIDSize.setText(None)
                self.SetReaderStatus('NOT CONNECTION', hex(fnResult),UFCODER_ERROR_CODES[fnResult])    
        
        if self.__conn:
            fnResult = self.mySO.GetReaderType(byref(readerType))           
            if fnResult == DL_OK:
                b = hex(readerType.value)
                self.ui.txtReaderType.setText(b.upper())
                fnResult = self.mySO.GetReaderSerialNumber(byref(readerSerial))
                if fnResult == DL_OK:
                    b = hex(readerSerial.value)
                  
                    self.ui.txtReaderSerial.setText(b.upper())
                    fnResult = self.mySO.GetCardIdEx(byref(cardType),cardUID,byref(cardUIDSize))
                    if fnResult == DL_OK:
                        fnResult = self.mySO.GetDlogicCardType(byref(self.__dlogicCardType))
                        cardType = self.__dlogicCardType.value
                        Functions.CardType = cardType
                        
                        if cardType == DL_NTAG_203 or cardType == DL_MIFARE_ULTRALIGHT or cardType == DL_MIFARE_ULTRALIGHT_C:
                            self.SetMyMenuItems(False)
                        else:
                            self.SetMyMenuItems(True)
                     
                        if fnResult == DL_OK:
                            for n in range(cardUIDSize.value):
                                c +=  '%0.2x' % cardUID[n]
                                
                            #cardType = hex(self.__dlogicCardType.value)
                            uidSize  = hex(cardUIDSize.value)   
                            self.ui.txtCardSerial.setText('0x'+c.upper())
                            self.ui.txtCardType.setText(hex(cardType).upper())
                            self.ui.txtUIDSize.setText(uidSize.upper())                          
                            
                            fnResult = self.mySO.ReadUserData(userData)                           
                            self.ui.txtUserData.setText(''.join([chr(i) for i in userData]))
                            
                    else:
                        self.ui.txtCardSerial.setText(None)
                        self.ui.txtCardType.setText(None)
                        self.ui.txtUIDSize.setText(None)
                        self.SetMyMenuItems(True)
                                    
                    self.SetCardStatus(fnResult,UFCODER_ERROR_CODES[fnResult])        
                
            else:
                self.mySO.ReaderClose()
                self.__conn = False
                                
       
        Functions.ReaderOn = False 
        
    
    
    
    def LinearReadWrite(self):
        self.CloseSubWin()  
        if self.ui.mdiArea.activeSubWindow() is None:            
            self.sub.setWidget(self.LR)                    
            self.ui.mdiArea.addSubWindow(self.sub)
            self.ui.txtCaption.setText("Linear Read/Write (AKM1,AKM2,PK)")
            self.sub.showNormal()
    
    def BlockReadWrite(self):
        self.CloseSubWin()
        if self.ui.mdiArea.activeSubWindow() is None:            
            self.sub.setWidget(self.BRW)                    
            self.ui.mdiArea.addSubWindow(self.sub)
            self.ui.txtCaption.setText("Block Read/Write (AKM1,AKM2,PK)")
            self.sub.showNormal()
    
    def BlockInSectorReadWrite(self):
        self.CloseSubWin()
        if self.ui.mdiArea.activeSubWindow() is None:            
            self.sub.setWidget(self.BRWInS)                    
            self.ui.mdiArea.addSubWindow(self.sub)
            self.ui.txtCaption.setText("BlockInSector Read/Write (AKM1,AKM2,PK)")
            self.sub.showNormal()
        
    def ValueBlockReadWrite(self):
        self.CloseSubWin()
        if self.ui.mdiArea.activeSubWindow() is None:            
            self.sub.setWidget(self.VBRW)                    
            self.ui.mdiArea.addSubWindow(self.sub)
            self.ui.txtCaption.setText("ValueBlock Read/Write (AKM1,AKM2,PK)")
            self.sub.showNormal()  
            
    def ValueBlockInSectorReadWrite(self):
        self.CloseSubWin()
        if self.ui.mdiArea.activeSubWindow() is None:            
            self.sub.setWidget(self.VBISRW)                    
            self.ui.mdiArea.addSubWindow(self.sub)
            self.ui.txtCaption.setText("ValueBlock InSector Read/Write (AKM1,AKM2,PK)")
            self.sub.showNormal()  
            
    def ValueBlockIncrDecr(self):
        self.CloseSubWin()
        if self.ui.mdiArea.activeSubWindow() is None:            
            self.sub.setWidget(self.VBINCDEC)                    
            self.ui.mdiArea.addSubWindow(self.sub)
            self.ui.txtCaption.setText("ValueBlock Increment/Decrement (AKM1,AKM2,PK)")
            self.sub.showNormal()
            
    def ValueBlockInSectorIncrDecr(self):
        self.CloseSubWin()
        if self.ui.mdiArea.activeSubWindow() is None:            
            self.sub.setWidget(self.VBINSINCDEC)                    
            self.ui.mdiArea.addSubWindow(self.sub)
            self.ui.txtCaption.setText("ValueBlock InSector Inc/Dec (AKM1,AKM2,PK)")
            self.sub.showNormal()
            
    def LinearFormatCard(self):
        self.CloseSubWin()
        if self.ui.mdiArea.activeSubWindow() is None:            
            self.sub.setWidget(self.LFC)                    
            self.ui.mdiArea.addSubWindow(self.sub)
            self.ui.txtCaption.setText("Linear Format Card (AKM1,AKM2,PK)")
            self.sub.showNormal()
    
    def SectorTrailerWrite(self):
        self.CloseSubWin()
        if self.ui.mdiArea.activeSubWindow() is None:            
            self.sub.setWidget(self.STW)                    
            self.ui.mdiArea.addSubWindow(self.sub)
            self.ui.txtCaption.setText("Sector Trailer Write (AKM1,AKM2,PK)")
            self.sub.showNormal()
    
    
    def ViewAll(self):
        self.CloseSubWin()
        if self.ui.mdiArea.activeSubWindow() is None:            
            self.sub.setWidget(self.VALL)                    
            self.ui.mdiArea.addSubWindow(self.sub)
            self.ui.txtCaption.setText("View All")
            self.sub.showNormal()
                    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    uFA = uFAdvanced()
    uFA.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
    uFA.show()
    sys.exit(app.exec_()) 
     


