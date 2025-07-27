'''
   @author: Vladan S
   @organization: D-Logic  
   @version: 2.0
'''

import sys
import re
from uFCoderAdvanced import *
import Functions
from  ValueBlockReadWriteForm import*


class ValueBlockReadWrite(QDialog,Ui_ValueBlockRW):
    """
       main class
    """
    def __init__(self,parent=None):
        super(ValueBlockReadWrite,self).__init__(parent)         
        self.initUI()
        self.mySO = Functions.GetPlatform()         
        self.FillKeyIndex(KEY_INDEX_MAX)            
        self.CreateLineEditForKeys(self.ui.pnlAuth,380,10,"txtPKKey","255",6)
     
    def initUI(self):
        self.ui = Ui_ValueBlockRW()
        self.ui.setupUi(self)
        
        self.ui.btnValueBlockRead.clicked.connect(self.ValueBlockRead)
        self.ui.btnValueBlockReadAKM1.clicked.connect(self.ValueBlockReadAKM1)
        self.ui.btnValueBlockReadAKM2.clicked.connect(self.ValueBlockReadAKM2)
        self.ui.btnValueBlockReadPK.clicked.connect(self.ValueBlockReadPK)
        
        self.ui.btnValueBlockWrite.clicked.connect(self.ValueBlockWrite) 
        self.ui.btnValueBlockWriteAKM1.clicked.connect(self.ValueBlockWriteAKM1)
        self.ui.btnValueBlockWriteAKM2.clicked.connect(self.ValueBlockWriteAKM2)
        self.ui.btnValueBlockWritePK.clicked.connect(self.ValueBlockWritePK)   
    
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
    
    
    
    
    def ValueBlockRead(self):
        """
         Value Block Read function
        """
        
        if Functions.FunctionOn == True or Functions.ReaderOn == True:return
        Functions.FunctionOn = True
        
        valueRead = c_int32()
        valueAddress = c_uint8()
        blockAddress = c_uint8()
        keyIndex = c_uint8()
        authMode = c_uint8()
        fnResult = c_int32()
        
        try:
                      
            sBlockAddress = self.ui.txtValueBlockAddressBR.text()
            if not sBlockAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtValueBlockAddressBR.setFocus()
                return
            
                    
            blockAddress = int(sBlockAddress)
            keyIndex = int(self.ui.cboKeyIndex.currentText())
            authMode = MIFARE_AUTHENT1A if self.ui.rbAUTH1A.isChecked() else MIFARE_AUTHENT1B
            
            fnResult = self.mySO.ValueBlockRead(byref(valueRead),byref(valueAddress),blockAddress,authMode,keyIndex)
            
            if fnResult == DL_OK:                               
                self.ui.txtValueReadDataBR.setText(str(valueRead.value))
                self.ui.txtValueAddressBR.setText(str(valueAddress.value))
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_OK,FUNCT_SOUND_OK)
            else:                
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_ERROR,FUNCT_SOUND_ERROR)
        finally:
            Functions.FunctionOn = False
            
            
            
    def ValueBlockReadAKM1(self):
        """
         Value Block Read AKM1 function
        """
        
        if Functions.FunctionOn == True or Functions.ReaderOn == True:return
        Functions.FunctionOn = True
        
        valueRead = c_int32()
        valueAddress = c_uint8()
        blockAddress = c_uint8()        
        authMode = c_uint8()
        fnResult = c_int32()
        
        try:
                      
            sBlockAddress = self.ui.txtValueBlockAddressAKM1.text()
            if not sBlockAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtValueBlockAddressAKM1.setFocus()
                return
            
                    
            blockAddress = int(sBlockAddress)            
            authMode = MIFARE_AUTHENT1A if self.ui.rbAUTH1A.isChecked() else MIFARE_AUTHENT1B
            
            fnResult = self.mySO.ValueBlockRead_AKM1(byref(valueRead),byref(valueAddress),blockAddress,authMode)
            
            if fnResult == DL_OK:                               
                self.ui.txtValueReadDataBRAKM1.setText(str(valueRead.value))
                self.ui.txtValueAddressAKM1.setText(str(valueAddress.value))
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_OK,FUNCT_SOUND_OK)
            else:                
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_ERROR,FUNCT_SOUND_ERROR)
        finally:
            Functions.FunctionOn = False
            
            
    def ValueBlockReadAKM2(self):
        """
         Value Block Read AKM2 function
        """
        
        if Functions.FunctionOn == True or Functions.ReaderOn == True:return
        Functions.FunctionOn = True
        
        valueRead = c_int32()
        valueAddress = c_uint8()
        blockAddress = c_uint8()        
        authMode = c_uint8()
        fnResult = c_int32()
        
        try:
                      
            sBlockAddress = self.ui.txtValueBlockAddressAKM2.text()
            if not sBlockAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtValueBlockAddressAKM2.setFocus()
                return
            
                    
            blockAddress = int(sBlockAddress)            
            authMode = MIFARE_AUTHENT1A if self.ui.rbAUTH1A.isChecked() else MIFARE_AUTHENT1B
            
            fnResult = self.mySO.ValueBlockRead_AKM2(byref(valueRead),byref(valueAddress),blockAddress,authMode)
            
            if fnResult == DL_OK:                               
                self.ui.txtValueReadDataBRAKM2.setText(str(valueRead.value))
                self.ui.txtValueAddressAKM2.setText(str(valueAddress.value))
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_OK,FUNCT_SOUND_OK)
            else:                
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_ERROR,FUNCT_SOUND_ERROR)
        finally:
            Functions.FunctionOn = False
            
    
    def ValueBlockReadPK(self):
        """
         Value Block Read PK function
        """
        
        if Functions.FunctionOn == True or Functions.ReaderOn == True:return
        Functions.FunctionOn = True
        
        valueRead = c_int32()
        valueAddress = c_uint8()
        blockAddress = c_uint8()        
        authMode = c_uint8()
        pPKKey   = POINTER(c_ubyte)
        fnResult = c_int32()
        
        try:
                      
            sBlockAddress = self.ui.txtValueBlockAddressPK.text()
            if not sBlockAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtValueBlockAddressPK.setFocus()
                return
            
            pPKKey = self.ReadPKKeys()                
            blockAddress = int(sBlockAddress)            
            authMode = MIFARE_AUTHENT1A if self.ui.rbAUTH1A.isChecked() else MIFARE_AUTHENT1B
            
            fnResult = self.mySO.ValueBlockRead_PK(byref(valueRead),byref(valueAddress),blockAddress,authMode,pPKKey)
            
            if fnResult == DL_OK:                               
                self.ui.txtValueReadDataBRPK.setText(str(valueRead.value))
                self.ui.txtValueAddressPK.setText(str(valueAddress.value))
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_OK,FUNCT_SOUND_OK)
            else:                
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_ERROR,FUNCT_SOUND_ERROR)
        finally:
            Functions.FunctionOn = False
            
            
            
            
    def ValueBlockWrite(self):
        """
         Value Block Write function
        """
        
        if Functions.FunctionOn == True or Functions.ReaderOn == True:return
        Functions.FunctionOn = True
        
        valueWrite = c_int32()
        valueAddress = c_uint8()
        blockAddress = c_uint8()
        keyIndex = c_uint8()
        authMode = c_uint8()
        fnResult = c_int32()
        
        try:
            
            sValueWrite = self.ui.txtValueWriteDataBW.text()
            if not sValueWrite.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtValueWriteDataBW.setFocus()
                return
                      
            sValueAddress = self.ui.txtValueAddressBW.text()
            if not sValueAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtValueAddressBW.setFocus()
                return
            
            sBlockAddress = self.ui.txtValueBlockAddressBW.text()
            if not sValueAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtValueBlockAddressBW.setFocus()
                return
            
            valueWrite = int(sValueWrite)
            valueAddress = int(sValueAddress)                        
            blockAddress = int(sBlockAddress)
            keyIndex = int(self.ui.cboKeyIndex.currentText())
            authMode = MIFARE_AUTHENT1A if self.ui.rbAUTH1A.isChecked() else MIFARE_AUTHENT1B
            
            fnResult = self.mySO.ValueBlockWrite(valueWrite,valueAddress,blockAddress,authMode,keyIndex)
            
            if fnResult == DL_OK:                                              
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_OK,FUNCT_SOUND_OK)
            else:                
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_ERROR,FUNCT_SOUND_ERROR)
        finally:
            Functions.FunctionOn = False
    
    
    
    def ValueBlockWriteAKM1(self):
        """
         Value Block Write AKM1 function
        """
        
        if Functions.FunctionOn == True or Functions.ReaderOn == True:return
        Functions.FunctionOn = True
        
        valueWrite = c_int32()
        valueAddress = c_uint8()
        blockAddress = c_uint8()        
        authMode = c_uint8()
        fnResult = c_int32()        
        try:
            
            sValueWrite = self.ui.txtValueWriteDataBWAKM1.text()
            if not sValueWrite.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtValueWriteDataBWAKM1.setFocus()
                return
                      
            sValueAddress = self.ui.txtValueAddressBWAKM1.text()
            if not sValueAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtValueAddressBWAKM1.setFocus()
                return
            
            sBlockAddress = self.ui.txtValueBlockAddressBWAKM1.text()
            if not sValueAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtValueBlockAddressBWAKM1.setFocus()
                return
            
            valueWrite = int(sValueWrite)
            valueAddress = int(sValueAddress)                        
            blockAddress = int(sBlockAddress)            
            authMode = MIFARE_AUTHENT1A if self.ui.rbAUTH1A.isChecked() else MIFARE_AUTHENT1B
            
            fnResult = self.mySO.ValueBlockWrite_AKM1(valueWrite,valueAddress,blockAddress,authMode)
            
            if fnResult == DL_OK:                                              
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_OK,FUNCT_SOUND_OK)
            else:                
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_ERROR,FUNCT_SOUND_ERROR)
        finally:
            Functions.FunctionOn = False
            
            
    def ValueBlockWriteAKM2(self):
        """
         Value Block Write AKM2 function
        """
        
        if Functions.FunctionOn == True or Functions.ReaderOn == True:return
        Functions.FunctionOn = True
        
        valueWrite = c_int32()
        valueAddress = c_uint8()
        blockAddress = c_uint8()        
        authMode = c_uint8()
        fnResult = c_int32()        
        try:
            
            sValueWrite = self.ui.txtValueWriteDataBWAKM2.text()
            if not sValueWrite.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtValueWriteDataBWAKM2.setFocus()
                return
                      
            sValueAddress = self.ui.txtValueAddressBWAKM2.text()
            if not sValueAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtValueAddressBWAKM2.setFocus()
                return
            
            sBlockAddress = self.ui.txtValueBlockAddressBWAKM2.text()
            if not sValueAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtValueBlockAddressBWAKM2.setFocus()
                return
            
            valueWrite = int(sValueWrite)
            valueAddress = int(sValueAddress)                        
            blockAddress = int(sBlockAddress)            
            authMode = MIFARE_AUTHENT1A if self.ui.rbAUTH1A.isChecked() else MIFARE_AUTHENT1B
            
            fnResult = self.mySO.ValueBlockWrite_AKM2(valueWrite,valueAddress,blockAddress,authMode)
            
            if fnResult == DL_OK:                                              
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_OK,FUNCT_SOUND_OK)
            else:                
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_ERROR,FUNCT_SOUND_ERROR)
        finally:
            Functions.FunctionOn = False
            
            
    def ValueBlockWritePK(self):
        """
         Value Block Write PK function
        """
        
        if Functions.FunctionOn == True or Functions.ReaderOn == True:return
        Functions.FunctionOn = True
        
        valueWrite = c_int32()
        valueAddress = c_uint8()
        blockAddress = c_uint8()        
        authMode = c_uint8()
        pPKKey = POINTER(c_ubyte)
        fnResult = c_int32()        
        try:
            
            sValueWrite = self.ui.txtValueWriteDataBWPK.text()
            if not sValueWrite.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtValueWriteDataBWPK.setFocus()
                return
                      
            sValueAddress = self.ui.txtValueAddressBWPK.text()
            if not sValueAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtValueAddressBWPK.setFocus()
                return
            
            sBlockAddress = self.ui.txtValueBlockAddressBWPK.text()
            if not sValueAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtValueBlockAddressBWPK.setFocus()
                return
            
            valueWrite = int(sValueWrite)
            valueAddress = int(sValueAddress)                        
            blockAddress = int(sBlockAddress)            
            authMode = MIFARE_AUTHENT1A if self.ui.rbAUTH1A.isChecked() else MIFARE_AUTHENT1B
            pPKKey = self.ReadPKKeys()
            fnResult = self.mySO.ValueBlockWrite_PK(valueWrite,valueAddress,blockAddress,authMode,pPKKey)
            
            if fnResult == DL_OK:                                              
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_OK,FUNCT_SOUND_OK)
            else:                
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_ERROR,FUNCT_SOUND_ERROR)
        finally:
            Functions.FunctionOn = False
            
            