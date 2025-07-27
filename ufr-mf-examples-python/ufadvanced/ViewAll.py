'''
   @author: Vladan S
   @organization: D-Logic  
   @version: 2.0
'''

import sys
import ctypes
from uFCoderAdvanced import *
import Functions
from  ViewAllForm  import*


from PyQt5.Qt import QTableWidgetItem




class ViewAll(QDialog,Ui_ViewAll):
    """
       main class
    """
    def __init__(self,parent=None):
        super(ViewAll,self).__init__(parent)         
        self.initUI()
        self.mySO = Functions.GetPlatform()         
        self.FillKeyIndex(KEY_INDEX_MAX)            
        self._maxBlock = c_uint()
     
    def initUI(self):
        self.ui = Ui_ViewAll()
        self.ui.setupUi(self)
        
        self.ui.btnReadCard.clicked.connect(self.ReadCard)   
    
    def FillKeyIndex(self,count):
        
        for n in range(0,count):
            self.ui.cboKeyIndex.addItem(str(n))
     
            
    def SetFnStatus(self,fnValue,fnExplain):
        self.ui.lblFnValue.setText(hex(fnValue))
        self.ui.lblFnExplain.setText(fnExplain)        
    
    #==========================================================================================
    
    def DrawNTAGCardType(self):
        if  Functions.FunctionOn == True or Functions.ReaderOn == True:return        
        Functions.FunctionOn = True
        
        pageCounter = c_uint8()
        arPageRead = (c_uint8 * 8)()
        pReadPage = POINTER(c_uint8)
        keyIndex = c_uint8()
        authMode = c_uint8()
        fnResult = c_int32()        
        try:
            self.DrawNTAGGrid()
            keyIndex      = int(self.ui.cboKeyIndex.currentText())
            authMode      = MIFARE_AUTHENT1A  if self.ui.rbAUTH1A.isChecked() else MIFARE_AUTHENT1B
            pReadPage     = arPageRead
            self.ui.pBar.reset()
            self.ui.pBar.setValue(0)
            self.ui.pBar.setMaximum(self._maxBlock)
            self.ui.pBar.setVisible(True)
            
            
            
            for pageCounter in range(4,self._maxBlock):
                fnResult = self.mySO.BlockRead(pReadPage,pageCounter,authMode,keyIndex)
                
                if fnResult == DL_OK:
                    self.ui.pBar.setValue(pageCounter)
                    if self.ui.chkHex.checkState()==Qt.Checked:
                        for i in range(0,4):
                                    self.ui.grdViewAll.setItem(pageCounter - 3,1+i,QTableWidgetItem('$' + str('%0.2X' % int(arPageRead[i]))))
                    else: 
                        for i in range(0,4):
                                    self.ui.grdViewAll.setItem(pageCounter - 3,1+i,QTableWidgetItem(chr(arPageRead[i])))
                
                else :break
                        
            if fnResult == DL_OK:        
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_OK,FUNCT_SOUND_OK)
            else:                
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_ERROR,FUNCT_SOUND_ERROR) 
                         
        finally:
            Functions.FunctionOn = False
            self.ui.pBar.setVisible(False)
    
    def Draw1k4kCardType(self):
        if  Functions.FunctionOn == True or Functions.ReaderOn == True:return        
        Functions.FunctionOn = True
        
        blockCount = c_uint()
        BISCounter = c_uint()
        BISCount = c_uint()
        sectorCounter = c_uint()         
        arBlockRead = (c_uint8 * MAX_BLOCK)()
        pBlockRead = POINTER(c_uint8)            
        keyIndex = c_uint8()
        authMode = c_uint8()
        fnResult = c_int32()
        try:
            BISCounter    = 3
            BISCount      = 0
            blockCount    = 0
            sectorCounter = 0
            keyIndex      = int(self.ui.cboKeyIndex.currentText())
            authMode      = MIFARE_AUTHENT1A  if self.ui.rbAUTH1A.isChecked() else MIFARE_AUTHENT1B
            self.Draw1k4kGrid()
            
            self.ui.pBar.reset()
            self.ui.pBar.setValue(0)
            self.ui.pBar.setMaximum(self._maxBlock)
            self.ui.pBar.setVisible(True)
            pBlockRead = arBlockRead
            
            while blockCount<self._maxBlock:                
                BISCount = 0                
                while BISCount<BISCounter:                     
                    self.ui.grdViewAll.setItem(blockCount,0,QTableWidgetItem(str(sectorCounter)))
                    self.ui.grdViewAll.setItem(blockCount,1,QTableWidgetItem (str(BISCount)))
                    self.ui.grdViewAll.setItem(blockCount,2,QTableWidgetItem (str(blockCount)))
                    
                    fnResult = self.mySO.BlockRead(pBlockRead,blockCount,authMode,keyIndex)
                 
                    if fnResult == DL_OK:
                        if self.ui.chkHex.checkState() == Qt.Checked:                            
                                for i in range(0,16):
                                    self.ui.grdViewAll.setItem(blockCount,3+i,QTableWidgetItem('$' + str('%0.2X' % int(arBlockRead[i]))))
                        else:                           
                            for i in range(0,16):                                
                                self.ui.grdViewAll.setItem(blockCount,3 + i,QTableWidgetItem(chr(arBlockRead[i])))
                    
                    BISCount += 1
                    blockCount += 1
                                       
                blockCount += 1
                self.ui.pBar.setValue(blockCount)
                
                if (sectorCounter >= 31 and blockCount % 16 == 0):                                        
                    for i in range(0,19):
                        item = QtWidgets.QTableWidgetItem(i)
                        item.setBackground(QtGui.QColor(Qt.lightGray))                                            
                        self.ui.grdViewAll.setItem(blockCount-1,i,item)
                        
                    BISCounter = 15
                    sectorCounter += 1                   
                    
                else:
                    
                    for i in range(0,19):
                        item = QtWidgets.QTableWidgetItem(i)
                        item.setBackground(QtGui.QColor(Qt.lightGray))                                            
                        self.ui.grdViewAll.setItem(blockCount-1,i,item)                                                
                    sectorCounter += 1
                    
                    
            if fnResult == DL_OK:        
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_OK,FUNCT_SOUND_OK)
            else:                
                self.SetFnStatus(fnResult,ErrCodes.UFCODER_ERROR_CODES[fnResult])
                Functions.ReaderUISignal(FUNCT_LIGHT_ERROR,FUNCT_SOUND_ERROR)
        finally:
            Functions.FunctionOn = False
            self.ui.pBar.setVisible(False)
    
    
    
    def Draw1k4kGrid(self):
        self.ui.grdViewAll.clear()
        columnCount = 19
        self._maxBlock = int(Functions.MaxBlock(Functions.CardType))
        le = [str(int(i)) for i in range(0,16)]
        self.ui.grdViewAll.setColumnCount(columnCount)
        self.ui.grdViewAll.setHorizontalHeaderLabels(("SCT;BIS;BLO").split(";") + le)
        self.ui.grdViewAll.verticalHeader().setDefaultSectionSize(20)
        self.ui.grdViewAll.verticalHeader().setVisible(False)
        self.ui.grdViewAll.horizontalHeader().setDefaultSectionSize(30)
        self.ui.grdViewAll.horizontalHeader().setVisible(True)
        self.ui.grdViewAll.setRowCount(self._maxBlock)
        
    def DrawNTAGGrid(self):
        self.ui.grdViewAll.clear()
        columnCount = 5
        self._maxBlock = int(Functions.MaxBlock(Functions.CardType))  
        
        self.ui.grdViewAll.setColumnCount(columnCount)
        self.ui.grdViewAll.verticalHeader().setDefaultSectionSize(20)
        self.ui.grdViewAll.verticalHeader().setVisible(False)
        self.ui.grdViewAll.horizontalHeader().setVisible(False)
        self.ui.grdViewAll.setRowCount(self._maxBlock-1)
        
        
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(Qt.gray))
        item.setText("PAGE") 
        self.ui.grdViewAll.setItem(0,0,item)
        self.ui.grdViewAll.setColumnWidth(0,160) 
        
        for i in range(4,self._maxBlock): 
            item = QtWidgets.QTableWidgetItem()
            item.setBackground(QtGui.QColor(Qt.gray))
            item.setText(str(i))     
            self.ui.grdViewAll.setItem(i-3,0,item)
        
        for i in range (1,5):
            item = QtWidgets.QTableWidgetItem()
            item.setBackground(QtGui.QColor(Qt.gray))
            item.setText(str(i))
            self.ui.grdViewAll.setColumnWidth(i,100)
            self.ui.grdViewAll.setItem(0,i,item)
            
        
        
        
           
    
    
    def ReadCard(self):                
        cardType = Functions.CardType             
        if cardType == DL_NTAG_203 or cardType == DL_MIFARE_ULTRALIGHT or cardType == DL_MIFARE_ULTRALIGHT_C:
            self.DrawNTAGCardType()
        elif cardType == DL_MIFARE_CLASSIC_1K or cardType == DL_MIFARE_CLASSIC_4K or cardType == DL_MIFARE_PLUS_S_4K:
            self.Draw1k4kCardType()
            