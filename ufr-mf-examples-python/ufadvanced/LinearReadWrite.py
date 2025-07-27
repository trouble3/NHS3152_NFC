'''
 Linear Read/Write

 @author: Vladan S
'''
import sys
import re
import ErrCodes
import Functions
from ctypes import *
#from Constants import *
 
from uFCoderAdvanced import * 
from LinearReadWriteForm import* 

from PyQt5.QtWidgets import QDialog,QCheckBox,QComboBox
from PyQt5.QtCore import QCoreApplication,Qt
from PyQt5.Qt import QLineEdit,QEvent, QWidget
from PyQt5 import  QtGui




class LinearRW(QDialog,Ui_subLinearReadWrite):
    
    def __init__(self,parent=None):        
        super(LinearRW,self).__init__(parent)        
        self.mySO = Functions.GetPlatform()                 
        self.initUI()
        
            
    def initUI(self):
        self.ui = Ui_subLinearReadWrite()
        self.ui.setupUi(self)
        
        self.FillKeyIndex(KEY_INDEX_MAX)            
        self.CreateLineEditForKeys(self.ui.pnlAuth,380,10,"txtPKKey","255",6)
        
        self.ui.btnLinearRead.clicked.connect(self.LinearRead)
        self.ui.btnLinearReadAKM1.clicked.connect(self.LinearReadAKM1)
        self.ui.btnLinearReadAKM2.clicked.connect(self.LinearReadAKM2)
        self.ui.btnLinearReadPK.clicked.connect(self.LinearReadPK)
               
        self.ui.btnLinearWrite.clicked.connect(self.LinearWrite)
        self.ui.btnLinearWriteAKM1.clicked.connect(self.LinearWriteAKM1)
        self.ui.btnLinearWriteAKM2.clicked.connect(self.LinearWriteAKM2)
        self.ui.btnLinearWritePK.clicked.connect(self.LinearWritePK)
        
        
        
        self.ui.txtLinearWrite.textChanged.connect(lambda:self.LenLinearWriteText(self.ui.txtDataLengthWrite,self.ui.txtLinearWrite))
        self.ui.txtLinearWriteAKM1.textChanged.connect(lambda:self.LenLinearWriteText(self.ui.txtDataLengthWriteAKM1,self.ui.txtLinearWriteAKM1))
        self.ui.txtLinearWriteAKM2.textChanged.connect(lambda:self.LenLinearWriteText(self.ui.txtDataLengthWriteAKM2,self.ui.txtLinearWriteAKM2))
        self.ui.txtLinearWritePK.textChanged.connect(lambda:self.LenLinearWriteText(self.ui.txtDataLengthWritePK,self.ui.txtLinearWritePK))
        
    def FillKeyIndex(self,count):
        
        for n in range(0,count):
            self.ui.cboKeyIndex.addItem(str(n))
            
    def CreateLineEditForKeys(self,parent,xOsa,yOsa,name,value,count):
        i = 1
        xSpace = 0
        for i in range(count):
            self.txtKey = QtWidgets.QLineEdit(parent)
            self.txtKey.setGeometry(QtCore.QRect(xOsa + xSpace, yOsa, 30, 20))
            font = QtGui.QFont()
            font.setFamily("Verdana")
            font.setPointSize(8)
            font.setBold(True)
            font.setWeight(70)
            self.txtKey.setFont(font)
            self.txtKey.setAlignment(QtCore.Qt.AlignCenter)
            self.txtKey.setReadOnly(False)
            self.txtKey.setText(value)
            self.txtKey.setMaxLength(3)
            self.txtKey.setObjectName(name + str(i))
            self.txtKey.textEdited.connect(self.RegKey)
            self.txtKey.installEventFilter(self)
            xSpace+=32
     
    def eventFilter(self, myObject, event):
        try:            
            if event.type() == QEvent.FocusOut:
                if  myObject.text() == '' or int(myObject.text()) > 255:
                    myObject.setFocus()
                if len(myObject.text()) == 0:
                    myObject.setText("0")
                return True
        
            return QDialog.eventFilter(self, myObject,event)
        except ValueError:
            #QtWidgets.QMessageBox.Warning(self,'Must enter an number !','WARNING',QtWidgets.QMessageBox.Ok)
            myObject.setFocus()
             
     
    def RegKey(self):
        sender  = self.sender()             
        sendText = sender.text()        
        match = re.search('[a-zA-Z]',sendText)        
        if match:                 
            sender.backspace() 
            
    def LenLinearWriteText(self,txtDLength,txtTekst):            
        txtDLength.setText(str(len(txtTekst.toPlainText())))
            
    def SetFnStatus(self,fnValue,fnExplain):
        self.ui.lblFnValue.setText(hex(fnValue))
        self.ui.lblFnExplain.setText(fnExplain)        
    
    
    def ReadPKKeys(self):
        le = QLineEdit()
        arPKKey = (c_uint8 *6)()
        counter = 1
        lek = []
        for le in self.ui.pnlAuth.children():
            if isinstance(le, QLineEdit):                
                lek.append(int(le.text()))
                arPKKey[counter - 1] = int(le.text())
                counter +=1
        return arPKKey
    
    
    
    def LinearRead(self):
        """
         Linear Read function
         
        """             
        if  Functions.FunctionOn == True or Functions.ReaderOn == True:return        
        Functions.FunctionOn = True
        
        linearAddress = c_uint16()
        dataLength = c_uint16()
        bytesReturned = c_uint16()
        authMode = c_uint8()
        keyIndex = c_uint8()                
        fnResult = c_ulong()
         
        try: 
            strLinAddress = self.ui.txtLinearAddressRead.displayText()
            if not strLinAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,"Warning","You must enter any number !",QtWidgets.QMessageBox.Ok)
                self.lrui.txtLinearAddressRead.setFocus()
                return
            strDataLength = self.ui.txtDataLengthRead.displayText()
            if not strDataLength.isnumeric():
                QtWidgets.QMessageBox.warning(self,"Warning","You must enter any number !",QtWidgets.QMessageBox.Ok)
                self.ui.txtDataLengthRead.setFocus()
                return             
            
            linearAddress = int(strLinAddress)
            dataLength    = int(strDataLength)
            dataValue = (c_uint8 * dataLength)()
            authMode  = MIFARE_AUTHENT1A  if self.ui.rbAUTH1A.isChecked() else MIFARE_AUTHENT1B
            keyIndex = int(self.ui.cboKeyIndex.currentText())
            fnResult = self.mySO.LinearRead(dataValue,linearAddress,dataLength,byref(bytesReturned),authMode,keyIndex)
            
            if fnResult == DL_OK:                
                li = [chr(i) for i in dataValue]
                self.ui.txtLinearRead.setText(''.join(li))
                self.ui.txtReadBytes.setText(str(bytesReturned.value))
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_OK,FUNCT_SOUND_OK)
            else:
                self.ui.txtReadBytes.setText(str(bytesReturned.value))
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_ERROR,FUNCT_SOUND_ERROR) 
    
        finally:
            Functions.FunctionOn = False    
    
    def LinearReadAKM1(self):
        """
         Linear Read AKM1 function
        """
        if  Functions.FunctionOn == True or Functions.ReaderOn == True:return        
        Functions.FunctionOn = True
        
        linearAddress = c_uint16()
        dataLength = c_uint16()
        bytesReturned = c_uint16()
        authMode = c_uint8()                    
        fnResult = c_ulong()
         
        try: 
            strLinAddress = self.ui.txtLinearAddressReadAKM1.displayText()
            if not strLinAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning !','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.lrui.txtLinearAddressReadAKM1.setFocus()
                return
            strDataLength = self.ui.txtDataLengthReadAKM1.displayText()
            if not strDataLength.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning !','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtDataLengthReadAKM1.setFocus()
                return             
            
            linearAddress = int(strLinAddress)
            dataLength    = int(strDataLength)
            dataValue = (c_uint8 * dataLength)()
            authMode  = MIFARE_AUTHENT1A  if self.ui.rbAUTH1A.isChecked() else MIFARE_AUTHENT1B
            
            fnResult = self.mySO.LinearRead_AKM1(dataValue,linearAddress,dataLength,byref(bytesReturned),authMode)
            if fnResult == DL_OK:                
                li = [chr(i) for i in dataValue]
                self.ui.txtLinearReadAKM1.setText(''.join(li))
                self.ui.txtReadBytesAKM1.setText(str(bytesReturned.value))
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_OK,FUNCT_SOUND_OK)
            else:
                self.ui.txtReadBytesAKM1.setText(str(bytesReturned.value))
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_ERROR,FUNCT_SOUND_ERROR) 
        finally:            
            Functions.FunctionOn = False
              
    
    def LinearReadAKM2(self):
        """
         Linear Read AKM2 function
        """
        if  Functions.FunctionOn == True or Functions.ReaderOn == True:return        
        Functions.FunctionOn = True
        
        linearAddress = c_uint16()
        dataLength = c_uint16()
        bytesReturned = c_uint16()
        authMode = c_uint8()                    
        fnResult = c_ulong()
         
        try: 
            strLinAddress = self.ui.txtLinearAddressReadAKM2.displayText()
            if not strLinAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning !','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.lrui.txtLinearAddressReadAKM1.setFocus()
                return
            strDataLength = self.ui.txtDataLengthReadAKM2.displayText()
            if not strDataLength.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning !','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtDataLengthReadAKM1.setFocus()
                return             
            
            linearAddress = int(strLinAddress)
            dataLength    = int(strDataLength)
            dataValue = (c_uint8 * dataLength)()
            authMode  = MIFARE_AUTHENT1A  if self.ui.rbAUTH1A.isChecked() else MIFARE_AUTHENT1B
            
            
            fnResult = self.mySO.LinearRead_AKM2(dataValue,linearAddress,dataLength,byref(bytesReturned),authMode)
            if fnResult == DL_OK:                
                li = [chr(i) for i in dataValue]
                self.ui.txtLinearReadAKM2.setText(''.join(li))
                self.ui.txtReadBytesAKM2.setText(str(bytesReturned.value))
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_OK,FUNCT_SOUND_OK)
            else:
                self.ui.txtReadBytesAKM2.setText(str(bytesReturned.value))
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_ERROR,FUNCT_SOUND_ERROR) 
        finally:
            Functions.FunctionOn = False       
    
    def LinearReadPK(self):
        """
         Linear Read PK function
        """
        if  Functions.FunctionOn == True or Functions.ReaderOn == True:return        
        Functions.FunctionOn = True
        
        linearAddress = c_uint16()
        dataLength = c_uint16()
        bytesReturned = c_uint16()
        authMode = c_uint8()                
        pPKKey   = POINTER(c_ubyte)                
        fnResult = c_ulong()
         
        try: 
            strLinAddress = self.ui.txtLinearAddressReadPK.displayText()
            if not strLinAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning !','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.lrui.txtLinearAddressReadPK.setFocus()
                return
            strDataLength = self.ui.txtDataLengthReadPK.displayText()
            if not strDataLength.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning !','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtDataLengthReadPK.setFocus()
                return             
            
            linearAddress = int(strLinAddress)
            dataLength    = int(strDataLength)
            dataValue = (c_uint8 * dataLength)()
            authMode  = MIFARE_AUTHENT1A  if self.ui.rbAUTH1A.isChecked() else MIFARE_AUTHENT1B
            
            pPKKey = self.ReadPKKeys()
            
            fnResult = self.mySO.LinearRead_PK(dataValue,linearAddress,dataLength,byref(bytesReturned),authMode,pPKKey)
            if fnResult == DL_OK:                
                li = [chr(i) for i in dataValue]
                self.ui.txtLinearReadPK.setText(''.join(li))
                self.ui.txtReadBytesPK.setText(str(bytesReturned.value))
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_OK,FUNCT_SOUND_OK)
            else:
                self.ui.txtReadBytesPK.setText(str(bytesReturned.value))
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_ERROR,FUNCT_SOUND_ERROR) 
        finally:
            Functions.FunctionOn = False 
    
    
    
    
    
    
    def LinearWrite(self):
        """
          Linear Write function
        """
        if  Functions.FunctionOn == True or Functions.ReaderOn == True:return        
        Functions.FunctionOn = True
        
        
        byteWritten = c_uint16()
        authMode = c_uint8()
        keyIndex = c_uint8()
        fnResult = c_uint32()
        
        try:                    
            linWrite = self.ui.txtLinearWrite.toPlainText()
            if not linWrite.strip():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any value !',QtWidgets.QMessageBox.Ok)
                self.ui.txtLinearWrite.setFocus()
                return
        
            linAddress = self.ui.txtLinearAddressWrite.displayText()
            if not linAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning ','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtLinearAddressWrite.setFocus()
                return
        
            dataLen = self.ui.txtDataLengthWrite.displayText()
            if not dataLen.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning ','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtDataLengthWrite.setFocus()
                return
            
            authMode = MIFARE_AUTHENT1A if self.ui.rbAUTH1A.isChecked() else MIFARE_AUTHENT1B
            keyIndex = int(self.ui.cboKeyIndex.currentText())
            
            dataValueToByte = str.encode(linWrite)
            
            fnResult = self.mySO.LinearWrite(dataValueToByte,int(linAddress),int(dataLen),byref(byteWritten),authMode,keyIndex)
            if fnResult == DL_OK:
                self.ui.txtBytesWritten.setText(str(byteWritten.value))
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_OK,FUNCT_SOUND_OK)
            else:
                self.ui.txtBytesWritten.setText(str(byteWritten.value))
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_ERROR,FUNCT_SOUND_ERROR)                     
        finally:
            Functions.FunctionOn = False 
            
            
            
            
    def LinearWriteAKM1(self):
        """
          Linear Write AKM1 function
        """
        if  Functions.FunctionOn == True or Functions.ReaderOn == True:return        
        Functions.FunctionOn = True
        
        
        byteWritten = c_uint16()
        authMode = c_uint8()           
        fnResult = c_uint32()
        try:          
            linWrite = self.ui.txtLinearWriteAKM1.toPlainText()
            if not linWrite.strip():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any value !',QtWidgets.QMessageBox.Ok)
                self.ui.txtLinearWriteAKM1.setFocus()
                return
        
            linAddress = self.ui.txtLinearAddressWriteAKM1.displayText()
            if not linAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning ','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtLinearAddressWriteAKM1.setFocus()
                return
        
            dataLen = self.ui.txtDataLengthWriteAKM1.displayText()
            if not dataLen.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning ','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtDataLengthWriteAKM1.setFocus()
                return
            
            authMode = MIFARE_AUTHENT1A if self.ui.rbAUTH1A.isChecked() else MIFARE_AUTHENT1B
            
            dataValueToByte = str.encode(linWrite)
            
            fnResult = self.mySO.LinearWrite_AKM1(dataValueToByte,int(linAddress),int(dataLen),byref(byteWritten),authMode)
            if fnResult == DL_OK:
                self.ui.txtBytesWrittenAKM1.setText(str(byteWritten.value))
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_OK,FUNCT_SOUND_OK)
            else:
                self.ui.txtBytesWrittenAKM1.setText(str(byteWritten.value))
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_ERROR,FUNCT_SOUND_ERROR)                     
        finally:
            Functions.FunctionOn = False 
            
            
            
            
    def LinearWriteAKM2(self):
        """
          Linear Write AKM2 function
        """
        if  Functions.FunctionOn == True or Functions.ReaderOn == True:return        
        Functions.FunctionOn = True
        try:
            
            byteWritten = c_uint16()
            authMode = c_uint8()
            
            fnResult = c_uint32()
        
        
            linWrite = self.ui.txtLinearWriteAKM2.toPlainText()
            if not linWrite.strip():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any value !',QtWidgets.QMessageBox.Ok)
                self.ui.txtLinearWriteAKM2.setFocus()
                return
        
            linAddress = self.ui.txtLinearAddressWriteAKM2.displayText()
            if not linAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning ','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtLinearAddressWriteAKM2.setFocus()
                return
        
            dataLen = self.ui.txtDataLengthWriteAKM2.displayText()
            if not dataLen.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning ','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtDataLengthWriteAKM2.setFocus()
                return
            
            authMode = MIFARE_AUTHENT1A if self.ui.rbAUTH1A.isChecked() else MIFARE_AUTHENT1B
            
            
            dataValueToByte = str.encode(linWrite)
            
            fnResult = self.mySO.LinearWrite_AKM2(dataValueToByte,int(linAddress),int(dataLen),byref(byteWritten),authMode)
            if fnResult == DL_OK:
                self.ui.txtBytesWrittenAKM2.setText(str(byteWritten.value))
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_OK,FUNCT_SOUND_OK)
            else:
                self.ui.txtBytesWrittenAKM2.setText(str(byteWritten.value))
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_ERROR,FUNCT_SOUND_ERROR)                     
        finally:
            Functions.FunctionOn = False 
            
            
            
    def LinearWritePK(self):
        """
          Linear Write PK function
        """
        if  Functions.FunctionOn == True or Functions.ReaderOn == True:return        
        Functions.FunctionOn = True
        try:
           
            byteWritten = c_uint16()
            authMode = c_uint8()            
            pPKKey   = POINTER(c_ubyte)
            fnResult = c_uint32()
        
        
            linWrite = self.ui.txtLinearWritePK.toPlainText()
            if not linWrite.strip():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any value !',QtWidgets.QMessageBox.Ok)
                self.ui.txtLinearWriteAKM1.setFocus()
                return
        
            linAddress = self.ui.txtLinearAddressWritePK.displayText()
            if not linAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning ','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtLinearAddressWritePK.setFocus()
                return
        
            dataLen = self.ui.txtDataLengthWritePK.displayText()
            if not dataLen.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning ','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtDataLengthWritePK.setFocus()
                return
            
            authMode = MIFARE_AUTHENT1A if self.ui.rbAUTH1A.isChecked() else MIFARE_AUTHENT1B
            
            pPKKey = self.ReadPKKeys()
            
            dataValueToByte = str.encode(linWrite)
            
            fnResult = self.mySO.LinearWrite_PK(dataValueToByte,int(linAddress),int(dataLen),byref(byteWritten),authMode,pPKKey)
            if fnResult == DL_OK:
                self.ui.txtBytesWrittenPK.setText(str(byteWritten.value))
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_OK,FUNCT_SOUND_OK)
            else:
                self.ui.txtBytesWrittenPK.setText(str(byteWritten.value))
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_ERROR,FUNCT_SOUND_ERROR)                     
        finally:
            Functions.FunctionOn = False 