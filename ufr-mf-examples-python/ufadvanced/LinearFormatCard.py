'''
   @author: Vladan S
   @organization: D-Logic  
   @version: 2.0
'''

import sys
import re
from uFCoderAdvanced import *
import Functions
from  LinearFormatCardForm  import*




class LinearFormatCard(QDialog,Ui_LinearFormatCard):
    """
       main class
    """
    def __init__(self,parent=None):
        super(LinearFormatCard,self).__init__(parent)         
        self.initUI()
        self.mySO = Functions.GetPlatform()         
        self.FillKeyIndex(KEY_INDEX_MAX)            
        
        
        self.CreateLineEditForKeys(self.ui.pnlAuth,380,10,"txtPKKey","255",6)
         
        self.CreateLineEditForKeys(self.ui.fmKeyA,56,32,"txtKeyA","255",6)
        self.CreateLineEditForKeys(self.ui.fmKeyB,56,32,"txtKeyB","255",6)
     
    def initUI(self):
        self.ui = Ui_LinearFormatCard()
        self.ui.setupUi(self)
        
        self.ui.btnLinearFormat.clicked.connect(self.LinearFormatCard)
        self.ui.btnLinearFormatAKM1.clicked.connect(self.LinearFormatCardAKM1)
        self.ui.btnLinearFormatAKM2.clicked.connect(self.LinearFormatCardAKM2)
        self.ui.btnLinearFormatPK.clicked.connect(self.LinearFormatCardPK)
        
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
                if self.ui.chkKeyA.checkState() == Qt.Checked or self.ui.chkKeyB.checkState() == Qt.Checked:return False 
                elif int(o.text())>255 :                     
                    o.undo()        
                    o.setMaxLength(3)                                                    
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
    
    
    
    def LinearFormatCard(self):
        """
          Linear Format Card function
        """
          
        if Functions.FunctionOn == True or Functions.ReaderOn == True:return
        Functions.FunctionOn = True
               
        pKeyA = POINTER(c_uint8)
        pKeyB = POINTER(c_uint8)
        blockAccessBits = c_uint8()
        sectorTrailerAccessBits = c_uint8()
        sectorTrailerByte9 = c_uint8()
        sectorFormatted = c_uint8()
        keyIndex = c_uint8()
        authMode = c_uint8()
        fnResult = c_int32()
        
        try:
            sSectorTrailerByte9 = self.ui.txtSectorTrailerByte9.text()
            if not sSectorTrailerByte9.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtSectorTrailerByte9.setFocus()
                return
            
            pKeyA = Functions.ReadKeys("txtKeyA", self.ui.fmKeyA, self.ui.chkKeyA.checkState())
            pKeyB = Functions.ReadKeys("txtKeyB", self.ui.fmKeyB, self.ui.chkKeyB.checkState())
            blockAccessBits = int(self.ui.cboBlockAccessBits.currentText())
            sectorTrailerAccessBits = int(self.ui.cboSectorTrailerAccessBits.currentText())
            sectorTrailerByte9 = int(sSectorTrailerByte9)
            
            keyIndex = int(self.ui.cboKeyIndex.currentText())
            authMode = MIFARE_AUTHENT1A if self.ui.rbAUTH1A.isChecked() else MIFARE_AUTHENT1B
            
            fnResult = self.mySO.LinearFormatCard(pKeyA,blockAccessBits,sectorTrailerAccessBits,sectorTrailerByte9,pKeyB,byref(sectorFormatted),authMode,keyIndex)
            
            if fnResult == DL_OK: 
                self.ui.txtSectorFormatted.setText(str(sectorFormatted.value))                                              
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_OK,FUNCT_SOUND_OK)
            else:                
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_ERROR,FUNCT_SOUND_ERROR)
        
        
        finally:
            Functions.FunctionOn = False
        
        
    
    def LinearFormatCardAKM1(self):
        """
          Linear Format Card AKM1 function
        """
          
        if Functions.FunctionOn == True or Functions.ReaderOn == True:return
        Functions.FunctionOn = True
               
        pKeyA = POINTER(c_uint8)
        pKeyB = POINTER(c_uint8)
        blockAccessBits = c_uint8()
        sectorTrailerAccessBits = c_uint8()
        sectorTrailerByte9 = c_uint8()
        sectorFormatted = c_uint8()        
        authMode = c_uint8()
        fnResult = c_int32()
        
        try:
            sSectorTrailerByte9 = self.ui.txtSectorTrailerByte9AKM1.text()
            if not sSectorTrailerByte9.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtSectorTrailerByte9AKM1.setFocus()
                return
            
            pKeyA = Functions.ReadKeys("txtKeyA", self.ui.fmKeyA, self.ui.chkKeyA.checkState())
            pKeyB = Functions.ReadKeys("txtKeyB", self.ui.fmKeyB, self.ui.chkKeyB.checkState())
            blockAccessBits = int(self.ui.cboBlockAccessBitsAKM1.currentText())
            sectorTrailerAccessBits = int(self.ui.cboSectorTrailerAccessBitsAKM1.currentText())
            sectorTrailerByte9 = int(sSectorTrailerByte9)
                        
            authMode = MIFARE_AUTHENT1A if self.ui.rbAUTH1A.isChecked() else MIFARE_AUTHENT1B
            
            fnResult = self.mySO.LinearFormatCard_AKM1(pKeyA,blockAccessBits,sectorTrailerAccessBits,sectorTrailerByte9,pKeyB,byref(sectorFormatted),authMode)
            
            if fnResult == DL_OK: 
                self.ui.txtSectorFormattedAKM1.setText(str(sectorFormatted.value))                                              
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_OK,FUNCT_SOUND_OK)
            else:                
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_ERROR,FUNCT_SOUND_ERROR)
        
        
        finally:
            Functions.FunctionOn = False    
    
    
    def LinearFormatCardAKM2(self):
        """
          Linear Format Card AKM2 function
        """
          
        if Functions.FunctionOn == True or Functions.ReaderOn == True:return
        Functions.FunctionOn = True
               
        pKeyA = POINTER(c_uint8)
        pKeyB = POINTER(c_uint8)
        blockAccessBits = c_uint8()
        sectorTrailerAccessBits = c_uint8()
        sectorTrailerByte9 = c_uint8()
        sectorFormatted = c_uint8()        
        authMode = c_uint8()
        fnResult = c_int32()
        
        try:
            sSectorTrailerByte9 = self.ui.txtSectorTrailerByte9AKM2.text()
            if not sSectorTrailerByte9.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtSectorTrailerByte9AKM2.setFocus()
                return
            
            pKeyA = Functions.ReadKeys("txtKeyA", self.ui.fmKeyA, self.ui.chkKeyA.checkState())
            pKeyB = Functions.ReadKeys("txtKeyB", self.ui.fmKeyB, self.ui.chkKeyB.checkState())
            blockAccessBits = int(self.ui.cboBlockAccessBitsAKM2.currentText())
            sectorTrailerAccessBits = int(self.ui.cboSectorTrailerAccessBitsAKM2.currentText())
            sectorTrailerByte9 = int(sSectorTrailerByte9)
                        
            authMode = MIFARE_AUTHENT1A if self.ui.rbAUTH1A.isChecked() else MIFARE_AUTHENT1B
            
            fnResult = self.mySO.LinearFormatCard_AKM2(pKeyA,blockAccessBits,sectorTrailerAccessBits,sectorTrailerByte9,pKeyB,byref(sectorFormatted),authMode)
            
            if fnResult == DL_OK: 
                self.ui.txtSectorFormattedAKM2.setText(str(sectorFormatted.value))                                              
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_OK,FUNCT_SOUND_OK)
            else:                
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_ERROR,FUNCT_SOUND_ERROR)
        
        
        finally:
            Functions.FunctionOn = False    
    
    
    def LinearFormatCardPK(self):
        """
          Linear Format Card PK function
        """
          
        if Functions.FunctionOn == True or Functions.ReaderOn == True:return
        Functions.FunctionOn = True
               
        pKeyA = POINTER(c_uint8)
        pKeyB = POINTER(c_uint8)
        pPKKey = POINTER(c_ubyte)
        blockAccessBits = c_uint8()
        sectorTrailerAccessBits = c_uint8()
        sectorTrailerByte9 = c_uint8()
        sectorFormatted = c_uint8()        
        authMode = c_uint8()
        fnResult = c_int32()
        
        try:
            sSectorTrailerByte9 = self.ui.txtSectorTrailerByte9PK.text()
            if not sSectorTrailerByte9.isnumeric():
                QtWidgets.QMessageBox.warning(self,'Warning','You must enter any number !',QtWidgets.QMessageBox.Ok)
                self.ui.txtSectorTrailerByte9PK.setFocus()
                return
            
            pPKKey = self.ReadPKKeys()
            pKeyA = Functions.ReadKeys("txtKeyA", self.ui.fmKeyA, self.ui.chkKeyA.checkState())
            pKeyB = Functions.ReadKeys("txtKeyB", self.ui.fmKeyB, self.ui.chkKeyB.checkState())
            blockAccessBits = int(self.ui.cboBlockAccessBitsPK.currentText())
            sectorTrailerAccessBits = int(self.ui.cboSectorTrailerAccessBitsPK.currentText())
            sectorTrailerByte9 = int(sSectorTrailerByte9)
                        
            authMode = MIFARE_AUTHENT1A if self.ui.rbAUTH1A.isChecked() else MIFARE_AUTHENT1B
            
            fnResult = self.mySO.LinearFormatCard_PK(pKeyA,blockAccessBits,sectorTrailerAccessBits,sectorTrailerByte9,pKeyB,byref(sectorFormatted),authMode,pPKKey)
            
            if fnResult == DL_OK: 
                self.ui.txtSectorFormattedPK.setText(str(sectorFormatted.value))                                              
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_OK,FUNCT_SOUND_OK)
            else:                
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_ERROR,FUNCT_SOUND_ERROR)
        
        
        finally:
            Functions.FunctionOn = False    
    
