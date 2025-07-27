'''
   @author: Vladan S
   @organization: D-Logic  
   @version: 2.0
'''

import sys
import re
from uFCoderAdvanced import *
import Functions
from BlockReadWriteForm import *

class BlockRW(QDialog,Ui_subBlockReadWrite):
    """
       main class
    """
    def __init__(self,parent=None):
        super(BlockRW,self).__init__(parent)         
        self.initUI()
        self.mySO = Functions.GetPlatform()             
        self.FillKeyIndex(KEY_INDEX_MAX)            
        self.CreateLineEditForKeys(self.ui.pnlAuth,380,10,"txtPKKey","255",6)
     
    def initUI(self):
        self.ui = Ui_subBlockReadWrite()
        self.ui.setupUi(self)
        
        self.ui.btnBlockRead.clicked.connect(self.BlockRead)
        self.ui.btnBlockReadAKM1.clicked.connect(self.BlockReadAKM1)
        self.ui.btnBlockReadAKM2.clicked.connect(self.BlockReadAKM2)
        self.ui.btnBlockReadPK.clicked.connect(self.BlockReadPK)        
        self.ui.btnBlockWrite.clicked.connect(self.BlockWrite)
        self.ui.btnBlockWriteAKM1.clicked.connect(self.BlockWriteAKM1)
        self.ui.btnBlockWriteAKM2.clicked.connect(self.BlockWriteAKM2)
        self.ui.btnBlockWritePK.clicked.connect(self.BlockWritePK)
        
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
    
    
    
    def BlockRead(self):
        """
         Block Read function
        """
        
        if  Functions.FunctionOn == True or Functions.ReaderOn == True:return        
        Functions.FunctionOn = True
        
        blockAddress = c_uint8()
        keyIndex = c_uint8()
        blockRead = (c_uint8 * MAX_BLOCK)()       
        fnResult = c_int32()
        try:
            sBlockAddress = self.ui.txtBlockAddressBR.displayText()
            if not sBlockAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,"Warning","You must enter any number !",QtWidgets.QMessageBox.Ok)
                self.ui.txtBlockAddressBR.setFocus()
                return
            
            blockAddress = int(sBlockAddress)
            authMode  = MIFARE_AUTHENT1A  if self.ui.rbAUTH1A.isChecked() else MIFARE_AUTHENT1B
            keyIndex = int(self.ui.cboKeyIndex.currentText())            
            
            fnResult = self.mySO.BlockRead(blockRead,blockAddress,authMode,keyIndex)
            if fnResult == DL_OK:
                if self.ui.chkHexBoxBR.checkState() == Qt.Checked:
                    li = [('%0.2x' % i) for i in blockRead]
                    self.ui.txtReadDataBR.setText(''.join(li))
                else:
                    li = [chr(i) for i in blockRead]                                
                    self.ui.txtReadDataBR.setText(''.join(li))
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_OK,FUNCT_SOUND_OK)
            else:                
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_ERROR,FUNCT_SOUND_ERROR) 
        finally:
            Functions.FunctionOn = False
            
    
    
    
    
    def BlockReadAKM1(self):
        """
         Block Read AKM1 function
        """
        if  Functions.FunctionOn == True or Functions.ReaderOn == True:return        
        Functions.FunctionOn = True
        
        blockAddress = c_byte()        
        blockRead = (c_uint8 * MAX_BLOCK)()       
        fnResult = c_int32()
        try:
            sBlockAddress = self.ui.txtBlockAddressBRAKM1.displayText()
            if not sBlockAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,"Warning","You must enter any number !",QtWidgets.QMessageBox.Ok)
                self.ui.txtBlockAddressBRAKM1.setFocus()
                return
            
            blockAddress = int(sBlockAddress)
            authMode  = MIFARE_AUTHENT1A  if self.ui.rbAUTH1A.isChecked() else MIFARE_AUTHENT1B                    
            fnResult = self.mySO.BlockRead_AKM1(blockRead,blockAddress,authMode)
            if fnResult == DL_OK:
                if self.ui.chkHexBoxBRAKM1.checkState() == Qt.Checked:
                    li = [('%0.2x' % i) for i in blockRead]
                    self.ui.txtReadDataBRAKM1.setText(''.join(li))
                else:
                    li = [chr(i) for i in blockRead]                                
                    self.ui.txtReadDataBRAKM1.setText(''.join(li))
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_OK,FUNCT_SOUND_OK)
            else:                
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_ERROR,FUNCT_SOUND_ERROR) 
        finally:
            Functions.FunctionOn = False
            
            
    def BlockReadAKM2(self):        
        """
         Block Read AKM2 function
        """
        if  Functions.FunctionOn == True or Functions.ReaderOn == True:return        
        Functions.FunctionOn = True
        
        blockAddress = c_byte()        
        blockRead = (c_uint8 * MAX_BLOCK)()       
        fnResult = c_int32()
        try:
            sBlockAddress = self.ui.txtBlockAddressBRAKM2.displayText()
            if not sBlockAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,"Warning","You must enter any number !",QtWidgets.QMessageBox.Ok)
                self.ui.txtBlockAddressBRAKM2.setFocus()
                return
            
            blockAddress = int(sBlockAddress)
            authMode  = MIFARE_AUTHENT1A  if self.ui.rbAUTH1A.isChecked() else MIFARE_AUTHENT1B                    
            fnResult = self.mySO.BlockRead_AKM2(blockRead,blockAddress,authMode)
            if fnResult == DL_OK:
                if self.ui.chkHexBoxBRAKM2.checkState() == Qt.Checked:
                    li = [('%0.2x' % i) for i in blockRead]
                    self.ui.txtReadDataBRAKM2.setText(''.join(li))
                else:
                    li = [chr(i) for i in blockRead]                                
                    self.ui.txtReadDataBRAKM2.setText(''.join(li))
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_OK,FUNCT_SOUND_OK)
            else:                
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_ERROR,FUNCT_SOUND_ERROR) 
        finally:
            Functions.FunctionOn = False
            
    
    def BlockReadPK(self):        
        """
         Block Read PK function
        """
        if  Functions.FunctionOn == True or Functions.ReaderOn == True:return        
        Functions.FunctionOn = True
        
        
        pPKKey   = POINTER(c_ubyte)
        blockAddress = c_byte()        
        blockRead = (c_uint8 * MAX_BLOCK)()       
        fnResult = c_int32()
        try:
            sBlockAddress = self.ui.txtBlockAddressBRPK.displayText()
            if not sBlockAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,"Warning","You must enter any number !",QtWidgets.QMessageBox.Ok)
                self.ui.txtBlockAddressBRPK.setFocus()
                return
            
            pPKKey = self.ReadPKKeys()
            
            blockAddress = int(sBlockAddress)
            authMode  = MIFARE_AUTHENT1A  if self.ui.rbAUTH1A.isChecked() else MIFARE_AUTHENT1B                    
            fnResult = self.mySO.BlockRead_PK(blockRead,blockAddress,authMode,pPKKey)
            
            if fnResult == DL_OK:
                if self.ui.chkHexBoxBRPK.checkState() == Qt.Checked:
                    li = [('%0.2x' % i) for i in blockRead]
                    self.ui.txtReadDataBRPK.setText(''.join(li))
                else:
                    li = [chr(i) for i in blockRead]                                
                    self.ui.txtReadDataBRPK.setText(''.join(li))
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_OK,FUNCT_SOUND_OK)
            else:                
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_ERROR,FUNCT_SOUND_ERROR) 
        finally:
            Functions.FunctionOn = False
            
    
        #FFFA31323334FAFBFCFDFEFF
    
    def BlockWrite(self):
        """
          Block Write function
        """
        if  Functions.FunctionOn == True or Functions.ReaderOn == True:return      
        Functions.FunctionOn = True
        
        blockWrite = (c_ubyte * 16)()
        pBlockWrite = POINTER(c_ubyte)
        blockAddress = c_byte()
        keyIndex = c_byte()
        fnResult = c_ulong()
        try:
            sBlockWrite = self.ui.txtWriteDataBW.text()    
                    
            if  sBlockWrite == "":
                QtWidgets.QMessageBox.warning(self,"Warning","You must enter any value !",QtWidgets.QMessageBox.Ok)
                self.ui.txtWriteDataBW.setFocus()
                return
            
            sBlockAddress = self.ui.txtBlockAddressBW.displayText() 
            if not sBlockAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,"Warning","You must enter any number !",QtWidgets.QMessageBox.Ok)
                self.ui.txtBlockAddressBW.setFocus()
                return
            
            if self.ui.chkHexBoxBW.checkState() == Qt.Checked:                               
                x = 0                
                for i in range(len(sBlockWrite)//2):                                      
                    blockWrite[i] =  int(sBlockWrite[x:2+x],16)                  
                    x += 2            
            else:
                blockWrite = str.encode(sBlockWrite)
           
            pBlockWrite = blockWrite
                        
            blockAddress = int(sBlockAddress)
            keyIndex = int(self.ui.cboKeyIndex.currentText())
            authMode  = MIFARE_AUTHENT1A  if self.ui.rbAUTH1A.isChecked() else MIFARE_AUTHENT1B
            
            fnResult = self.mySO.BlockWrite(pBlockWrite,blockAddress,authMode,keyIndex)
            if fnResult == DL_OK:
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_OK,FUNCT_SOUND_OK)
            else:                
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_ERROR,FUNCT_SOUND_ERROR)
        
        except :
            e = sys.exc_info()[0]
            QtWidgets.QMessageBox.warning(self,'Warning ','Must enter appropriate format !\n' + str(e) \
                                          +'\n Length: ' + str(len(sBlockWrite)),QtWidgets.QMessageBox.Ok)       
            
        finally:
            Functions.FunctionOn = False
            
    
    def BlockWriteAKM1(self):
        """
          Block Write AKM1 function
        """
        if  Functions.FunctionOn == True or Functions.ReaderOn == True:return      
        Functions.FunctionOn = True
        
        blockWrite = (c_ubyte * 16)()
        pBlockWrite = POINTER(c_ubyte)
        blockAddress = c_byte()        
        fnResult = c_ulong()
        try:
            sBlockWrite = self.ui.txtWriteDataAKM1.text()    
                    
            if  sBlockWrite == "":
                QtWidgets.QMessageBox.warning(self,"Warning","You must enter any value !",QtWidgets.QMessageBox.Ok)
                self.ui.txtWriteDataAKM1.setFocus()
                return
            
            sBlockAddress = self.ui.txtBlockAddressBWAKM1.displayText() 
            if not sBlockAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,"Warning","You must enter any number !",QtWidgets.QMessageBox.Ok)
                self.ui.txtBlockAddressBWAKM1.setFocus()
                return
            
            if self.ui.chkHexBoxBWAKM1.checkState() == Qt.Checked:                               
                x = 0                
                for i in range(len(sBlockWrite)//2):                                      
                    blockWrite[i] =  int(sBlockWrite[x:2+x],16)                  
                    x += 2            
            else:
                blockWrite = str.encode(sBlockWrite)
           
            pBlockWrite = blockWrite
                        
            blockAddress = int(sBlockAddress)            
            authMode  = MIFARE_AUTHENT1A  if self.ui.rbAUTH1A.isChecked() else MIFARE_AUTHENT1B            
            fnResult = self.mySO.BlockWrite_AKM1(pBlockWrite,blockAddress,authMode)
            
            if fnResult == DL_OK:
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_OK,FUNCT_SOUND_OK)
            else:                
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_ERROR,FUNCT_SOUND_ERROR)
        
        except :
            e = sys.exc_info()[0]
            QtWidgets.QMessageBox.warning(self,'Warning ','Must enter appropriate format !\n' + str(e) \
                                          +'\n Length: ' + str(len(sBlockWrite)),QtWidgets.QMessageBox.Ok)       
            
        finally:
            Functions.FunctionOn = False
            
            
    def BlockWriteAKM2(self):
        """
          Block Write AKM2 function
        """
        if  Functions.FunctionOn == True or Functions.ReaderOn == True:return      
        Functions.FunctionOn = True
        
        blockWrite = (c_ubyte * 16)()
        pBlockWrite = POINTER(c_ubyte)
        blockAddress = c_byte()        
        fnResult = c_ulong()
        try:
            sBlockWrite = self.ui.txtWriteDataAKM2.text()    
                    
            if  sBlockWrite == "":
                QtWidgets.QMessageBox.warning(self,"Warning","You must enter any value !",QtWidgets.QMessageBox.Ok)
                self.ui.txtWriteDataAKM2.setFocus()
                return
            
            sBlockAddress = self.ui.txtBlockAddressBWAKM2.displayText() 
            if not sBlockAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,"Warning","You must enter any number !",QtWidgets.QMessageBox.Ok)
                self.ui.txtBlockAddressBWAKM2.setFocus()
                return
            
            if self.ui.chkHexBoxBWAKM2.checkState() == Qt.Checked:                               
                x = 0                
                for i in range(len(sBlockWrite)//2):                                      
                    blockWrite[i] =  int(sBlockWrite[x:2+x],16)                  
                    x += 2            
            else:
                blockWrite = str.encode(sBlockWrite)
           
            pBlockWrite = blockWrite
                        
            blockAddress = int(sBlockAddress)            
            authMode  = MIFARE_AUTHENT1A  if self.ui.rbAUTH1A.isChecked() else MIFARE_AUTHENT1B
            
            fnResult = self.mySO.BlockWrite_AKM2(pBlockWrite,blockAddress,authMode)
            
            if fnResult == DL_OK:
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_OK,FUNCT_SOUND_OK)
            else:                
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_ERROR,FUNCT_SOUND_ERROR)
        
        except :
            e = sys.exc_info()[0]
            QtWidgets.QMessageBox.warning(self,'Warning ','Must enter appropriate format !\n' + str(e) \
                                          +'\n Length: ' + str(len(sBlockWrite)),QtWidgets.QMessageBox.Ok)       
            
        finally:
            Functions.FunctionOn = False  
            
            
    def BlockWritePK(self):
        """
          Block Write PK function
        """
        if  Functions.FunctionOn == True or Functions.ReaderOn == True:return      
        Functions.FunctionOn = True
        
        blockWrite = (c_ubyte * 16)()
        pBlockWrite = POINTER(c_ubyte)
        pPKKey = POINTER(c_ubyte)
        blockAddress = c_byte()        
        fnResult = c_ulong()
        try:
            sBlockWrite = self.ui.txtWriteDataPK.text()    
                    
            if  sBlockWrite == "":
                QtWidgets.QMessageBox.warning(self,"Warning","You must enter any value !",QtWidgets.QMessageBox.Ok)
                self.ui.txtWriteDataPK.setFocus()
                return
            
            sBlockAddress = self.ui.txtBlockAddressBWPK.displayText() 
            if not sBlockAddress.isnumeric():
                QtWidgets.QMessageBox.warning(self,"Warning","You must enter any number !",QtWidgets.QMessageBox.Ok)
                self.ui.txtBlockAddressBWPK.setFocus()
                return
            
            if self.ui.chkHexBoxBWPK.checkState() == Qt.Checked:                               
                x = 0                
                for i in range(len(sBlockWrite)//2):                                      
                    blockWrite[i] =  int(sBlockWrite[x:2+x],16)                  
                    x += 2            
            else:
                blockWrite = str.encode(sBlockWrite)
           
            pBlockWrite = blockWrite
            pPKKey      = self.ReadPKKeys()                     
            blockAddress = int(sBlockAddress)            
            authMode  = MIFARE_AUTHENT1A  if self.ui.rbAUTH1A.isChecked() else MIFARE_AUTHENT1B
            
            fnResult = self.mySO.BlockWrite_PK(pBlockWrite,blockAddress,authMode,pPKKey)
                        
            if fnResult == DL_OK:
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_OK,FUNCT_SOUND_OK)
            else:                
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_ERROR,FUNCT_SOUND_ERROR)
        
        except :
            e = sys.exc_info()[0]
            QtWidgets.QMessageBox.warning(self,'Warning ','Must enter appropriate format !\n' + str(e) \
                                          +'\n Length: ' + str(len(sBlockWrite)),QtWidgets.QMessageBox.Ok)       
            
        finally:
            Functions.FunctionOn = False      