'''
   @author: Vladan S
   @organization: D-Logic  
   @version: 2.0
'''

import sys
import re
from uFCoderAdvanced import *
import Functions
from BlockInSectorReadWriteForm import*

class BlockRWInSector(QDialog,Ui_BlockRWInSector):
    """
       main class
    """
    def __init__(self,parent=None):
        super(BlockRWInSector,self).__init__(parent)         
        self.initUI()
        self.mySO = Functions.GetPlatform()         
        self.FillKeyIndex(KEY_INDEX_MAX)            
        self.CreateLineEditForKeys(self.ui.pnlAuth,380,10,"txtPKKey","255",6)
     
    def initUI(self):
        self.ui = Ui_BlockRWInSector()
        self.ui.setupUi(self)
        
        self.ui.btnBlockInSRead.clicked.connect(self.BlockInSectorRead)
        self.ui.btnBlockInSReadAKM1.clicked.connect(self.BlockInSectorReadAKM1)
        self.ui.btnBlockInSReadAKM2.clicked.connect(self.BlockInSectorReadAKM2)
        self.ui.btnBlockInSReadPK.clicked.connect(self.BlockInSectorReadPK)
        
        self.ui.btnBlockInSWrite.clicked.connect(self.BlockInSectorWrite)
        self.ui.btnBlockInSWriteAKM1.clicked.connect(self.BlockInSectorWriteAKM1)
        self.ui.btnBlockInSWriteAKM2.clicked.connect(self.BlockInSectorWriteAKM2)
        self.ui.btnBlockInSWritePK.clicked.connect(self.BlockInSectorWritePK)
    
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
    
    
    
    
    
    
    def BlockInSectorRead(self):        
        """
           BlockInSector Read function
        """
                 
        if Functions.FunctionOn == True or Functions.ReaderOn == True:return
        Functions.FunctionOn = True 
        
        blockAddress = c_uint8()
        blockInSectAddress = c_uint8()
        blockRead = (c_uint8 * MAX_BLOCK)()
        pBlockRead = POINTER(c_uint8)
        keyIndex = c_uint8()
        fnResult = c_uint32()
        
        try:
            
            sBlockInSectAddress = self.ui.txtSectorAddressBR.displayText()
            if not sBlockInSectAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,"Warning","You must enter any number !",QtWidgets.QMessageBox.Ok)
                self.ui.txtSectorAddressBR.setFocus()
                return
            
            sBlockAddress = self.ui.txtBlockInSAddressBR.displayText()
            if not sBlockAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,"Warning","You must enter any number !",QtWidgets.QMessageBox.Ok)
                self.ui.txtBlockInSAddressBR.setFocus()
                return
            
            pBlockRead = blockRead
            blockAddress = int(sBlockAddress)
            blockInSectAddress = int(sBlockInSectAddress)
            keyIndex = int(self.ui.cboKeyIndex.currentText())
            authMode = MIFARE_AUTHENT1A if self.ui.rbAUTH1A.isChecked() else MIFARE_AUTHENT1B
            
            fnResult = self.mySO.BlockInSectorRead(pBlockRead,blockInSectAddress,blockAddress,authMode,keyIndex)
            
            if fnResult == DL_OK:                
                li = [chr(i) for i in blockRead]                                
                self.ui.txtReadInSDataBR.setText(''.join(li))
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_OK,FUNCT_SOUND_OK)
            else:                
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_ERROR,FUNCT_SOUND_ERROR)
         
        finally:
            Functions.FunctionOn = False
     
       
        
    def BlockInSectorReadAKM1(self):        
        """
           BlockInSector Read AKM1 function
        """
                 
        if Functions.FunctionOn == True or Functions.ReaderOn == True:return
        Functions.FunctionOn = True 
        
        blockAddress = c_uint8()
        blockInSectAddress = c_uint8()
        blockRead = (c_uint8 * MAX_BLOCK)()
        pBlockRead = POINTER(c_uint8)        
        fnResult = c_uint32()
        
        try:
            
            sBlockInSectAddress = self.ui.txtSectorAddressBRAKM1.displayText()
            if not sBlockInSectAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,"Warning","You must enter any number !",QtWidgets.QMessageBox.Ok)
                self.ui.txtSectorAddressBRAKM1.setFocus()
                return
            
            sBlockAddress = self.ui.txtBlockInSAddressBRAKM1.displayText()
            if not sBlockAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,"Warning","You must enter any number !",QtWidgets.QMessageBox.Ok)
                self.ui.txtBlockInSAddressBRAKM1.setFocus()
                return
            
            pBlockRead = blockRead
            blockAddress = int(sBlockAddress)
            blockInSectAddress = int(sBlockInSectAddress)            
            authMode = MIFARE_AUTHENT1A if self.ui.rbAUTH1A.isChecked() else MIFARE_AUTHENT1B
            
            fnResult = self.mySO.BlockInSectorRead_AKM1(pBlockRead,blockInSectAddress,blockAddress,authMode)
            
            if fnResult == DL_OK:                
                li = [chr(i) for i in blockRead]                                
                self.ui.txtReadInSDataBRAKM1.setText(''.join(li))
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_OK,FUNCT_SOUND_OK)
            else:                
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_ERROR,FUNCT_SOUND_ERROR)
         
        finally:
            Functions.FunctionOn = False 
    
    
    
    def BlockInSectorReadAKM2(self):        
        """
           BlockInSector Read AKM2 function
        """
                 
        if Functions.FunctionOn == True or Functions.ReaderOn == True:return
        Functions.FunctionOn = True 
        
        blockAddress = c_uint8()
        blockInSectAddress = c_uint8()
        blockRead = (c_uint8 * MAX_BLOCK)()
        pBlockRead = POINTER(c_uint8)        
        fnResult = c_uint32()
        
        try:
            
            sBlockInSectAddress = self.ui.txtSectorAddressBRAKM2.displayText()
            if not sBlockInSectAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,"Warning","You must enter any number !",QtWidgets.QMessageBox.Ok)
                self.ui.txtSectorAddressBRAKM2.setFocus()
                return
            
            sBlockAddress = self.ui.txtBlockInSAddressBRAKM2.displayText()
            if not sBlockAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,"Warning","You must enter any number !",QtWidgets.QMessageBox.Ok)
                self.ui.txtBlockInSAddressBRAKM2.setFocus()
                return
            
            pBlockRead = blockRead
            blockAddress = int(sBlockAddress)
            blockInSectAddress = int(sBlockInSectAddress)            
            authMode = MIFARE_AUTHENT1A if self.ui.rbAUTH1A.isChecked() else MIFARE_AUTHENT1B
            
            fnResult = self.mySO.BlockInSectorRead_AKM2(pBlockRead,blockInSectAddress,blockAddress,authMode)
            
            if fnResult == DL_OK:                
                li = [chr(i) for i in blockRead]                                
                self.ui.txtReadInSDataBRAKM2.setText(''.join(li))
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_OK,FUNCT_SOUND_OK)
            else:                
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_ERROR,FUNCT_SOUND_ERROR)
         
        finally:
            Functions.FunctionOn = False     
    
    def BlockInSectorReadPK(self):        
        """
           BlockInSector Read PK function
        """
                 
        if Functions.FunctionOn == True or Functions.ReaderOn == True:return
        Functions.FunctionOn = True 
        
        blockAddress = c_uint8()
        blockInSectAddress = c_uint8()
        blockRead = (c_uint8 * MAX_BLOCK)()
        pBlockRead = POINTER(c_uint8)        
        pPKKey   = POINTER(c_ubyte)        
        fnResult = c_uint32()
        
        try:
            
            sBlockInSectAddress = self.ui.txtSectorAddressBRPK.displayText()
            if not sBlockInSectAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,"Warning","You must enter any number !",QtWidgets.QMessageBox.Ok)
                self.ui.txtSectorAddressBRPK.setFocus()
                return
            
            sBlockAddress = self.ui.txtBlockInSAddressBRPK.displayText()
            if not sBlockAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,"Warning","You must enter any number !",QtWidgets.QMessageBox.Ok)
                self.ui.txtBlockInSAddressBRPK.setFocus()
                return
            
            pBlockRead = blockRead
            blockAddress = int(sBlockAddress)
            blockInSectAddress = int(sBlockInSectAddress)            
            authMode = MIFARE_AUTHENT1A if self.ui.rbAUTH1A.isChecked() else MIFARE_AUTHENT1B
            
            
            pPKKey = self.ReadPKKeys()
            
            fnResult = self.mySO.BlockInSectorRead_PK(pBlockRead,blockInSectAddress,blockAddress,authMode,pPKKey)
            
            if fnResult == DL_OK:                
                li = [chr(i) for i in blockRead]                                
                self.ui.txtReadInSDataBRPK.setText(''.join(li))
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_OK,FUNCT_SOUND_OK)
            else:                
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_ERROR,FUNCT_SOUND_ERROR)
         
        finally:
            Functions.FunctionOn = False     
    
    
    
    def BlockInSectorWrite(self):        
        """
           BlockInSector Write function
        """
                 
        if Functions.FunctionOn == True or Functions.ReaderOn == True:return
        Functions.FunctionOn = True 
        
        blockAddress = c_uint8()
        blockInSectAddress = c_uint8()
        blockWrite = (c_uint8 * MAX_BLOCK)()
        pBlockWrite = POINTER(c_uint8)
        keyIndex = c_uint8()
        fnResult = c_uint32()
        
        try:
            
            sBlockInSectAddress = self.ui.txtSectorAddressBW.displayText()
            if not sBlockInSectAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,"Warning","You must enter any number !",QtWidgets.QMessageBox.Ok)
                self.ui.txtSectorAddressBW.setFocus()
                return
            
            sBlockAddress = self.ui.txtBlockInSAddressBW.displayText()
            if not sBlockAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,"Warning","You must enter any number !",QtWidgets.QMessageBox.Ok)
                self.ui.txtBlockInSAddressBW.setFocus()
                return
            
            sBlockWrite = self.ui.txtWriteInSDataBW.text()
            if sBlockWrite.strip() == '':
                QtWidgets.QMessageBox.warning(self,"Warning","You must enter any value !",QtWidgets.QMessageBox.Ok)
                self.ui.txtWriteInSDataBW.setFocus()
                return
                
            
            
            blockWrite = str.encode(sBlockWrite)
            pBlockWrite = blockWrite
            blockAddress = int(sBlockAddress)
            blockInSectAddress = int(sBlockInSectAddress)
            keyIndex = int(self.ui.cboKeyIndex.currentText())
            authMode = MIFARE_AUTHENT1A if self.ui.rbAUTH1A.isChecked() else MIFARE_AUTHENT1B
            
            fnResult = self.mySO.BlockInSectorWrite(pBlockWrite,blockInSectAddress,blockAddress,authMode,keyIndex)
            
            if fnResult == DL_OK:                                
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_OK,FUNCT_SOUND_OK)
            else:                
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_ERROR,FUNCT_SOUND_ERROR)
         
        finally:
            Functions.FunctionOn = False
    
    
    def BlockInSectorWriteAKM1(self):        
        """
           BlockInSector Write AKM1 function
        """
                 
        if Functions.FunctionOn == True or Functions.ReaderOn == True:return
        Functions.FunctionOn = True 
        
        blockAddress = c_uint8()
        blockInSectAddress = c_uint8()
        blockWrite = (c_uint8 * MAX_BLOCK)()
        pBlockWrite = POINTER(c_uint8)        
        fnResult = c_uint32()
        
        try:
            
            sBlockInSectAddress = self.ui.txtSectorAddressBWAKM1.displayText()
            if not sBlockInSectAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,"Warning","You must enter any number !",QtWidgets.QMessageBox.Ok)
                self.ui.txtSectorAddressBWAKM1.setFocus()
                return
            
            sBlockAddress = self.ui.txtBlockInSAddressBWAKM1.displayText()
            if not sBlockAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,"Warning","You must enter any number !",QtWidgets.QMessageBox.Ok)
                self.ui.txtBlockInSAddressBWAKM1.setFocus()
                return
            
            sBlockWrite = self.ui.txtWriteInSDataBWAKM1.text()
            if sBlockWrite.strip() == '':
                QtWidgets.QMessageBox.warning(self,"Warning","You must enter any value !",QtWidgets.QMessageBox.Ok)
                self.ui.txtWriteInSDataBWAKM1.setFocus()
                return
            
            blockWrite = str.encode(sBlockWrite)
            pBlockWrite = blockWrite
            blockAddress = int(sBlockAddress)
            blockInSectAddress = int(sBlockInSectAddress)            
            authMode = MIFARE_AUTHENT1A if self.ui.rbAUTH1A.isChecked() else MIFARE_AUTHENT1B
            
            fnResult = self.mySO.BlockInSectorWrite_AKM1(pBlockWrite,blockInSectAddress,blockAddress,authMode)
            
            if fnResult == DL_OK:                                
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_OK,FUNCT_SOUND_OK)
            else:                
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_ERROR,FUNCT_SOUND_ERROR)
         
        finally:
            Functions.FunctionOn = False
    
    
    def BlockInSectorWriteAKM2(self):        
        """
           BlockInSector Write AKM2 function
        """
                 
        if Functions.FunctionOn == True or Functions.ReaderOn == True:return
        Functions.FunctionOn = True 
        
        blockAddress = c_uint8()
        blockInSectAddress = c_uint8()
        blockWrite = (c_uint8 * MAX_BLOCK)()
        pBlockWrite = POINTER(c_uint8)        
        fnResult = c_uint32()
        
        try:
            
            sBlockInSectAddress = self.ui.txtSectorAddressBWAKM2.displayText()
            if not sBlockInSectAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,"Warning","You must enter any number !",QtWidgets.QMessageBox.Ok)
                self.ui.txtSectorAddressBWAKM2.setFocus()
                return
            
            sBlockAddress = self.ui.txtBlockInSAddressBWAKM2.displayText()
            if not sBlockAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,"Warning","You must enter any number !",QtWidgets.QMessageBox.Ok)
                self.ui.txtBlockInSAddressBWAKM2.setFocus()
                return
            
            sBlockWrite = self.ui.txtWriteInSDataBWAKM2.text()
            if sBlockWrite.strip() == '':
                QtWidgets.QMessageBox.warning(self,"Warning","You must enter any value !",QtWidgets.QMessageBox.Ok)
                self.ui.txtWriteInSDataBWAKM2.setFocus()
                return
            
            blockWrite = str.encode(sBlockWrite)
            pBlockWrite = blockWrite            
            blockAddress = int(sBlockAddress)
            blockInSectAddress = int(sBlockInSectAddress)            
            authMode = MIFARE_AUTHENT1A if self.ui.rbAUTH1A.isChecked() else MIFARE_AUTHENT1B
            
            fnResult = self.mySO.BlockInSectorWrite_AKM2(pBlockWrite,blockInSectAddress,blockAddress,authMode)
            
            if fnResult == DL_OK:                                
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_OK,FUNCT_SOUND_OK)
            else:                
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_ERROR,FUNCT_SOUND_ERROR)
         
        finally:
            Functions.FunctionOn = False
    
    
    def BlockInSectorWritePK(self):        
        """
           BlockInSector Write PK function
        """
                 
        if Functions.FunctionOn == True or Functions.ReaderOn == True:return
        Functions.FunctionOn = True 
        
        blockAddress = c_uint8()
        blockInSectAddress = c_uint8()
        blockWrite = (c_uint8 * MAX_BLOCK)()
        pBlockWrite = POINTER(c_uint8)       
        pPKKey   = POINTER(c_ubyte)        
        fnResult = c_uint32()
        
        try:
            
            sBlockInSectAddress = self.ui.txtSectorAddressBWPK.displayText()
            if not sBlockInSectAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,"Warning","You must enter any number !",QtWidgets.QMessageBox.Ok)
                self.ui.txtSectorAddressBWPK.setFocus()
                return
            
            sBlockAddress = self.ui.txtBlockInSAddressBWPK.displayText()
            if not sBlockAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,"Warning","You must enter any number !",QtWidgets.QMessageBox.Ok)
                self.ui.txtBlockInSAddressBWPK.setFocus()
                return
            
            sBlockWrite = self.ui.txtWriteInSDataBWPK.text()
            if sBlockWrite.strip() == '':
                QtWidgets.QMessageBox.warning(self,"Warning","You must enter any value !",QtWidgets.QMessageBox.Ok)
                self.ui.txtWriteInSDataBWPK.setFocus()
                return
            
            blockWrite = str.encode(sBlockWrite)
            pBlockWrite = blockWrite
            blockAddress = int(sBlockAddress)
            blockInSectAddress = int(sBlockInSectAddress)            
            authMode = MIFARE_AUTHENT1A if self.ui.rbAUTH1A.isChecked() else MIFARE_AUTHENT1B
            
            
            pPKKey = self.ReadPKKeys()
            
            fnResult = self.mySO.BlockInSectorWrite_PK(pBlockWrite,blockInSectAddress,blockAddress,authMode,pPKKey)
            
            if fnResult == DL_OK:                                
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_OK,FUNCT_SOUND_OK)
            else:                
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_ERROR,FUNCT_SOUND_ERROR)
         
        finally:
            Functions.FunctionOn = False
    