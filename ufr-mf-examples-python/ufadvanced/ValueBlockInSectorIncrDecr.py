'''
   @author: Vladan S
   @organization: D-Logic  
   @version: 2.0
'''

import sys
import re
from uFCoderAdvanced import *
import Functions
from  ValueBlockInSectorIncrDecrForm  import*




class ValueBlockIncrDecr(QDialog,Ui_ValueBlockInSectorIncrDecr):
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
        self.ui = Ui_ValueBlockInSectorIncrDecr()
        self.ui.setupUi(self)
        
        self.ui.btnIncrementValue.clicked.connect(self.ValueBlockInSectorIncrement)
        self.ui.btnIncrementValueAKM1.clicked.connect(self.ValueBlockInSectorIncrementAKM1)
        self.ui.btnIncrementValueAKM2.clicked.connect(self.ValueBlockInSectorIncrementAKM2)
        self.ui.btnIncrementValuePK.clicked.connect(self.ValueBlockInSectorIncrementPK)
         
        self.ui.btnDecrementValue.clicked.connect(self.ValueBlockInSectorDecrement)
        self.ui.btnDecrementValueAKM1.clicked.connect(self.ValueBlockInSectorDecrementAKM1)
        self.ui.btnDecrementValueAKM2.clicked.connect(self.ValueBlockInSectorDecrementAKM2)
        self.ui.btnDecrementValuePK.clicked.connect(self.ValueBlockInSectorDecrementPK)
           
    
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
    
    
    
    
    def ValueBlockInSectorIncrement(self):
        """
          ValueBlock InSector Increment function
        """
        
        if Functions.FunctionOn == True or Functions.ReaderOn == True:return
        Functions.FunctionOn = True
        
        incrementValue = c_int32()
        sectorAddress = c_uint8()
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
             
            sSectorAddress = self.ui.txtSectorAddressIncr.text()
            if not sSectorAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtSectorAddressIncr.setFocus()
                return
                      
            sBlockAddress = self.ui.txtBlockAddressIncr.text()
            if not sBlockAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtBlockAddressIncr.setFocus()
                return
            
            incrementValue = int(sIncrementValue) 
            sectorAddress = int(sSectorAddress)       
            blockAddress = int(sBlockAddress)
            keyIndex = int(self.ui.cboKeyIndex.currentText())
            authMode = MIFARE_AUTHENT1A if self.ui.rbAUTH1A.isChecked() else MIFARE_AUTHENT1B
            
            fnResult = self.mySO.ValueBlockInSectorIncrement(incrementValue,sectorAddress,blockAddress,authMode,keyIndex)
            
            if fnResult == DL_OK:                                               
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_OK,FUNCT_SOUND_OK)
            else:                
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_ERROR,FUNCT_SOUND_ERROR)
        
        finally:
            Functions.FunctionOn = False
    
    
    def ValueBlockInSectorIncrementAKM1(self):
        """
          ValueBlock InSector Increment AKM1 function
        """
        
        if Functions.FunctionOn == True or Functions.ReaderOn == True:return
        Functions.FunctionOn = True
        
        incrementValue = c_int32()
        sectorAddress = c_uint8()
        blockAddress = c_uint8()        
        authMode = c_uint8()
        fnResult = c_int32()
        
        try:
            sIncrementValue = self.ui.txtIncrementValueAKM1.text()
            if not sIncrementValue.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtIncrementValueAKM1.setFocus()
                return
             
            sSectorAddress = self.ui.txtSectorAddressIncrAKM1.text()
            if not sSectorAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtSectorAddressIncrAKM1.setFocus()
                return
                      
            sBlockAddress = self.ui.txtBlockAddressIncrAKM1.text()
            if not sBlockAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtBlockAddressIncrAKM1.setFocus()
                return
            
            incrementValue = int(sIncrementValue) 
            sectorAddress = int(sSectorAddress)       
            blockAddress = int(sBlockAddress)            
            authMode = MIFARE_AUTHENT1A if self.ui.rbAUTH1A.isChecked() else MIFARE_AUTHENT1B
            
            fnResult = self.mySO.ValueBlockInSectorIncrement_AKM1(incrementValue,sectorAddress,blockAddress,authMode)
            
            if fnResult == DL_OK:                                               
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_OK,FUNCT_SOUND_OK)
            else:                
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_ERROR,FUNCT_SOUND_ERROR)
        
        finally:
            Functions.FunctionOn = False
    
    
    def ValueBlockInSectorIncrementAKM2(self):
        """
          ValueBlock InSector Increment AKM2 function
        """
        
        if Functions.FunctionOn == True or Functions.ReaderOn == True:return
        Functions.FunctionOn = True
        
        incrementValue = c_int32()
        sectorAddress = c_uint8()
        blockAddress = c_uint8()        
        authMode = c_uint8()
        fnResult = c_int32()
        
        try:
            sIncrementValue = self.ui.txtIncrementValueAKM2.text()
            if not sIncrementValue.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtIncrementValueAKM2.setFocus()
                return
             
            sSectorAddress = self.ui.txtSectorAddressIncrAKM2.text()
            if not sSectorAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtSectorAddressIncrAKM2.setFocus()
                return
                      
            sBlockAddress = self.ui.txtBlockAddressIncrAKM2.text()
            if not sBlockAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtBlockAddressIncrAKM2.setFocus()
                return
            
            incrementValue = int(sIncrementValue) 
            sectorAddress = int(sSectorAddress)       
            blockAddress = int(sBlockAddress)            
            authMode = MIFARE_AUTHENT1A if self.ui.rbAUTH1A.isChecked() else MIFARE_AUTHENT1B
            
            fnResult = self.mySO.ValueBlockInSectorIncrement_AKM2(incrementValue,sectorAddress,blockAddress,authMode)
            
            if fnResult == DL_OK:                                               
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_OK,FUNCT_SOUND_OK)
            else:                
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_ERROR,FUNCT_SOUND_ERROR)
        
        finally:
            Functions.FunctionOn = False
    
    
    
    def ValueBlockInSectorIncrementPK(self):
        """
          ValueBlock InSector Increment PK function
        """
        
        if Functions.FunctionOn == True or Functions.ReaderOn == True:return
        Functions.FunctionOn = True
        
        incrementValue = c_int32()
        sectorAddress = c_uint8()
        blockAddress = c_uint8() 
        pPKKey   = POINTER(c_ubyte)       
        authMode = c_uint8()
        fnResult = c_int32()
        
        try:
            sIncrementValue = self.ui.txtIncrementValuePK.text()
            if not sIncrementValue.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtIncrementValuePK.setFocus()
                return
             
            sSectorAddress = self.ui.txtSectorAddressIncrPK.text()
            if not sSectorAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtSectorAddressIncrPK.setFocus()
                return
                      
            sBlockAddress = self.ui.txtBlockAddressIncrPK.text()
            if not sBlockAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtBlockAddressIncrPK.setFocus()
                return
            
            incrementValue = int(sIncrementValue) 
            sectorAddress = int(sSectorAddress)       
            blockAddress = int(sBlockAddress)
            pPKKey = self.ReadPKKeys()            
            authMode = MIFARE_AUTHENT1A if self.ui.rbAUTH1A.isChecked() else MIFARE_AUTHENT1B
            
            fnResult = self.mySO.ValueBlockInSectorIncrement_PK(incrementValue,sectorAddress,blockAddress,authMode,pPKKey)
            
            if fnResult == DL_OK:                                               
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_OK,FUNCT_SOUND_OK)
            else:                
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_ERROR,FUNCT_SOUND_ERROR)
        
        finally:
            Functions.FunctionOn = False
    
    
    
    
    def ValueBlockInSectorDecrement(self):
        """
          ValueBlock InSector Decrement function
        """
        
        if Functions.FunctionOn == True or Functions.ReaderOn == True:return
        Functions.FunctionOn = True
        
        decrementValue = c_int32()
        sectorAddress = c_uint8()
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
             
            sSectorAddress = self.ui.txtSectorAddressDecr.text()
            if not sSectorAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtSectorAddressDecr.setFocus()
                return
                      
            sBlockAddress = self.ui.txtBlockAddressDecr.text()
            if not sBlockAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtBlockAddressDecr.setFocus()
                return
            
            decrementValue = int(sDecrementValue) 
            sectorAddress = int(sSectorAddress)       
            blockAddress = int(sBlockAddress)
            keyIndex = int(self.ui.cboKeyIndex.currentText())
            authMode = MIFARE_AUTHENT1A if self.ui.rbAUTH1A.isChecked() else MIFARE_AUTHENT1B
            
            fnResult = self.mySO.ValueBlockInSectorDecrement(decrementValue,sectorAddress,blockAddress,authMode,keyIndex)
            
            if fnResult == DL_OK:                                               
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_OK,FUNCT_SOUND_OK)
            else:                
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_ERROR,FUNCT_SOUND_ERROR)
        
        finally:
            Functions.FunctionOn = False
    
    
    
    def ValueBlockInSectorDecrementAKM1(self):
        """
          ValueBlock InSector Decrement AKM1 function
        """
        
        if Functions.FunctionOn == True or Functions.ReaderOn == True:return
        Functions.FunctionOn = True
        
        decrementValue = c_int32()
        sectorAddress = c_uint8()
        blockAddress = c_uint8()        
        authMode = c_uint8()
        fnResult = c_int32()
        
        try:
            sDecrementValue = self.ui.txtDecrementValueAKM1.text()
            if not sDecrementValue.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtDecrementValueAKM1.setFocus()
                return
             
            sSectorAddress = self.ui.txtSectorAddressDecrAKM1.text()
            if not sSectorAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtSectorAddressDecrAKM1.setFocus()
                return
                      
            sBlockAddress = self.ui.txtBlockAddressDecrAKM1.text()
            if not sBlockAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtBlockAddressDecrAKM1.setFocus()
                return
            
            decrementValue = int(sDecrementValue) 
            sectorAddress = int(sSectorAddress)       
            blockAddress = int(sBlockAddress)            
            authMode = MIFARE_AUTHENT1A if self.ui.rbAUTH1A.isChecked() else MIFARE_AUTHENT1B
            
            fnResult = self.mySO.ValueBlockInSectorDecrement_AKM1(decrementValue,sectorAddress,blockAddress,authMode)
            
            if fnResult == DL_OK:                                               
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_OK,FUNCT_SOUND_OK)
            else:                
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_ERROR,FUNCT_SOUND_ERROR)
        
        finally:
            Functions.FunctionOn = False
    
    
    
    def ValueBlockInSectorDecrementAKM2(self):
        """
          ValueBlock InSector Decrement AKM2 function
        """
        
        if Functions.FunctionOn == True or Functions.ReaderOn == True:return
        Functions.FunctionOn = True
        
        decrementValue = c_int32()
        sectorAddress = c_uint8()
        blockAddress = c_uint8()        
        authMode = c_uint8()
        fnResult = c_int32()
        
        try:
            sDecrementValue = self.ui.txtDecrementValueAKM2.text()
            if not sDecrementValue.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtDecrementValueAKM2.setFocus()
                return
             
            sSectorAddress = self.ui.txtSectorAddressDecrAKM2.text()
            if not sSectorAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtSectorAddressDecrAKM2.setFocus()
                return
                      
            sBlockAddress = self.ui.txtBlockAddressDecrAKM2.text()
            if not sBlockAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtBlockAddressDecrAKM2.setFocus()
                return
            
            decrementValue = int(sDecrementValue) 
            sectorAddress = int(sSectorAddress)       
            blockAddress = int(sBlockAddress)            
            authMode = MIFARE_AUTHENT1A if self.ui.rbAUTH1A.isChecked() else MIFARE_AUTHENT1B
            
            fnResult = self.mySO.ValueBlockInSectorDecrement_AKM2(decrementValue,sectorAddress,blockAddress,authMode)
            
            if fnResult == DL_OK:                                               
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_OK,FUNCT_SOUND_OK)
            else:                
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_ERROR,FUNCT_SOUND_ERROR)
        
        finally:
            Functions.FunctionOn = False
            
            
            
    def ValueBlockInSectorDecrementPK(self):
        """
          ValueBlock InSector Decrement PK function
        """
        
        if Functions.FunctionOn == True or Functions.ReaderOn == True:return
        Functions.FunctionOn = True
        
        decrementValue = c_int32()
        sectorAddress = c_uint8()
        blockAddress = c_uint8()        
        authMode = c_uint8()
        pPKKey   = POINTER(c_ubyte) 
        fnResult = c_int32()
        
        try:
            sDecrementValue = self.ui.txtDecrementValuePK.text()
            if not sDecrementValue.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtDecrementValuePK.setFocus()
                return
             
            sSectorAddress = self.ui.txtSectorAddressDecrPK.text()
            if not sSectorAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtSectorAddressDecrPK.setFocus()
                return
                      
            sBlockAddress = self.ui.txtBlockAddressDecrPK.text()
            if not sBlockAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtBlockAddressDecrPK.setFocus()
                return
            
            decrementValue = int(sDecrementValue) 
            sectorAddress = int(sSectorAddress)       
            blockAddress = int(sBlockAddress) 
            pPKKey = self.ReadPKKeys()           
            authMode = MIFARE_AUTHENT1A if self.ui.rbAUTH1A.isChecked() else MIFARE_AUTHENT1B
            
            fnResult = self.mySO.ValueBlockInSectorDecrement_PK(decrementValue,sectorAddress,blockAddress,authMode,pPKKey)
            
            if fnResult == DL_OK:                                               
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_OK,FUNCT_SOUND_OK)
            else:                
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_ERROR,FUNCT_SOUND_ERROR)
        
        finally:
            Functions.FunctionOn = False
    
    