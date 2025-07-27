'''
@author:       Vladan S
@organization: D-Logic
@version:      2.5
'''

from ctypes import *
import os
from platform import *
import sys
import threading
import time 



from PyQt5.QtWidgets import QMainWindow, QAction, QApplication
import webbrowser
import Constants, ErrCodes  
from uFSimplestForm import *



class uFSimplest(QMainWindow,threading.Thread):
    """ Main class """
    
    
    def __init__(self):
        super().__init__()        
        self.initUI()

    def initUI(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.linkLabel.setMouseTracking(1)
        
        if sys.platform.startswith('win32'):              
            self.mySO = windll.LoadLibrary(os.getcwd() + '\\ufr-lib\\windows\\x86\\uFCoder-x86.dll')      
        elif sys.platform.startswith('linux'):
            self.mySO = cdll.LoadLibrary(os.getcwd()+'//ufr-lib//linux//x86_64//libuFCoder-x86_64.so') 
        
                                    
        self.__CONN = False 
        self.__readerOn = False
        self.__functionOn = False        
        self.__dlogicCardType = c_int()  
        
                    
       
        self.ui.btnLinearRead.clicked.connect(self.LinearRead)
        self.ui.btnLinearWrite.clicked.connect(self.LinearWrite)
        self.ui.btnFormatCard.clicked.connect(self.FormatCard)
        self.ui.linkLabel.mousePressEvent = self.OpenURL
         
        
         
        t = threading.Thread(target=self.ThreadStart)
        t.daemon = True
        t.start()
                        
   
    def __getReaderOn(self):
        return self.__readerOn
    
    def __setReaderOn(self,value):
        self.__readerOn = value
    
    
    
    def __getFunctionOn(self):
        return self.__functionOn
    
    def __setFunctionOn(self,value):
        self.__functionOn = value
    
    FunctionOn = property(fget = __getFunctionOn,fset = __setFunctionOn)
    ReaderOn = property(fget = __getReaderOn,fset = __setReaderOn)
    
    def OpenURL(self,event):        
        webbrowser.open(self.ui.linkLabel.text())
    
    def closeEvent(self,event):
        reply = QtWidgets.QMessageBox.question(self,'Message',"Are you sure you want to quit?",QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if(reply == QtWidgets.QMessageBox.Yes):
            event.accept()
            sys.exit(0)
        else:
            event.ignore()
    
    
    
            
    def ThreadStart(self):
        while True:                                              
            self.Connect()                    
            time.sleep(Constants.TIME_SLEEP)   
    
    def Connect(self): 
        if  self.FunctionOn  : return
               
        readerType = c_int32() 
        cardType = c_uint8()
        cardUIDSize = c_uint8()
        cardUID = (c_ubyte * 9)() 
        c = str()            
        try:            
            self._ReaderOn = True
        
            if self.__CONN != True:
                fResult = self.mySO.ReaderOpen() 
                if fResult == Constants.DL_OK:                                
                    self.ui.txtConnected.setText('CONNECTED')
                    self.ui.txtConnErrorValue.setText(hex(fResult))
                    self.ui.txtConnErrorMsg.setText(ErrCodes.UFCODER_ERROR_CODES[fResult]) 
                    self.__CONN = True         
                else: 
                    self.ui.txtConnected.setText('NOT CONNECTED')
                    self.ui.txtConnErrorValue.setText(hex(fResult))
                    self.ui.txtConnErrorMsg.setText(ErrCodes.UFCODER_ERROR_CODES[fResult])
                    self.ui.txtCardType.setText(None)
                    self.ui.txtCardUID.setText(None)
                    self.ui.txtUIDSize.setText(None)
                    self.__CONN = False
        
            if self.__CONN:            
                fResult = self.mySO.GetReaderType(byref(readerType))
                if fResult == Constants.DL_OK:
                    fResult = self.mySO.GetDlogicCardType(byref(self.__dlogicCardType))
                    if fResult == Constants.DL_OK:
                                            
                        fResult = self.mySO.GetCardIdEx(byref(cardType),cardUID,byref(cardUIDSize))                    
                        if fResult == Constants.DL_OK:                                                                                                                                                    
                            for n in range(cardUIDSize.value):                                                           
                                c +=  '%0.2x' % cardUID[n]
                                                                     
                            cardType = hex(self.__dlogicCardType.value)
                            uidSize  = hex(cardUIDSize.value) 
                                                                       
                            self.ui.txtCardUID.setText('0x'+ c.upper())                                                    
                            self.ui.txtCardType.setText(cardType.upper())
                            self.ui.txtUIDSize.setText(uidSize.upper())
                            self.ui.txtCardErrorValue.setText(hex(fResult))
                            self.ui.txtCardErrorMsg.setText(ErrCodes.UFCODER_ERROR_CODES[fResult])
                    else:
                        self.ui.txtCardUID.setText(None)
                        self.ui.txtCardType.setText(None)
                        self.ui.txtUIDSize.setText(None)
                        self.ui.txtCardErrorValue.setText(None)
                        self.ui.txtCardErrorMsg.setText(None)
            else:
                self.__CONN = False
                self.mySO.ReaderClose
        finally:
            self.ReaderOn = False                
    
                                                                                                        
    def ReaderUISignal(self,lightValue,soundValue):
                    
        uiSignal = self.mySO.ReaderUISignal
        uiSignal.argtypes = (c_uint8,c_uint8)
        uiSignal.restype = c_int
        uiSignal(lightValue,soundValue)

    
    def LinearRead(self):  
        if self.ReaderOn  or self.FunctionOn :return          
        try:
            self.FunctionOn = True   
#            dataLength =(Constants.MaxBytes(self.__dlogicCardType.value))
            dataLength =(Constants.MaxBytes(self.__dlogicCardType.value))
            byRet = c_uint16()
            print(dataLength)
            dataValue = (c_uint32 * Constants.MAX_BYTES_ULTRALIGHT_C)()
#            dataValue = (c_uint8 * dataLength)()
            #byRet = c_uint16()
            for i in range(100):
                
                fResult = self.mySO.LinearRead((dataValue),16,2,byref(byRet),Constants.MIFARE_AUTHENT1A,0)
                s1 = c_uint16()
                s1 = ((dataValue[0] << 8) & 0xFF00) + (dataValue[1] & 0x00FF)
                # fResult = self.mySO.LinearRead((dataValue),16,2,byref(byRet),Constants.MIFARE_AUTHENT1A,0)

                # s2 = ((dataValue[0] << 8) & 0x0000FF00) + (dataValue[1] & 0x000000FF)
                # fResult = self.mySO.LinearRead((dataValue),16,2,byref(byRet),Constants.MIFARE_AUTHENT1A,0)
                # s3 = ((dataValue[0] << 8) & 0x0000FF00) + (dataValue[1] & 0x000000FF)
                # s = (s1 + s2 + s3)/3
                print(s1)


#			fResult = self.mySO.LinearRead((dataValue),23,dataLength,byref(byRet),Constants.MIFARE_AUTHENT1A,0)
#            lista = list(dataValue)
            if fResult == Constants.DL_OK:  
                print("OK\n")  
                print(dataValue[0])                    
                # li = [chr(i) for i in dataValue]                                                
                # self.ui.txtLinearRead.setText(''.join(li))                   
                # self.ReaderUISignal(Constants.FUNCT_LIGHT_OK ,Constants.FUNCT_SOUND_OK)
                # self.ui.txtFuncErrorValue.setText(hex(fResult))
                # self.ui.txtFunctErrorMsg.setText(ErrCodes.UFCODER_ERROR_CODES[fResult])
            else:
                print("fail\n")  
                self.ReaderUISignal(Constants.FUNCT_LIGHT_ERROR ,Constants.FUNCT_SOUND_ERROR )        
                self.ui.txtFuncErrorValue.setText(hex(fResult))
                self.ui.txtFunctErrorMsg.setText(ErrCodes.UFCODER_ERROR_CODES[fResult])
        finally:
            self.FunctionOn = False 
            
                  
            
    
    def LinearWrite(self):
        """  - LINEAR WRITE - function """
        
        if self.ReaderOn == True or self.FunctionOn == True:return
                    
        try:
            self.FunctionOn = True            
            dataValueToWrite = self.ui.txtLinearWrite.toPlainText()
            if not dataValueToWrite.strip():
                QtGui.QMessageBox.information(self,'Information','You must enter any value !',QtGui.QMessageBox.Ok)
                self.ui.txtLinearWrite.setFocus()                                                
                return                        
            
            dataValueToBytes = str.encode(dataValueToWrite)
            dataLength = len(dataValueToWrite)
            byRet = c_uint16()
         
            fResult = self.mySO.LinearWrite(dataValueToBytes,0,dataLength,byref(byRet),Constants.MIFARE_AUTHENT1A,0)              
            if fResult == Constants.DL_OK:
                self.ReaderUISignal(Constants.FUNCT_LIGHT_OK ,Constants.FUNCT_SOUND_OK)
                self.ui.txtFuncErrorValue.setText(hex(fResult))
                self.ui.txtFunctErrorMsg.setText(ErrCodes.UFCODER_ERROR_CODES[fResult]) 
            else:
                self.ReaderUISignal(Constants.FUNCT_LIGHT_ERROR ,Constants.FUNCT_SOUND_ERROR )        
                self.ui.txtFuncErrorValue.setText(hex(fResult))
                self.ui.txtFunctErrorMsg.setText(ErrCodes.UFCODER_ERROR_CODES[fResult])   
            
        finally:
            self.FunctionOn = False

            
    def FormatCard(self):
        """ - FORMAT CARD -  function """ 

        if self.ReaderOn  or self.FunctionOn :return
        try:
            self.FunctionOn = True
           
            blockCount = 0
            keyIndex = 0
            BISCount = 0
            BISCounter = 3
            sectorCounter = 0
            fResult = 0
            
            pData = POINTER(c_uint8)
            blockData = (c_uint8 * Constants.MAX_BLOCK)()
            cardType = self.__dlogicCardType.value
            maxBlock = Constants.MaxBlock(cardType)                                 
           
            self.ui.pBar.reset()
            self.ui.pBar.setMaximum(maxBlock)
            self.ui.pBar.setVisible(True)
            
            memset(blockData,Constants.FORMAT_SIGN,Constants.MAX_BLOCK)
            pData = byref(blockData)
            
            if cardType == Constants.DL_MIFARE_ULTRALIGHT or cardType == Constants.DL_MIFARE_ULTRALIGHT_C or \
                cardType == Constants.DL_NTAG_203:                
                while blockCount<maxBlock:
                    self.ui.pBar.setValue(blockCount)
                    fResult = self.mySO.BlockWrite(pData,blockCount,Constants.MIFARE_AUTHENT1A,keyIndex)
                    blockCount += 1                   
                    #if fResult != 0:break
                        
            else:
                if cardType == Constants.DL_MIFARE_CLASSIC_1K or cardType == Constants.DL_MIFARE_CLASSIC_4K \
                    or cardType == Constants.DL_MIFARE_PLUS_S_4K:
                    while blockCount<maxBlock:
                        BISCount = 0                                                                       
                        while BISCount<BISCounter:                            
                            fResult = self.mySO.BlockWrite(pData,blockCount,Constants.MIFARE_AUTHENT1A,keyIndex)
                            #if fResult != 0:break
                            BISCount += 1
                            blockCount += 1  
                            self.ui.pBar.setValue(blockCount)                                              
                    
                    blockCount +=1                                                                
                    if (sectorCounter >=31 and blockCount % 16 == 0):
                        sectorCounter+=1
                        BISCounter = 15
                    else:
                        sectorCounter+=1
                                                                                        
            if fResult == Constants.DL_OK:                
                self.ReaderUISignal(Constants.FUNCT_LIGHT_OK ,Constants.FUNCT_SOUND_OK)
                self.ui.txtFuncErrorValue.setText(hex(fResult))
                self.ui.txtFunctErrorMsg.setText(ErrCodes.UFCODER_ERROR_CODES[fResult]) 
            else:
                self.ReaderUISignal(Constants.FUNCT_LIGHT_ERROR ,Constants.FUNCT_SOUND_ERROR )        
                self.ui.txtFuncErrorValue.setText(hex(fResult))
                self.ui.txtFunctErrorMsg.setText(ErrCodes.UFCODER_ERROR_CODES[fResult])                                     
        finally:
            self.FunctionOn = False
            self.ui.pBar.setVisible(False)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    uFS = uFSimplest()
    uFS.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
    uFS.show()    
    sys.exit(app.exec_())
    
            
            
            
