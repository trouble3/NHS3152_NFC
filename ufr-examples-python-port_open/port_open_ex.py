#from ctypes import c_uint32, c_char_p, c_void_p, c_uint, c_ubyte, windll, byref
import sys
import ErrorCodes

if sys.platform.startswith('win32'):
    uFR = windll.LoadLibrary("ufr-lib//windows//x86//uFCoder-x86.dll")
elif sys.platform.startswith('linux'):
    uFR = cdll.LoadLibrary("ufr-lib//linux//x86_64//libuFCoder-x86_64.so") 

def ReaderOpenEx(reader_type, port_name, port_interface, arg):
    openReader = uFR.ReaderOpenEx
    openReader.argtypes = (c_uint32, c_char_p, c_uint32, c_void_p)
    openReader.restype = c_uint
    b = c_char_p(port_name.encode('utf-8'))
    return openReader(reader_type, b, port_interface, arg)

def ReaderUISignal(light, sound):
    uiSignal = uFR.ReaderUISignal
    uiSignal.argtypes = (c_ubyte, c_ubyte)
    uiSignal.restype = c_uint
    uiSignal(light, sound)
        
if __name__ == '__main__':

    # For opening uFR Nano Online UDP mode use:
    # status = ReaderOpenEx(0, "ip_address:port_number", 85, 0)
    #
    # For opening uFR Nano Online TCP/IP mode use:
    # status = ReaderOpenEx(0, "ip address:port_number", 84, 0)    
    #
    # For opening uFR Nano Online without reset/RTS on ESP32 - transparent mode 115200 use:
    # status = ReaderOpenEx(2, 0, 0, "UNIT_OPEN_RESET_DISABLE")
    
    print("---------------------------------------------")
    print("https://www.d-logic.net/nfc-rfid-reader-sdk/")
    print("---------------------------------------------")
    print("ReaderOpenEx() API tester application version 1.0")
    print("---------------------------------------------")
    
    # uFR online example:
    # status = ReaderOpenEx(0, "192.168.1.101:8881", 85, 0)  
    
    status = ReaderOpenEx(0, "", 0, 0)
    if status == 0:
        print("Status: " + ErrorCodes.UFCODER_ERROR_CODES[status])
        print("Result: Port successfully opened")
        print("---------------------------------------------")
        ReaderUISignal(1, 1)
    elif status != 0:
        print("Status: " + ErrorCodes.UFCODER_ERROR_CODES[status])
        print("Result: Port not opened")
        print("---------------------------------------------")
        
    print("Test finished.")
   
