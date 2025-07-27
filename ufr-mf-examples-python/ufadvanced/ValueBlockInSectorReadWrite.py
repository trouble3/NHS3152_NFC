'''
   @author: Vladan S
   @organization: D-Logic  
   @version: 2.0
'''

import sys
import re
from uFCoderAdvanced import *
import Functions
from  ValueBlockInSectorReadWriteForm  import*



class ValueBlockInSectorReadWrite(QDialog,Ui_ValueBlockInSectorRW):
    """
       main class
    """
    def __init__(self,parent=None):
        super(ValueBlockInSectorReadWrite,self).__init__(parent)         
        self.initUI()
        self.mySO = Functions.GetPlatform()         
        self.FillKeyIndex(KEY_INDEX_MAX)            
        self.CreateLineEditForKeys(self.ui.pnlAuth,380,10,"txtPKKey","255",6)
     
    def initUI(self):
        self.ui = Ui_ValueBlockInSectorRW()
        self.ui.setupUi(self)
        
        self.ui.btnValueBlockRead.clicked.connect(self.ValueBlockInSRead)
        self.ui.btnValueBlockReadAKM1.clicked.connect(self.ValueBlockInSReadAKM1)
        self.ui.btnValueBlockReadAKM2.clicked.connect(self.ValueBlockInSReadAKM2)
        self.ui.btnValueBlockReadPK.clicked.connect(self.ValueBlockInSReadPK)
        
        self.ui.btnValueBlockWrite.clicked.connect(self.ValueBlockInSWrite) 
        self.ui.btnValueBlockWriteAKM1.clicked.connect(self.ValueBlockInSWriteAKM1)
        self.ui.btnValueBlockWriteAKM2.clicked.connect(self.ValueBlockInSWriteAKM2)
        self.ui.btnValueBlockWritePK.clicked.connect(self.ValueBlockInSWritePK) 
           
    
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
    
    
    
    
    def ValueBlockInSRead(self):
        """
         Value Block InSector Read function
        """
        
        if Functions.FunctionOn == True or Functions.ReaderOn == True:return
        Functions.FunctionOn = True
        
        valueRead = c_int32()
        sectorAddress = c_uint8()
        valueAddress = c_uint8()
        blockAddress = c_uint8()
        keyIndex = c_uint8()
        authMode = c_uint8()
        fnResult = c_int32()
        
        try:
            
            
            sSectorAddress = self.ui.txtSectorAddressBR.text()
            if not sSectorAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtSectorAddressBR.setFocus()
                return
                      
            sBlockAddress = self.ui.txtValueBlockAddressBR.text()
            if not sBlockAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtValueBlockAddressBR.setFocus()
                return
            
            sectorAddress = int(sSectorAddress)        
            blockAddress = int(sBlockAddress)
            keyIndex = int(self.ui.cboKeyIndex.currentText())
            authMode = MIFARE_AUTHENT1A if self.ui.rbAUTH1A.isChecked() else MIFARE_AUTHENT1B
            
            fnResult = self.mySO.ValueBlockInSectorRead(byref(valueRead),byref(valueAddress),sectorAddress,blockAddress,authMode,keyIndex)
            
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
            
            
            
    def ValueBlockInSReadAKM1(self):
        """
         Value Block InSector Read AKM1 function
        """
        
        if Functions.FunctionOn == True or Functions.ReaderOn == True:return
        Functions.FunctionOn = True
        
        sectorAddress = c_uint8()
        valueRead = c_int32()
        valueAddress = c_uint8()
        blockAddress = c_uint8()        
        authMode = c_uint8()
        fnResult = c_int32()
        
        try:
            sSectorAddress = self.ui.txtSectorAddressBRAKM1.text()
            if not sSectorAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtSectorAddressBRAKM1.setFocus()
                return
                      
            sBlockAddress = self.ui.txtValueBlockAddressBRAKM1.text()
            if not sBlockAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtValueBlockAddressBRAKM1.setFocus()
                return
            
            sectorAddress = int(sSectorAddress)        
            blockAddress = int(sBlockAddress)            
            authMode = MIFARE_AUTHENT1A if self.ui.rbAUTH1A.isChecked() else MIFARE_AUTHENT1B
            
            fnResult = self.mySO.ValueBlockInSectorRead_AKM1(byref(valueRead),byref(valueAddress),sectorAddress, blockAddress,authMode)
            
            if fnResult == DL_OK:                               
                self.ui.txtValueReadDataBRAKM1.setText(str(valueRead.value))
                self.ui.txtValueAddressBRAKM1.setText(str(valueAddress.value))
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_OK,FUNCT_SOUND_OK)
            else:                
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_ERROR,FUNCT_SOUND_ERROR)
        finally:
            Functions.FunctionOn = False
            
            
    def ValueBlockInSReadAKM2(self):
        """
         Value Block InSector Read AKM2 function
        """
        
        if Functions.FunctionOn == True or Functions.ReaderOn == True:return
        Functions.FunctionOn = True
        
        sectorAddress = c_uint8()
        valueRead = c_int32()
        valueAddress = c_uint8()
        blockAddress = c_uint8()        
        authMode = c_uint8()
        fnResult = c_int32()
        
        try:
            sSectorAddress = self.ui.txtSectorAddressBRAKM2.text()
            if not sSectorAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtSectorAddressBRAKM2.setFocus()
                return
                      
            sBlockAddress = self.ui.txtValueBlockAddressBRAKM2.text()
            if not sBlockAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtValueBlockAddressBRAKM2.setFocus()
                return
            
            sectorAddress = int(sSectorAddress)        
            blockAddress = int(sBlockAddress)            
            authMode = MIFARE_AUTHENT1A if self.ui.rbAUTH1A.isChecked() else MIFARE_AUTHENT1B
            
            fnResult = self.mySO.ValueBlockInSectorRead_AKM2(byref(valueRead),byref(valueAddress),sectorAddress, blockAddress,authMode)
            
            if fnResult == DL_OK:                               
                self.ui.txtValueReadDataBRAKM2.setText(str(valueRead.value))
                self.ui.txtValueAddressBRAKM2.setText(str(valueAddress.value))
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_OK,FUNCT_SOUND_OK)
            else:                
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_ERROR,FUNCT_SOUND_ERROR)
        finally:
            Functions.FunctionOn = False
            
    
    def ValueBlockInSReadPK(self):
        """
         Value Block InSector Read PK function
        """
        
        if Functions.FunctionOn == True or Functions.ReaderOn == True:return
        Functions.FunctionOn = True
        
        sectorAddress = c_uint8()
        valueRead = c_int32()
        valueAddress = c_uint8()
        blockAddress = c_uint8()        
        authMode = c_uint8()
        pPKKey   = POINTER(c_ubyte)
        fnResult = c_int32()
        
        try:
            
            sSectorAddress = self.ui.txtSectorAddressBRPK.text()
            if not sSectorAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtSectorAddressBRPK.setFocus()
                return 
                      
            sBlockAddress = self.ui.txtValueBlockAddressBRPK.text()
            if not sBlockAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtValueBlockAddressBRPK.setFocus()
                return
            
            pPKKey = self.ReadPKKeys()
            sectorAddress = int(sSectorAddress)                
            blockAddress = int(sBlockAddress)            
            authMode = MIFARE_AUTHENT1A if self.ui.rbAUTH1A.isChecked() else MIFARE_AUTHENT1B
            
            fnResult = self.mySO.ValueBlockInSectorRead_PK(byref(valueRead),byref(valueAddress),sectorAddress,blockAddress,authMode,pPKKey)
            
            if fnResult == DL_OK:                               
                self.ui.txtValueReadDataBRPK.setText(str(valueRead.value))
                self.ui.txtValueAddressBRPK.setText(str(valueAddress.value))
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_OK,FUNCT_SOUND_OK)
            else:                
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_ERROR,FUNCT_SOUND_ERROR)
        finally:
            Functions.FunctionOn = False
            
            
            
            
    def ValueBlockInSWrite(self):
        """
         Value Block InSector Write function
        """
        
        if Functions.FunctionOn == True or Functions.ReaderOn == True:return
        Functions.FunctionOn = True
        
        valueWrite = c_int32()
        valueAddress = c_uint8()
        sectorAddress = c_uint8()
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
            
            sSectorAddress = self.ui.txtSectorAddressBW.text()
            if not sSectorAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtSectorAddressBW.setFocus()
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
            sectorAddress = int(sSectorAddress)
            valueAddress = int(sValueAddress)                        
            blockAddress = int(sBlockAddress)
            keyIndex = int(self.ui.cboKeyIndex.currentText())
            authMode = MIFARE_AUTHENT1A if self.ui.rbAUTH1A.isChecked() else MIFARE_AUTHENT1B
            
            fnResult = self.mySO.ValueBlockInSectorWrite(valueWrite,valueAddress,sectorAddress, blockAddress,authMode,keyIndex)
            
            if fnResult == DL_OK:                                              
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_OK,FUNCT_SOUND_OK)
            else:                
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_ERROR,FUNCT_SOUND_ERROR)
        finally:
            Functions.FunctionOn = False
    
    
    
    def ValueBlockInSWriteAKM1(self):
        """
         Value Block InSector Write AKM1 function
        """
        
        if Functions.FunctionOn == True or Functions.ReaderOn == True:return
        Functions.FunctionOn = True
        
        valueWrite = c_int32()
        valueAddress = c_uint8()
        sectorAddress = c_uint8()
        blockAddress = c_uint8()        
        authMode = c_uint8()
        fnResult = c_int32()        
        try:
            
            sSectorAddress = self.ui.txtSectorAddressBWAKM1.text()
            if not sSectorAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtSectorAddressBWAKM1.setFocus()
                return 
            
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
            
            sectorAddress = int(sSectorAddress)
            valueWrite = int(sValueWrite)
            valueAddress = int(sValueAddress)                        
            blockAddress = int(sBlockAddress)            
            authMode = MIFARE_AUTHENT1A if self.ui.rbAUTH1A.isChecked() else MIFARE_AUTHENT1B
            
            fnResult = self.mySO.ValueBlockInSectorWrite_AKM1(valueWrite,valueAddress,sectorAddress,blockAddress,authMode)
            
            if fnResult == DL_OK:                                              
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_OK,FUNCT_SOUND_OK)
            else:                
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_ERROR,FUNCT_SOUND_ERROR)
        finally:
            Functions.FunctionOn = False
            
            
    def ValueBlockInSWriteAKM2(self):
        """
         Value Block InSector Write AKM2 function
        """
        
        if Functions.FunctionOn == True or Functions.ReaderOn == True:return
        Functions.FunctionOn = True
        
        valueWrite = c_int32()
        valueAddress = c_uint8()
        sectorAddress = c_uint8()
        blockAddress = c_uint8()        
        authMode = c_uint8()
        fnResult = c_int32()        
        try:
            
            sValueWrite = self.ui.txtValueWriteDataBWAKM2.text()
            if not sValueWrite.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtValueWriteDataBWAKM2.setFocus()
                return
            
            sSectorAddress = self.ui.txtSectorAddressBWAKM2.text()
            if not sSectorAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtSectorAddressBWAKM1.setFocus()
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
            sectorAddress = int(sSectorAddress)
            valueAddress = int(sValueAddress)                        
            blockAddress = int(sBlockAddress)            
            authMode = MIFARE_AUTHENT1A if self.ui.rbAUTH1A.isChecked() else MIFARE_AUTHENT1B
            
            fnResult = self.mySO.ValueBlockInSectorWrite_AKM2(valueWrite,valueAddress,sectorAddress,blockAddress,authMode)
            
            if fnResult == DL_OK:                                              
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_OK,FUNCT_SOUND_OK)
            else:                
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_ERROR,FUNCT_SOUND_ERROR)
        finally:
            Functions.FunctionOn = False
            
            
    def ValueBlockInSWritePK(self):
        """
         Value Block InSector Write PK function
        """
        
        if Functions.FunctionOn == True or Functions.ReaderOn == True:return
        Functions.FunctionOn = True
        
        valueWrite = c_int32()
        valueAddress = c_uint8()
        sectorAddress = c_uint8()
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
            
            sSectorAddress = self.ui.txtSectorAddressBWPK.text()
            if not sSectorAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtSectorAddressBWPK.setFocus()
                return
            
            
            sBlockAddress = self.ui.txtValueBlockAddressBWPK.text()
            if not sValueAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtValueBlockAddressBWPK.setFocus()
                return
            
            valueWrite = int(sValueWrite)
            valueAddress = int(sValueAddress)
            sectorAddress = int(sSectorAddress)                        
            blockAddress = int(sBlockAddress)            
            authMode = MIFARE_AUTHENT1A if self.ui.rbAUTH1A.isChecked() else MIFARE_AUTHENT1B
            pPKKey = self.ReadPKKeys()
            fnResult = self.mySO.ValueBlockInSectorWrite_PK(valueWrite,valueAddress,sectorAddress,blockAddress,authMode,pPKKey)
            
            if fnResult == DL_OK:                                              
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_OK,FUNCT_SOUND_OK)
            else:                
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_ERROR,FUNCT_SOUND_ERROR)
        finally:
            Functions.FunctionOn = False
            
            
