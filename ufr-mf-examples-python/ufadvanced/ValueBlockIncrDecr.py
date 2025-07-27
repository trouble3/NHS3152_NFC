'''
   @author: Vladan S
   @organization: D-Logic  
   @version: 2.0
'''

import sys
import re
from uFCoderAdvanced import *
import Functions
from  ValueBlockIncrDecrForm  import*




class ValueBlockIncrDecr(QDialog,Ui_ValueBlockIncremDecrem):
    """
       main class
    """
    def __init__(self,parent=None):
        super(ValueBlockIncrDecr,self).__init__(parent)         
        self.initUI()
        self.mySO = Functions.GetPlatform()         
        self.FillKeyIndex(KEY_INDEX_MAX)            
        self.CreateLineEditForKeys(self.ui.pnlAuth,380,10,"txtPKKey","255",6)
     
    def initUI(self):
        self.ui = Ui_ValueBlockIncremDecrem()
        self.ui.setupUi(self)
        
        self.ui.btnIncrementValue.clicked.connect(self.ValueBlockIncrement)
        self.ui.btnIncrementValueAKM1.clicked.connect(self.ValueBlockIncrementAKM1)
        self.ui.btnIncrementValueAKM2.clicked.connect(self.ValueBlockIncrementAKM2)
        self.ui.btnIncrementValuePK.clicked.connect(self.ValueBlockIncrementPK)
        
        self.ui.btnDecrementValue.clicked.connect(self.ValueBlockDecrement)
        self.ui.btnDecrementValueAKM1.clicked.connect(self.ValueBlockDecrementAKM1)
        self.ui.btnDecrementValueAKM2.clicked.connect(self.ValueBlockDecrementAKM2)
        self.ui.btnDecrementValuePK.clicked.connect(self.ValueBlockDecrementPK)
           
    
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
    
    
    
    
    def ValueBlockIncrement(self):
        """
          ValueBlock Increment function
        """
        
        if Functions.FunctionOn == True or Functions.ReaderOn == True:return
        Functions.FunctionOn = True
        
        incrementValue = c_int32()
        blockAddress = c_uint8()
        keyIndex = c_uint8()
        authMode = c_uint8()
        fnResult = c_int32()
        
        try:
            sIncrementValue = self.ui.txtIncrementValue.text()
            if not sIncrementValue.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtIncrementValue.setFocus()
                return
                      
            sBlockAddress = self.ui.txtBlockAddressIncr.text()
            if not sBlockAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtBlockAddressIncr.setFocus()
                return
            
            incrementValue = int(sIncrementValue)        
            blockAddress = int(sBlockAddress)
            keyIndex = int(self.ui.cboKeyIndex.currentText())
            authMode = MIFARE_AUTHENT1A if self.ui.rbAUTH1A.isChecked() else MIFARE_AUTHENT1B
            
            fnResult = self.mySO.ValueBlockIncrement(incrementValue,blockAddress,authMode,keyIndex)
            
            if fnResult == DL_OK:                                               
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_OK,FUNCT_SOUND_OK)
            else:                
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_ERROR,FUNCT_SOUND_ERROR)
        
        finally:
            Functions.FunctionOn = False
    
    
    
    
    def ValueBlockIncrementAKM1(self):
        """
          ValueBlock Increment AKM1 function
        """
        
        if Functions.FunctionOn == True or Functions.ReaderOn == True:return
        Functions.FunctionOn = True
        
        incrementValue = c_int32()
        blockAddress = c_uint8()        
        authMode = c_uint8()
        fnResult = c_int32()
        
        try:
            sIncrementValue = self.ui.txtIncrementValueAKM1.text()
            if not sIncrementValue.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtIncrementValueAKM1.setFocus()
                return
                      
            sBlockAddress = self.ui.txtBlockAddressIncrAKM1.text()
            if not sBlockAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtBlockAddressIncrAKM1.setFocus()
                return
            
            incrementValue = int(sIncrementValue)        
            blockAddress = int(sBlockAddress)            
            authMode = MIFARE_AUTHENT1A if self.ui.rbAUTH1A.isChecked() else MIFARE_AUTHENT1B
            
            fnResult = self.mySO.ValueBlockIncrement_AKM1(incrementValue,blockAddress,authMode)
            
            if fnResult == DL_OK:                                               
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_OK,FUNCT_SOUND_OK)
            else:                
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_ERROR,FUNCT_SOUND_ERROR)
        
        finally:
            Functions.FunctionOn = False
    
    def ValueBlockIncrementAKM2(self):
        """
          ValueBlock Increment AKM2 function
        """
        
        if Functions.FunctionOn == True or Functions.ReaderOn == True:return
        Functions.FunctionOn = True
        
        incrementValue = c_int32()
        blockAddress = c_uint8()        
        authMode = c_uint8()
        fnResult = c_int32()
        
        try:
            sIncrementValue = self.ui.txtIncrementValueAKM2.text()
            if not sIncrementValue.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtIncrementValueAKM2.setFocus()
                return
                      
            sBlockAddress = self.ui.txtBlockAddressIncrAKM2.text()
            if not sBlockAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtBlockAddressIncrAKM2.setFocus()
                return
            
            incrementValue = int(sIncrementValue)        
            blockAddress = int(sBlockAddress)            
            authMode = MIFARE_AUTHENT1A if self.ui.rbAUTH1A.isChecked() else MIFARE_AUTHENT1B
            
            fnResult = self.mySO.ValueBlockIncrement_AKM2(incrementValue,blockAddress,authMode)
            
            if fnResult == DL_OK:                                               
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_OK,FUNCT_SOUND_OK)
            else:                
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_ERROR,FUNCT_SOUND_ERROR)
        
        finally:
            Functions.FunctionOn = False
            
    
    def ValueBlockIncrementPK(self):
        """
          ValueBlock Increment PK function
        """
        
        if Functions.FunctionOn == True or Functions.ReaderOn == True:return
        Functions.FunctionOn = True
        
        incrementValue = c_int32()
        blockAddress = c_uint8()        
        authMode = c_uint8()
        pPKKey   = POINTER(c_ubyte)
        fnResult = c_int32()
        
        try:
            sIncrementValue = self.ui.txtIncrementValuePK.text()
            if not sIncrementValue.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtIncrementValuePK.setFocus()
                return
                      
            sBlockAddress = self.ui.txtBlockAddressIncrPK.text()
            if not sBlockAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtBlockAddressIncrPK.setFocus()
                return
            
            incrementValue = int(sIncrementValue)        
            blockAddress = int(sBlockAddress)            
            authMode = MIFARE_AUTHENT1A if self.ui.rbAUTH1A.isChecked() else MIFARE_AUTHENT1B
            pPKKey = self.ReadPKKeys()
            
            fnResult = self.mySO.ValueBlockIncrement_PK(incrementValue,blockAddress,authMode,pPKKey)
            
            if fnResult == DL_OK:                                               
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_OK,FUNCT_SOUND_OK)
            else:                
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_ERROR,FUNCT_SOUND_ERROR)
        
        finally:
            Functions.FunctionOn = False
    
    
    def ValueBlockDecrement(self):
        """
          ValueBlock Decrement function
        """
        
        if Functions.FunctionOn == True or Functions.ReaderOn == True:return
        Functions.FunctionOn = True
        
        decrementValue = c_int32()
        blockAddress = c_uint8()
        keyIndex = c_uint8()
        authMode = c_uint8()
        fnResult = c_int32()
        
        try:
            sDecrementValue = self.ui.txtDecrementValue.text()
            if not sDecrementValue.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtDecrementValue.setFocus()
                return
                      
            sBlockAddress = self.ui.txtBlockAddressDecr.text()
            if not sBlockAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtBlockAddressDecr.setFocus()
                return
            
            decrementValue = int(sDecrementValue)        
            blockAddress = int(sBlockAddress)
            keyIndex = int(self.ui.cboKeyIndex.currentText())
            authMode = MIFARE_AUTHENT1A if self.ui.rbAUTH1A.isChecked() else MIFARE_AUTHENT1B
            
            fnResult = self.mySO.ValueBlockDecrement(decrementValue,blockAddress,authMode,keyIndex)
            
            if fnResult == DL_OK:                                               
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_OK,FUNCT_SOUND_OK)
            else:                
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_ERROR,FUNCT_SOUND_ERROR)
        
        finally:
            Functions.FunctionOn = False
    
    
    def ValueBlockDecrementAKM1(self):
        """
          ValueBlock Decrement AKM1 function
        """
        
        if Functions.FunctionOn == True or Functions.ReaderOn == True:return
        Functions.FunctionOn = True
        
        decrementValue = c_int32()
        blockAddress = c_uint8()        
        authMode = c_uint8()
        fnResult = c_int32()
        
        try:
            sDecrementValue = self.ui.txtDecrementValueAKM1.text()
            if not sDecrementValue.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtDecrementValueAKM1.setFocus()
                return
                      
            sBlockAddress = self.ui.txtBlockAddressDecrAKM1.text()
            if not sBlockAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtBlockAddressDecrAKM1.setFocus()
                return
            
            decrementValue = int(sDecrementValue)        
            blockAddress = int(sBlockAddress)           
            authMode = MIFARE_AUTHENT1A if self.ui.rbAUTH1A.isChecked() else MIFARE_AUTHENT1B
            
            fnResult = self.mySO.ValueBlockDecrement_AKM1(decrementValue,blockAddress,authMode)
            
            if fnResult == DL_OK:                                               
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_OK,FUNCT_SOUND_OK)
            else:                
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_ERROR,FUNCT_SOUND_ERROR)
        
        finally:
            Functions.FunctionOn = False
    
    
    def ValueBlockDecrementAKM2(self):
        """
          ValueBlock Decrement AKM2 function
        """
        
        if Functions.FunctionOn == True or Functions.ReaderOn == True:return
        Functions.FunctionOn = True
        
        decrementValue = c_int32()
        blockAddress = c_uint8()        
        authMode = c_uint8()
        fnResult = c_int32()
        
        try:
            sDecrementValue = self.ui.txtDecrementValueAKM2.text()
            if not sDecrementValue.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtDecrementValueAKM2.setFocus()
                return
                      
            sBlockAddress = self.ui.txtBlockAddressDecrAKM2.text()
            if not sBlockAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtBlockAddressDecrAKM2.setFocus()
                return
            
            decrementValue = int(sDecrementValue)        
            blockAddress = int(sBlockAddress)           
            authMode = MIFARE_AUTHENT1A if self.ui.rbAUTH1A.isChecked() else MIFARE_AUTHENT1B
            
            fnResult = self.mySO.ValueBlockDecrement_AKM2(decrementValue,blockAddress,authMode)
            
            if fnResult == DL_OK:                                               
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_OK,FUNCT_SOUND_OK)
            else:                
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_ERROR,FUNCT_SOUND_ERROR)
        
        finally:
            Functions.FunctionOn = False
            
            
            
    def ValueBlockDecrementPK(self):
        """
          ValueBlock Decrement PK function
        """
        
        if Functions.FunctionOn == True or Functions.ReaderOn == True:return
        Functions.FunctionOn = True
        
        decrementValue = c_int32()
        blockAddress = c_uint8()        
        authMode = c_uint8()
        pPKKey = POINTER(c_ubyte)
        fnResult = c_int32()
        
        try:
            sDecrementValue = self.ui.txtDecrementValuePK.text()
            if not sDecrementValue.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtDecrementValuePK.setFocus()
                return
                      
            sBlockAddress = self.ui.txtBlockAddressDecrPK.text()
            if not sBlockAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtBlockAddressDecrPK.setFocus()
                return
            
            pPKKey = self.ReadPKKeys()
            decrementValue = int(sDecrementValue)        
            blockAddress = int(sBlockAddress)           
            authMode = MIFARE_AUTHENT1A if self.ui.rbAUTH1A.isChecked() else MIFARE_AUTHENT1B
            
            fnResult = self.mySO.ValueBlockDecrement_PK(decrementValue,blockAddress,authMode,pPKKey)
            
            if fnResult == DL_OK:                                               
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_OK,FUNCT_SOUND_OK)
            else:                
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_ERROR,FUNCT_SOUND_ERROR)
        
        finally:
            Functions.FunctionOn = False