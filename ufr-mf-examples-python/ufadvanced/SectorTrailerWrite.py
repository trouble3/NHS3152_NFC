'''
   @author: Vladan S
   @organization: D-Logic  
   @version: 2.0
'''

import sys
import re
from uFCoderAdvanced import *
import Functions
from  SectorTrailerWriteForm  import*




class SectorTrailerWrite(QDialog,Ui_SectorTrailerWrite):
    """
       main class
    """
    def __init__(self,parent=None):
        super(SectorTrailerWrite,self).__init__(parent)         
        self.initUI()
        self.mySO = Functions.GetPlatform()         
        self.FillKeyIndex(KEY_INDEX_MAX)            
        
        
        self.CreateLineEditForKeys(self.ui.pnlAuth,380,10,"txtPKKey","255",6)
         
        self.CreateLineEditForKeys(self.ui.fmKeyA,56,32,"txtKeyA","255",6)
        self.CreateLineEditForKeys(self.ui.fmKeyB,56,32,"txtKeyB","255",6)
     
    def initUI(self):
        self.ui = Ui_SectorTrailerWrite()
        self.ui.setupUi(self)
        
        self.ui.btnSectorTrailerWrite.clicked.connect(self.SectorTrailerWrite)
        self.ui.btnSectorTrailerWriteAKM1.clicked.connect(self.SectorTrailerWriteAKM1)
        self.ui.btnSectorTrailerWriteAKM2.clicked.connect(self.SectorTrailerWriteAKM2)
        self.ui.btnSectorTrailerWritePK.clicked.connect(self.SectorTrailerWritePK)
        
        self.ui.chkKeyA.stateChanged.connect(self.KeyACheckBoxToHex) 
        self.ui.chkKeyB.stateChanged.connect(self.KeyBCheckBoxToHex)
           
    
    def FillKeyIndex(self,count):
        
        for n in range(0,count):
            self.ui.cboKeyIndex.addItem(str(n))
            
    def CreateLineEditForKeys(self,parent,xOsa,yOsa,name,value,count):
        i = 0
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
            xSpace += 32
      
   
     
    def eventFilter(self, o, ev):
            if ev.type() == QEvent.FocusIn:                            
                if self.ui.chkKeyA.checkState() == Qt.Checked or self.ui.chkKeyB.checkState() == Qt.Checked: 
                    o.setMaxLength(2)
                else:
                    o.setMaxLength(3)
                return False             
            if ev.type() == QEvent.FocusOut: 
                if o.text() == '' : o.undo()                
                if self.ui.chkKeyA.checkState() == Qt.Checked or self.ui.chkKeyB.checkState() == Qt.Checked:return 
                elif int(o.text())>255 : 
                    o.undo()                                                            
                return False                     
            #else:                               
            return QtCore.QObject.eventFilter(self, o,ev)          
      
    def RegKey(self):
        sender  = self.sender()             
        sendText = sender.text() 
        if self.ui.chkKeyA.checkState() == Qt.Checked or self.ui.chkKeyB.checkState() == Qt.Checked:                
            match = re.search('[g-zG-Z]',sendText)        
            if match:                 
                sender.backspace() 
             
    
    def KeyACheckBoxToHex(self,state):
        Functions.DecHexCheckBox("txtKeyA",self.ui.fmKeyA, state)
        
    def KeyBCheckBoxToHex(self,state):
        Functions.DecHexCheckBox("txtKeyB",self.ui.fmKeyB, state)      
            
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
    
    
    
    def SectorTrailerWrite(self):
        """
          Sector Trailer Write function
        """
          
        if Functions.FunctionOn == True or Functions.ReaderOn == True:return
        Functions.FunctionOn = True
               
        pKeyA = POINTER(c_uint8)
        pKeyB = POINTER(c_uint8)
        addressingMode = c_uint8()
        blockOrSectorAddress = c_uint8()
        accessBits0 = c_uint8()
        accessBits1 = c_uint8()
        accessBits2 = c_uint8()       
        sectorTrailerAccessBits = c_uint8()
        sectorTrailerByte9 = c_uint8()        
        keyIndex = c_uint8()
        authMode = c_uint8()
        fnResult = c_int32()
        
        try:
            
            sBlockOrSectorAddress = self.ui.txtBlockOrSectorAddress.text()
            if not sBlockOrSectorAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtBlockOrSectorAddress.setFocus()
                return
                                
            sSectorTrailerByte9 = self.ui.txtSectorTrailerByte9.text()
            if not sSectorTrailerByte9.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtSectorTrailerByte9.setFocus()
                return
            
            pKeyA = Functions.ReadKeys("txtKeyA", self.ui.fmKeyA, self.ui.chkKeyA.checkState())
            pKeyB = Functions.ReadKeys("txtKeyB", self.ui.fmKeyB, self.ui.chkKeyB.checkState())
            
            addressingMode = int(self.ui.cboAddressingMode.currentText())
            blockOrSectorAddress = int(sBlockOrSectorAddress)
            accessBits0 = int(self.ui.cboAccessBits0.currentText())
            accessBits1 = int(self.ui.cboAccessBits1.currentText())
            accessBits2 = int(self.ui.cboAccessBits2.currentText())
            sectorTrailerAccessBits = int(self.ui.cboTrailerAccessBits.currentText())                        
            sectorTrailerByte9 = int(sSectorTrailerByte9)
            keyIndex = int(self.ui.cboKeyIndex.currentText())            
            authMode = MIFARE_AUTHENT1A if self.ui.rbAUTH1A.isChecked() else MIFARE_AUTHENT1B
            
            fnResult = self.mySO.SectorTrailerWrite(addressingMode,blockOrSectorAddress,pKeyA,accessBits0,accessBits1,accessBits2,sectorTrailerAccessBits,sectorTrailerByte9,pKeyB,authMode,keyIndex)
            
            if fnResult == DL_OK:                                                             
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_OK,FUNCT_SOUND_OK)
            else:                
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_ERROR,FUNCT_SOUND_ERROR)
        
        
        finally:
            Functions.FunctionOn = False
    
    
    def SectorTrailerWriteAKM1(self):
        """
          Sector Trailer Write AKM1 function
        """
          
        if Functions.FunctionOn == True or Functions.ReaderOn == True:return
        Functions.FunctionOn = True
               
        pKeyA = POINTER(c_uint8)
        pKeyB = POINTER(c_uint8)
        addressingMode = c_uint8()
        blockOrSectorAddress = c_uint8()
        accessBits0 = c_uint8()
        accessBits1 = c_uint8()
        accessBits2 = c_uint8()       
        sectorTrailerAccessBits = c_uint8()
        sectorTrailerByte9 = c_uint8()                
        authMode = c_uint8()
        fnResult = c_int32()
        
        try:
            
            sBlockOrSectorAddress = self.ui.txtBlockOrSectorAddressAKM1.text()
            if not sBlockOrSectorAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtBlockOrSectorAddressAKM1.setFocus()
                return
                                
            sSectorTrailerByte9 = self.ui.txtSectorTrailerByte9AKM1.text()
            if not sSectorTrailerByte9.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtSectorTrailerByte9AKM1.setFocus()
                return
            
            pKeyA = Functions.ReadKeys("txtKeyA", self.ui.fmKeyA, self.ui.chkKeyA.checkState())
            pKeyB = Functions.ReadKeys("txtKeyB", self.ui.fmKeyB, self.ui.chkKeyB.checkState())
            
            addressingMode = int(self.ui.cboAddressingModeAKM1.currentText())
            blockOrSectorAddress = int(sBlockOrSectorAddress)
            accessBits0 = int(self.ui.cboAccessBits0AKM1.currentText())
            accessBits1 = int(self.ui.cboAccessBits1AKM1.currentText())
            accessBits2 = int(self.ui.cboAccessBits2AKM1.currentText())
            sectorTrailerAccessBits = int(self.ui.cboTrailerAccessBitsAKM1.currentText())                        
            sectorTrailerByte9 = int(sSectorTrailerByte9)
                       
            authMode = MIFARE_AUTHENT1A if self.ui.rbAUTH1A.isChecked() else MIFARE_AUTHENT1B
            
            fnResult = self.mySO.SectorTrailerWrite_AKM1(addressingMode,blockOrSectorAddress,pKeyA,accessBits0,accessBits1,accessBits2,sectorTrailerAccessBits,sectorTrailerByte9,pKeyB,authMode)
            
            if fnResult == DL_OK:                                                             
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_OK,FUNCT_SOUND_OK)
            else:                
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_ERROR,FUNCT_SOUND_ERROR)
        
        
        finally:
            Functions.FunctionOn = False
        
    
    
    def SectorTrailerWriteAKM2(self):
        """
          Sector Trailer Write AKM2 function
        """
          
        if Functions.FunctionOn == True or Functions.ReaderOn == True:return
        Functions.FunctionOn = True
               
        pKeyA = POINTER(c_uint8)
        pKeyB = POINTER(c_uint8)
        addressingMode = c_uint8()
        blockOrSectorAddress = c_uint8()
        accessBits0 = c_uint8()
        accessBits1 = c_uint8()
        accessBits2 = c_uint8()       
        sectorTrailerAccessBits = c_uint8()
        sectorTrailerByte9 = c_uint8()                
        authMode = c_uint8()
        fnResult = c_int32()
        
        try:
            
            sBlockOrSectorAddress = self.ui.txtBlockOrSectorAddressAKM2.text()
            if not sBlockOrSectorAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtBlockOrSectorAddressAKM2.setFocus()
                return
                                
            sSectorTrailerByte9 = self.ui.txtSectorTrailerByte9AKM2.text()
            if not sSectorTrailerByte9.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtSectorTrailerByte9AKM2.setFocus()
                return
            
            pKeyA = Functions.ReadKeys("txtKeyA", self.ui.fmKeyA, self.ui.chkKeyA.checkState())
            pKeyB = Functions.ReadKeys("txtKeyB", self.ui.fmKeyB, self.ui.chkKeyB.checkState())
            
            addressingMode = int(self.ui.cboAddressingModeAKM2.currentText())
            blockOrSectorAddress = int(sBlockOrSectorAddress)
            accessBits0 = int(self.ui.cboAccessBits0AKM2.currentText())
            accessBits1 = int(self.ui.cboAccessBits1AKM2.currentText())
            accessBits2 = int(self.ui.cboAccessBits2AKM2.currentText())
            sectorTrailerAccessBits = int(self.ui.cboTrailerAccessBitsAKM2.currentText())                        
            sectorTrailerByte9 = int(sSectorTrailerByte9)
                       
            authMode = MIFARE_AUTHENT1A if self.ui.rbAUTH1A.isChecked() else MIFARE_AUTHENT1B
            
            fnResult = self.mySO.SectorTrailerWrite_AKM2(addressingMode,blockOrSectorAddress,pKeyA,accessBits0,accessBits1,accessBits2,sectorTrailerAccessBits,sectorTrailerByte9,pKeyB,authMode)
            
            if fnResult == DL_OK:                                                             
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_OK,FUNCT_SOUND_OK)
            else:                
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_ERROR,FUNCT_SOUND_ERROR)
        
        finally:
            Functions.FunctionOn = False
            
    
    def SectorTrailerWritePK(self):
        """
          Sector Trailer Write PK function
        """
          
        if Functions.FunctionOn == True or Functions.ReaderOn == True:return
        Functions.FunctionOn = True
               
        pKeyA = POINTER(c_uint8)
        pKeyB = POINTER(c_uint8)
        pPKKey = POINTER(c_ubyte)
        addressingMode = c_uint8()
        blockOrSectorAddress = c_uint8()
        accessBits0 = c_uint8()
        accessBits1 = c_uint8()
        accessBits2 = c_uint8()       
        sectorTrailerAccessBits = c_uint8()
        sectorTrailerByte9 = c_uint8()                
        authMode = c_uint8()
        fnResult = c_int32()
        
        try:
            
            sBlockOrSectorAddress = self.ui.txtBlockOrSectorAddressPK.text()
            if not sBlockOrSectorAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtBlockOrSectorAddressPK.setFocus()
                return
                                
            sSectorTrailerByte9 = self.ui.txtSectorTrailerByte9PK.text()
            if not sSectorTrailerByte9.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtSectorTrailerByte9PK.setFocus()
                return
            
            pPKKey = self.ReadPKKeys()
            pKeyA = Functions.ReadKeys("txtKeyA", self.ui.fmKeyA, self.ui.chkKeyA.checkState())
            pKeyB = Functions.ReadKeys("txtKeyB", self.ui.fmKeyB, self.ui.chkKeyB.checkState())
            
            addressingMode = int(self.ui.cboAddressingModePK.currentText())
            blockOrSectorAddress = int(sBlockOrSectorAddress)
            accessBits0 = int(self.ui.cboAccessBits0PK.currentText())
            accessBits1 = int(self.ui.cboAccessBits1PK.currentText())
            accessBits2 = int(self.ui.cboAccessBits2PK.currentText())
            sectorTrailerAccessBits = int(self.ui.cboTrailerAccessBitsPK.currentText())                        
            sectorTrailerByte9 = int(sSectorTrailerByte9)
                       
            authMode = MIFARE_AUTHENT1A if self.ui.rbAUTH1A.isChecked() else MIFARE_AUTHENT1B
            
            fnResult = self.mySO.SectorTrailerWrite_PK(addressingMode,blockOrSectorAddress,pKeyA,accessBits0,accessBits1,accessBits2,sectorTrailerAccessBits,sectorTrailerByte9,pKeyB,authMode,pPKKey)
            
            if fnResult == DL_OK:                                                             
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_OK,FUNCT_SOUND_OK)
            else:                
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_ERROR,FUNCT_SOUND_ERROR)
        
        
        finally:
            Functions.FunctionOn = False
        
        