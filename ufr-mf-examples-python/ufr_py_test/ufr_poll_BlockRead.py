# -*- coding: utf-8 -*-
from ctypes import *
from platform import *
import os, sys, threading, time, subprocess
import Constants, ErrCodes
last_card = ""
last_time = int(time.time())
#****************************
WIN32_DLL = 'uFCoder-x86.dll'  
ARMHF_SO  = 'libuFCoder-armhf.so'

time.sleep(2)   
#subprocess.call(["sudo", "rmmod", "ftdi_sio", "usbserial"])  # use this on Linux if FTDI not blacklisted
#************************************************************* 
class uFSimplest(threading.Thread):
    """ Main class """
#*************************************************************     
    def __init__(self):
        #super().__init__()
        threading.Thread().__init__()        
        self.initUI()
#************************************************************* 
    def initUI(self):
        if sys.platform.startswith('win32'):   
            self.mySO = windll.LoadLibrary(os.getcwd()+'\\ufr-lib\\windows\\x86\\' + WIN32_DLL) #change x86_64 to x86 for 32 bit library
        elif sys.platform.startswith('linux'):
            self.mySO = cdll.LoadLibrary(os.getcwd() + '\\ufr-lib\\linux\\arm-hf\\' + ARMHF_SO) #'libuFCoder-armhf.so' for RPi  TODO - add appropriate libraries for other OS'es                       
        self.__CONN = False 
        self.__readerOn = False
        self.__functionOn = False        
        self.__dlogicCardType = c_int()  
       
        threading.Thread(target=self.ThreadStart).start()
#*************************************************************         
# property ReaderOn - flags if reader is working
    def __getReaderOn(self):
        return self.__readerOn
    
    def __setReaderOn(self,value):
        self.__readerOn = value
    
    ReaderOn = property( fget = __getReaderOn,fset = __setReaderOn)
#*************************************************************     
# property FunctionOn - flags if some function is currently working  
    def __getFunctionOn(self):
        return self.__functionOn
    
    def __setFunctionOn(self,value):
        self.__functionOn = value
    
    FunctionOn = property(fget = __getFunctionOn,fset = __setFunctionOn)
    
#*************************************************************     
            
    def ThreadStart(self):
        while True:
            # clear console screen
            if sys.platform.startswith('win32'): #on Win
                os.system('cls')
            elif sys.platform.startswith('linux'):#on Linux
                os.system('clear')
            self.Connect()                    
            time.sleep(0.20)
            # pause time between two iterations in polling sequence. Keep it in safe range, reccomended not less than 50 ms, optimal 150-250 ms 
            while self.FunctionOn : pass
            # wait here if function is in progress
            c = input("Press Enter to continue \n or '''x'+<ENTER> to exit...")
            if c=='x' : sys.exit(0)
#*************************************************************
            
    def Connect(self): 
        if  self.FunctionOn: return
               
        cardType = c_uint8()    
        cardUIDSize = c_uint8()
        cardUID = (c_ubyte * 10)() #UID can be up to 10 bytes according to standard
        c =''
        numBlocks = int(0)
        bLen = 0
        blockData =''
        blockHex = ''
        allData =''
        #enclose in try..finally block
        try:            
            self._ReaderOn = True
        
            if self.__CONN != True:
                fResult = self.mySO.ReaderOpen()   #Open Reader
                if fResult == Constants.DL_OK:
                    print('Connected!', hex(fResult),ErrCodes.UFCODER_ERROR_CODES[fResult])  #prompt OK
                    self.__CONN = True         
                else:
                    print('Reader Not connected!',hex(fResult),ErrCodes.UFCODER_ERROR_CODES[fResult]) #prompt Error
                    self.__CONN = False
                    return
        
            if self.__CONN: #1
                fResult = self.mySO.GetDlogicCardType(byref(self.__dlogicCardType)) #first determine CardType from DLogic enumeration
                                                                                    #so we can know card parameters :
                                                                                    #num of bytes, blocks, bytes per block

                if fResult == Constants.DL_OK:  #2
                    print('Card Type =', str(' 0x%02X - %s' % (self.__dlogicCardType.value, Constants.CardName(self.__dlogicCardType.value))))
                    numBlocks = Constants.MaxBlock(self.__dlogicCardType.value)
                    bLen = Constants.BlockLength(self.__dlogicCardType.value)
                    fResult = self.mySO.GetCardIdEx(byref(cardType),cardUID,byref(cardUIDSize)) #read Card UID                  
                    if fResult == Constants.DL_OK:  #3                        
                        for n in range(cardUIDSize.value):                                                           
                            c = c + '%0.2x' % cardUID[n]                                               
                        print('card UID : ' + c)
                        FunctionOn = True               #this will pause thread poling
                        input("\nPress Enter to perform Block Read")
                        FunctionOn = False              #now enable
                        #self.LinearRead()               # Call Linear Read function
                        print('reading...\n')
                        for i in range (0, numBlocks):
                            blockHex = ('%.02x : ' % i)
                            blockData=self.BlockRead(i)
                            for j in range (0, bLen):
                                blockHex = blockHex+'%.02x '%(blockData[j])
                            #print(str(blockHex))  #if we want to print block by block
                            allData = allData + '\n'+blockHex   # or to print all at once
                        print(allData)
                        time.sleep(0.01) # release CPU load
                        
                else:                           #2
                    self.ReaderOn = False
                    return
            else:           #1   Exit because reader is not connected
                self.__CONN = False
                print('self.__CONN= false, will close reader')
                self.mySO.ReaderClose
        finally:
            self.ReaderOn = False                

#*************************************************************
# function to perform audio and visual signals

    def ReaderUISignal(self,lightValue,soundValue):
                    
        uiSignal = self.mySO.ReaderUISignal
        uiSignal.argtypes = (c_uint8,c_uint8)
        uiSignal.restype = c_int
        uiSignal(lightValue,soundValue)
        
#*************************************************************

    def BlockRead(self,block_address):
        import string
        if self.ReaderOn or self.FunctionOn:return
        bLen = 0   #variable to hold length of Block / Page
        try:
            
            self.FunctionOn = True
            bLen = Constants.BlockLength(self.__dlogicCardType.value) #determine number of bytes in Block/Page
            dataValue = (c_uint8 * bLen)()  #reserve space for bLen number bytes
            retData = (c_uint8 * bLen)()    #reserve space for return param        
            fResult = self.mySO.BlockRead((dataValue),block_address,Constants.MIFARE_AUTHENT1A,0) #call BlockRead with address 'block_address',
                                                                                                #use "MIFARE_AUTHENT1A" and
                                                                                                # reader key at index 0, where key is default value = FF FF FF FF FF FF.
                                                                                                #Store everything in 'dataValue'
            if (bLen==16 and (block_address%4)==3):  # if it is Mifare Classic card and actual block is trailer block (block_address MOD 4 == 3)
                for i in range (0,6) :          # change keyA read values with real values (ff), because according to Mifare spec
                                                # keyA can never be read, so we guess : if we get real data, then keyA is the key we passed to authentication
                    dataValue[i]=0xff           # so change first 6 bytes (keyA) with real values
            if fResult == Constants.DL_OK: #if success, return dataValue
                retData = dataValue
            else:                           # else return None
                retData = None    
        finally:
            self.FunctionOn = False 

            return retData

#*************************************************************
        
if __name__ == "__main__":

    uFS = uFSimplest()
    

