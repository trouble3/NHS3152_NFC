

'''
@author:       Vladan S
@organization: D-Logic
@version:      2.5
'''


import sys
import os
import threading
import time
import Constants,ErrCodes
from uFSimpleForm import *
import webbrowser
from platform import *
from ctypes import *
from PyQt5.QtWidgets import QMainWindow, QAction, QApplication,QMessageBox,QCheckBox
from PyQt5.QtCore import QCoreApplication,Qt
from Constants import *    
from PyQt5.Qt import QLineEdit,QEvent, QWidget
from Constants import *




class uFSimple(QMainWindow,threading.Thread):
    
    def __init__(self):
        super().__init__()        
        self.initUI()
        self.myLib = self.GetPlatform()
        self.__conn = False
        self.__readerOn = False
        self.__functionOn = False
        self.__dlogicCardType = c_uint8()
        
        t = threading.Thread(target=self.ThreadStart)
        t.daemon = True
        t.start()
        
        
        self.ui.mnuExit.triggered.connect(self.myClose)
        self.ui.btnLinearRead.clicked.connect(self.LinearRead)        
        self.ui.btnReaderUISignal.clicked.connect(self.GetReaderUISignal)
        self.ui.txtLinearWrite.textChanged.connect(self.LenLinearWriteText)
        self.ui.btnLinearWrite.clicked.connect(self.LinearWrite)
        self.ui.linkLabel.mousePressEvent = self.OpenURL
        
        self.ui.chkHexCardKeys.stateChanged.connect(self.CardKeysCheckBoxToHex)
                
        self.ui.chkHexReaderKey.stateChanged.connect(self.ReaderKeyCheckBoxToHex)
        
        self.ui.btnFormatCardKeys.clicked.connect(self.FormatCardKeys)
        self.ui.btnFormatReadKey.clicked.connect(self.FormatReaderKey)
           
        self.ui.txtCardKeysA1.textEdited.connect(self.CardKeysReg)
        self.ui.txtCardKeysA1.installEventFilter(self)        
        self.ui.txtCardKeysA2.textEdited.connect(self.CardKeysReg)
        self.ui.txtCardKeysA2.installEventFilter(self)
        self.ui.txtCardKeysA3.textEdited.connect(self.CardKeysReg)
        self.ui.txtCardKeysA3.installEventFilter(self)
        self.ui.txtCardKeysA4.textEdited.connect(self.CardKeysReg)
        self.ui.txtCardKeysA4.installEventFilter(self)
        self.ui.txtCardKeysA5.textEdited.connect(self.CardKeysReg)
        self.ui.txtCardKeysA5.installEventFilter(self)
        self.ui.txtCardKeysA6.textEdited.connect(self.CardKeysReg)
        self.ui.txtCardKeysA6.installEventFilter(self)
        
        self.ui.txtCardKeysB1.textEdited.connect(self.CardKeysReg)
        self.ui.txtCardKeysB1.installEventFilter(self)
        self.ui.txtCardKeysB2.textEdited.connect(self.CardKeysReg)
        self.ui.txtCardKeysB2.installEventFilter(self)
        self.ui.txtCardKeysB3.textEdited.connect(self.CardKeysReg)
        self.ui.txtCardKeysB3.installEventFilter(self)
        self.ui.txtCardKeysB4.textEdited.connect(self.CardKeysReg)
        self.ui.txtCardKeysB4.installEventFilter(self)
        self.ui.txtCardKeysB5.textEdited.connect(self.CardKeysReg)
        self.ui.txtCardKeysB5.installEventFilter(self)
        self.ui.txtCardKeysB6.textEdited.connect(self.CardKeysReg)
        self.ui.txtCardKeysB6.installEventFilter(self)
        
        self.ui.txtReaderKey1.textEdited.connect(self.CardKeysReg)
        self.ui.txtReaderKey1.installEventFilter(self)        
        self.ui.txtReaderKey2.textEdited.connect(self.CardKeysReg)
        self.ui.txtReaderKey2.installEventFilter(self)
        self.ui.txtReaderKey3.textEdited.connect(self.CardKeysReg)
        self.ui.txtReaderKey3.installEventFilter(self)
        self.ui.txtReaderKey4.textEdited.connect(self.CardKeysReg)
        self.ui.txtReaderKey4.installEventFilter(self)
        self.ui.txtReaderKey5.textEdited.connect(self.CardKeysReg)
        self.ui.txtReaderKey5.installEventFilter(self)
        self.ui.txtReaderKey6.textEdited.connect(self.CardKeysReg)
        self.ui.txtReaderKey6.installEventFilter(self)
    
    
    def initUI(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
     
     
    def myClose(self):
        QApplication.closeAllWindows()
            
    def closeEvent(self,event):
        reply = QtWidgets.QMessageBox.question(self,'Message',"Are you sure you want to quit?",QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if(reply == QtWidgets.QMessageBox.Yes):
            event.accept()
            sys.exit(0)
        else:
            event.ignore()
                
    def OpenURL(self, event):    
        webbrowser.open(self.ui.linkLabel.text())
    
    def GetPlatform(self):
           
        if sys.platform.startswith('win32'):
            return windll.LoadLibrary(os.getcwd()+'\\ufr-lib\\windows\\x86\\uFCoder-x86.dll')
        elif sys.platform.startswith('linux'):
            return cdll.LoadLibrary(os.getcwd()+'//ufr-lib//linux//x86_64//libuFCoder-x86_64.so')
        
    
    
   
    
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
    
    
    def CardKeysCheckBoxToHex(self,state):
                            
        self.DecHexCheckBox("txtCardKeysA",self.ui.tbCardKeys, state) 
        self.DecHexCheckBox("txtCardKeysB",self.ui.tbCardKeys, state)                               
           
      
    def ReaderKeyCheckBoxToHex(self,state):        
        self.DecHexCheckBox("txtReaderKey", self.ui.tbReaderKey, state)
            
   
    
    def eventFilter(self, o, ev):  
            if ev.type() == QEvent.FocusIn:                            
                if self.ui.chkHexReaderKey.checkState() == Qt.Checked or self.ui.chkHexCardKeys.checkState() == Qt.Checked: 
                    o.setMaxLength(2)
                else:
                    o.setMaxLength(3)
                return False   
                     
            if ev.type() == QEvent.FocusOut: 
                if o.text() == '' : o.undo()                
                if self.ui.chkHexReaderKey.checkState() == Qt.Checked or self.ui.chkHexCardKeys.checkState() == Qt.Checked:                     
                    return False                 
                elif int(o.text())>255 :                                    
                    o.undo()                                                                                                            
                return False                     
            #else:                               
            return QtCore.QObject.eventFilter(self, o,ev)     
        
        
  
    
    def CardKeysReg(self):        
        sender  = self.sender()             
        sendText = sender.text()
        
        if (self.ui.chkHexReaderKey.checkState() == Qt.Checked or self.ui.chkHexCardKeys.checkState() == Qt.Checked):                    
            match = re.search('[g-zG-Z]', sendText)
            if match:
                sender.backspace()
        elif (self.ui.chkHexReaderKey.checkState() == Qt.Unchecked or self.ui.chkHexCardKeys.checkState() == Qt.Unchecked):             
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
    
      
                     
    def FormatCardKeys(self):
        """
          Format card keys
        """
        if self.FunctionOn or self.ReaderOn:return
        
        self.FunctionOn = True
        
        blockAccessBits = c_uint8()
        sectorTrailersAccessBits = c_uint8()
        trailersByte9 = c_uint8()
        sectorsFormatted = c_uint8()
        c = 0        
        authMode     = c_uint8()
        keyIndex     = c_uint8()
        keyA  = (c_ubyte * 6)()
        keyB = (c_ubyte * 6)() 
        pKeyA = POINTER(c_ubyte)
        pKeyB = POINTER(c_ubyte) 
        fnResult = c_ulong()
        
        try:
            blockAccessBits = 0
            sectorTrailersAccessBits = 1
            trailersByte9 = 45            
            keyIndex = int(self.ui.txtKeyIndex.text())
            authMode  = MIFARE_AUTHENT1A  if self.ui.rbAUTH1A.isChecked() else MIFARE_AUTHENT1B
            
            lKeyA = self.ReadKeys("txtCardKeysA", self.ui.tbCardKeys,self.ui.chkHexCardKeys.checkState())
            lKeyB = self.ReadKeys("txtCardKeysB", self.ui.tbCardKeys,self.ui.chkHexCardKeys.checkState())                        
           
            for a in lKeyA:
                keyA[c] = a                
                c += 1
                                        
            for b in lKeyB:
                keyB[c] = b                
                c += 1
             
            pKeyA = keyA
            pKeyB = keyB
             
            pKeyA = self.ReadKeys("txtCardKeysA", self.ui.tbCardKeys,self.ui.chkHexCardKeys.checkState())
            pKeyB = self.ReadKeys("txtCardKeysB", self.ui.tbCardKeys,self.ui.chkHexCardKeys.checkState())
                        
            fnResult = self.myLib.LinearFormatCard(pKeyA,blockAccessBits,sectorTrailersAccessBits,trailersByte9,pKeyB,byref(sectorsFormatted),authMode,keyIndex)
           
            if fnResult == DL_OK:
                self.ui.txtSectorsFormat.setText(str(sectorsFormatted.value))
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                self.ReaderUISignal(FUNCT_LIGHT_OK,FUNCT_SOUND_OK)
            else:
                self.ui.txtSectorsFormat.setText(str(sectorsFormatted.value))
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                self.ReaderUISignal(FUNCT_LIGHT_ERROR,FUNCT_SOUND_ERROR)                        
        finally:
            self.FunctionOn = False
            
    
    def FormatReaderKey(self):
        """
          Format reader keys
        """
        if self.FunctionOn or self.ReaderOn:return        
        self.FunctionOn = True
        
        keyR       = (c_ubyte *6)()
        pReaderKey = POINTER(c_byte)
        keyIndex   = c_ubyte()
        c          = 0        
        fnResult   = c_ulong()
        
        try:
            lKeyR = self.ReadKeys("txtReaderKey", self.ui.tbReaderKey,self.ui.chkHexReaderKey.checkState())
            
            for rk in lKeyR:
                keyR[c] = rk               
                c += 1
                 
            pReaderKey = keyR
            
            fnResult = self.myLib.ReaderKeyWrite(pReaderKey,keyIndex)
            
            if fnResult == DL_OK:                
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                self.ReaderUISignal(FUNCT_LIGHT_OK,FUNCT_SOUND_OK)
            else:                
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                self.ReaderUISignal(FUNCT_LIGHT_ERROR,FUNCT_SOUND_ERROR)
        finally:
            self.FunctionOn = False
    
    
    
    
    def GetFunctionOn(self):
        return self.__functionOn
    
    def SetFunctionOn(self,value):
        self.__functionOn = value
    
        
        
            
    def GetReaderOn(self):
        return self.__readerOn
    
    def SetReaderOn(self,value):
        self.__readerOn = value
        
        
    FunctionOn = property(fget = GetFunctionOn,fset = SetFunctionOn)    
    
    ReaderOn = property(fget = GetReaderOn,fset = SetReaderOn)
    
    
    
     
    def ThreadStart(self):
        while True:
            self.MainLoop()
            time.sleep(0.8)
    

    
    def SetReaderStatus(self,connValue,errCodeValue,errExplain):
        self.ui.lblCONN.setText(connValue)
        self.ui.lblFnResult.setText(errCodeValue)
        self.ui.lblFnExplain.setText(errExplain)
    
    def SetCardStatus(self,errCodeValue,errExplain):
        self.ui.lblCardStatusValue.setText(hex(errCodeValue))
        self.ui.lblCardStatusExplain.setText(errExplain) 
        
    def SetFnStatus(self,fnValue,fnExplain):
        self.ui.lblFnErrorValue.setText(hex(fnValue))
        self.ui.lblFnErrorExplain.setText(fnExplain)       
    
    
    def ReaderUISignal(self,lightValue,soundValue):
        uiSignal = self.myLib.ReaderUISignal
        uiSignal.argtypes = (c_uint8,c_uint8)
        uiSignal.restype = c_int
        uiSignal(lightValue,soundValue) 
    
    def GetReaderUISignal(self):
        lightValue = self.ui.cboLightMode.currentIndex()
        soundValue = self.ui.cboSoundMode.currentIndex()
        self.ReaderUISignal(lightValue, soundValue)
    
    def LenLinearWriteText(self):
        self.ui.txtDataLengthWrite.setText(str(len(self.ui.txtLinearWrite.toPlainText())))
    
    
    
    
    
    def MainLoop(self):
        if self.FunctionOn: return
           
        readerType = c_uint32()
        readerSerial = c_uint32()
        cardType = c_uint8()
        cardSerial = c_uint32()
        cardUID = (c_ubyte * 9)()
        cardUIDSize = c_uint8()        
        fnResult = c_ulong()
        c = str()
                    
        self.ReaderOn = True        
        if self.__conn != True:
            fnResult = self.myLib.ReaderOpen()
            if fnResult == DL_OK:
                self.__conn = True
                self.SetReaderStatus('CONNECTED', hex(fnResult), ErrCodes.UFCODER_ERROR_CODES[fnResult])
            else:
                self.__conn = False
                self.ui.txtReaderType.setText(None)
                self.ui.txtReaderSerial.setText(None)
                self.ui.txtCardType.setText(None)
                self.ui.txtCardSerial.setText(None)
                self.ui.txtUIDSize.setText(None)
                self.SetReaderStatus('NOT CONNECTION', hex(fnResult), ErrCodes.UFCODER_ERROR_CODES[fnResult])    
        
        if self.__conn:
            fnResult = self.myLib.GetReaderType(byref(readerType))           
            if fnResult == DL_OK:
                b = hex(readerType.value)
                self.ui.txtReaderType.setText(b.upper())
                fnResult = self.myLib.GetReaderSerialNumber(byref(readerSerial))
                if fnResult == DL_OK:
                    b = hex(readerSerial.value) 
                    self.ui.txtReaderSerial.setText(b.upper())
                    fnResult = self.myLib.GetCardIdEx(byref(cardType),cardUID,byref(cardUIDSize))
                    if fnResult == DL_OK:
                        fnResult = self.myLib.GetDlogicCardType(byref(self.__dlogicCardType))
                        if fnResult == DL_OK:
                            for n in range(cardUIDSize.value):
                                c +=  '%0.2x' % cardUID[n]
                            
                            cardType = hex(self.__dlogicCardType.value)
                            uidSize  = hex(cardUIDSize.value)    
                            self.ui.txtCardSerial.setText('0x'+c.upper())
                            self.ui.txtCardType.setText(cardType.upper())
                            self.ui.txtUIDSize.setText(uidSize.upper())
                    else:
                        self.ui.txtCardSerial.setText(None)
                        self.ui.txtCardType.setText(None)
                        self.ui.txtUIDSize.setText(None)
                                    
                    self.SetCardStatus(fnResult, ErrCodes.UFCODER_ERROR_CODES[fnResult])        
                
            else:
                self.myLib.ReaderClose()
                self.__conn = False
                                
        self.ReaderOn = False
         

    def LinearRead(self):
        # if self.FunctionOn or self.ReaderOn:return
        
        # self.FunctionOn = True
        
        # linearAddress = c_uint16()
        # dataLength = c_uint16()
        # bytesReturned = c_uint16()
        # authMode = c_uint8()
        # keyIndex = c_uint8()                
        # fnResult = c_ulong()
         
        # try: 
        #     strLinAddress = self.ui.txtLinearAddressRead.displayText()
        #     if not strLinAddress.isnumeric():
        #         QtWidgets.QMessageBox.Warning(self,'Warning !','You must enter any number !',QtWidgets.QMessageBox.Ok)
        #         self.ui.txtLinearAddressRead.setFocus()
        #         return
        #     strDataLength = self.ui.txtDataLengthRead.displayText()
        #     if not strDataLength.isnumeric():
        #         QtWidgets.QMessageBox.Warning(self,'Warning !','You must enter any number !',QtWidgets.QMessageBox.Ok)
        #         self.ui.txtDataLengthRead.setFocus()
        #         return             
            
        #     linearAddress = int(strLinAddress)
        #     dataLength    = int(strDataLength)
        #     dataValue = (c_uint8 * dataLength)()
        #     authMode  = MIFARE_AUTHENT1A  if self.ui.rbAUTH1A.isChecked() else MIFARE_AUTHENT1B
        #     keyIndex = 0
            
        #     fnResult = self.myLib.LinearRead(dataValue,linearAddress,dataLength,byref(bytesReturned),authMode,keyIndex)
        #     if fnResult == DL_OK:                
        #         li = [chr(i) for i in dataValue]
        #         self.ui.txtLinearRead.setText(''.join(li))
        #         self.ui.txtReadBytes.setText(str(bytesReturned.value))
        #         self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
        #         self.ReaderUISignal(FUNCT_LIGHT_OK,FUNCT_SOUND_OK)
        #     else:
        #         self.ui.txtReadBytes.setText(str(bytesReturned.value))
        #         self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
        #         self.ReaderUISignal(FUNCT_LIGHT_ERROR,FUNCT_SOUND_ERROR) 
    
        # finally:
        #     self.FunctionOn = False    
        if self.FunctionOn or self.ReaderOn:return
        
        self.FunctionOn = True
        
        linearAddress = c_uint16()
        dataLength = c_uint16()
        bytesReturned = c_uint16()
        authMode = c_uint8()
        keyIndex = c_uint8()                
        fnResult = c_ulong()
         
        try: 
            strLinAddress = self.ui.txtLinearAddressRead.displayText()
            if not strLinAddress.isnumeric():
                QtWidgets.QMessageBox.Warning(self,'Warning !','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtLinearAddressRead.setFocus()
                return
            strDataLength = self.ui.txtDataLengthRead.displayText()
            if not strDataLength.isnumeric():
                QtWidgets.QMessageBox.Warning(self,'Warning !','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtDataLengthRead.setFocus()
                return             
            
            linearAddress = int(16)
            dataLength    = int(2)
            dataValue = (c_uint8 * dataLength)()
            authMode  = MIFARE_AUTHENT1A  if self.ui.rbAUTH1A.isChecked() else MIFARE_AUTHENT1B
            keyIndex = 0
            
            for i in range(50) :
                fnResult = self.myLib.LinearRead(dataValue,linearAddress,dataLength,byref(bytesReturned),authMode,keyIndex)
                s1 = c_uint16()
                s1 = ((dataValue[0] << 8) & 0xff00) + ( dataValue[1] & 0x00ff)
                print(s1)

    
        finally:
            self.FunctionOn = False    
        
         

    def LinearWrite(self):
        if self.FunctionOn or self.ReaderOn:return
        
        self.FunctionOn = True
        try:
            linearAddress = c_uint16()
            dataLength = c_uint16()
            byteWritten = c_uint16()
            authMode = c_uint8()
            keyIndex = c_uint8()
            fnResult = c_uint32()
        
        
            linWrite = self.ui.txtLinearWrite.toPlainText()
            if not linWrite.strip():
                QtWidgets.QMessageBox.Warning(self,'Warning','You must enter any value !',QtWidgets.QMessageBox.Ok)
                self.ui.txtLinearWrite.setFocus()
                return
        
            linAddress = self.ui.txtLinearAddressWrite.displayText()
            if not linAddress.isnumeric():
                QtWidgets.QMessageBox.Warning(self,'Warning ','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtLinearAddressWrite.setFocus()
                return
        
            dataLen = self.ui.txtDataLengthWrite.displayText()
            if not dataLen.isnumeric():
                QtWidgets.QMessageBox.Warning(self,'Warning ','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtDataLengthWrite.setFocus()
                return
            
            authMode = MIFARE_AUTHENT1A if self.ui.rbAUTH1A.isChecked() else MIFARE_AUTHENT1B
            keyIndex = 0
            
            dataValueToByte = str.encode(linWrite)
            
            fnResult = self.myLib.LinearWrite(dataValueToByte,int(linAddress),int(dataLen),byref(byteWritten),authMode,keyIndex)
            if fnResult == DL_OK:
                self.ui.txtBytesWritten.setText(str(byteWritten.value))
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                self.ReaderUISignal(FUNCT_LIGHT_OK,FUNCT_SOUND_OK)
            else:
                self.ui.txtBytesWritten.setText(str(byteWritten.value))
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                self.ReaderUISignal(FUNCT_LIGHT_ERROR,FUNCT_SOUND_ERROR) 
                
        
        finally:
            self.FunctionOn = True    
        





if __name__ == "__main__":
    app = QApplication(sys.argv)
    uFS = uFSimple() 
    uFS.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
    uFS.show() 
    sys.exit(app.exec_())
    
