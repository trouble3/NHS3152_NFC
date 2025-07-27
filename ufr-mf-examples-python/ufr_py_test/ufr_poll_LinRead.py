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
            self.mySO = windll.LoadLibrary(os.getcwd() + '\\ufr-lib\\windows\\x86\\' + WIN32_DLL) #change x86_64 to x86 for 32 bit library
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
                    fResult = self.mySO.GetCardIdEx(byref(cardType),cardUID,byref(cardUIDSize)) #read Card UID                  
                    if fResult == Constants.DL_OK:  #3                        
                        for n in range(cardUIDSize.value):                                                           
                            c = c + '%0.2x' % cardUID[n]                                               
                        print('card UID : ' + c)
                        FunctionOn = True               #this will pause thread poling
                        input("\nPress Enter to perform Linear Read")
                        FunctionOn = False              #now enable
                        self.LinearRead()               # Call Linear Read function
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
# function to perform Linear Read
# Linear Read function makes data space concatenated, automatically jumps over Trailer Blocks
# In this case LinearRead is used with reader keys (key index=0) and KeyA authentication (MIFARE_AUTHENT1A)
# by default all reader keys are 6xFF

    def LinearRead(self):
        import string
        if self.ReaderOn or self.FunctionOn:return
        asc = ''
        byte = ''
        bLen = 0
        offset = 0
        tmp = 0

        try:
            bLen = Constants.BlockLength(self.__dlogicCardType.value)
            self.FunctionOn = True   
            dataLength =(Constants.MaxBytes(self.__dlogicCardType.value))
            offset =(Constants.LinearOffset(self.__dlogicCardType.value))
            dataValue = (c_uint8 * dataLength)()       
            bytesRet = c_uint16()            
            fResult = self.mySO.LinearRead((dataValue),0,dataLength,byref(bytesRet),Constants.MIFARE_AUTHENT1A,0)                      
      
            if fResult == Constants.DL_OK:
                print('\nPerforming Linear Read function, Linear offset is %d bytes'% offset,' - %d pages/blocks \n' % (offset//bLen))
                for i in range (0 , dataLength) :
                    tmp = dataValue[i]
                    if i%bLen==0 :
                        asc=asc+'\n'+ '%.02x' % (i // bLen) +' : '
                        byte=byte+'\n'+'%.02x' % (i // bLen) +' : '   
                    if (tmp>31 and tmp<127):
                        asc = asc + ('%c' % tmp)
                    else:
                        asc = asc +'.'                       
                    byte = byte + ('%.02x ' % tmp)        
                print('\n','-'*48,'\nASCII content:\n',asc,'\n','-'*48,'\nByte content:\n',byte,'\n')
            else:
                self.ReaderUISignal(Constants.FUNCT_LIGHT_ERROR ,Constants.FUNCT_SOUND_ERROR )        
                print('err result='+hex(fResult))
                print('err msg='+ErrCodes.UFCODER_ERROR_CODES[fResult])
        finally:
            self.FunctionOn = False 
            print('-'*48)
                  
#************************************************************* 
if __name__ == "__main__":

    uFS = uFSimplest()
    

