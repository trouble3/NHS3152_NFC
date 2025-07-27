'''
  @author: Vladan S
  @organization: D-Logic
'''

import sys
import os
from Constants import*
from ctypes import *
from uFCoderAdvanced import *

 

def GetFunctionOn():
        return functionOn
     
def SetFunctionOn(value):
        functionOn = value
     
         
def GetReaderOn():     
        return readerOn
     
def SetReaderOn(value):
        readerOn = value
         
FunctionOn = property(fget = GetFunctionOn,fset = SetFunctionOn)    
ReaderOn = property(fget = GetReaderOn,fset = SetReaderOn)

def SetCardType(value):
    dlogicCardType = value
    
def GetCardType():
    return dlogicCardType

CardType = property(fget = GetCardType,fset = SetCardType)




def MaxBytes(cardType):
    if cardType == DL_NTAG_203:
        return MAX_BYTES_NTAG_203
    elif cardType == DL_MIFARE_ULTRALIGHT:
        return MAX_BYTES_ULTRALIGHT
    elif cardType == DL_MIFARE_ULTRALIGHT_C:
        return MAX_BYTES_ULTRALIGHT_C 
    elif cardType == DL_MIFARE_CLASSIC_1K:            
        return  MAX_BYTES_CLASSIC_1K
    elif cardType == DL_MIFARE_CLASSIC_4K:
        return MAX_BYTES_CLASSIC_4k 
    elif cardType == DL_MIFARE_PLUS_S_4K:
        return MAX_BYTES_CLASSIC_4k              
 
   
def MaxBlock(cardType):
    if cardType == DL_MIFARE_ULTRALIGHT: return MAX_BYTES_TOTAL_ULTRALIGHT/4
    elif cardType == DL_MIFARE_ULTRALIGHT_C:return MAX_BYTES_TOTAL_ULTRAL_C/4             
    elif cardType == DL_NTAG_203:return MAX_BYTES_TOTAL_NTAG_203/4               
    elif cardType == DL_MIFARE_CLASSIC_1K:return MAX_SECTORS_1k * 4
    elif cardType == DL_MIFARE_CLASSIC_4K:return (( MAX_SECTORS_1k * 2) * 4) + (( MAX_SECTORS_1k - 8) * 16)            
    elif cardType == DL_MIFARE_PLUS_S_4K:return (( MAX_SECTORS_1k * 2) * 4) + (( MAX_SECTORS_1k - 8) * 16)


def GetPlatform():
        '''         
        '''                    
        if sys.platform.startswith('win32'):
            return windll.LoadLibrary(os.getcwd()+'\\ufr-lib\\windows\\x86\\uFCoder-x86.dll')
        elif sys.platform.startswith('linux'):
            return cdll.LoadLibrary(os.getcwd()+'//ufr-lib//linux//x86_64//libuFCoder-x86_64.so')




def ReaderUISignal(lightValue,soundValue):
        myLib = GetPlatform()
        uiSignal = myLib.ReaderUISignal
        uiSignal.argtypes = (c_uint8,c_uint8)
        uiSignal.restype = c_int
        uiSignal(lightValue,soundValue) 
               

def DecHexCheckBox(txtName,QWidget,state):    
        myLE = QLineEdit()
        nO   = 0
        if state == Qt.Checked:                  
            for le in QWidget.children():
                if isinstance(myLE, QLineEdit) and le.objectName() == txtName + str(nO) :                    
                    le.setText(str('%0.2X' % int(le.text())))  
                    le.setMaxLength(2)                  
                    nO +=1
                    
        if state == Qt.Unchecked:
            for le in QWidget.children():
                if isinstance(myLE, QLineEdit) and le.objectName() == txtName + str(nO) :
                    le.setMaxLength(3)
                    le.setText(str(int(le.text(),16)))                    
                    nO +=1 
            

def ReadKeys(txtName,QWidget,state):        
        le = QLineEdit()
        arKey = (c_uint8 *6)()        
        i  = 0         
        if state == Qt.Checked:       
            for le in QWidget.children():                        
                if isinstance(le,QLineEdit) and le.objectName() == txtName + str(i):                
                    arKey[i] = int(le.text(),16)                                                    
                    i+=1
                
        if state == Qt.Unchecked:
            for le in QWidget.children():                        
                if isinstance(le,QLineEdit) and le.objectName() == txtName + str(i):                
                    arKey[i] = (int(le.text()))                                                         
                    i+=1                                                         
        return arKey        
        
