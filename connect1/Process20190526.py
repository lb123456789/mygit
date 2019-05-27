
import sys
sys.path.append('.\HslCommunication_Python')

from HslCommunication_Python.HslCommunication import SiemensS7Net
from HslCommunication_Python.HslCommunication import SiemensPLCS
from HslCommunication_Python.HslCommunication import SoftBasic
import os
import  time
from multiprocessing import Pool
from multiprocessing import Process

def printReadResult(result, addr):
    if result.IsSuccess:
    	print("success[" + addr + "]   " + str(result.Content))
    else:
    	print("failed[" + addr + "]   "+result.Message)
def printWriteResult(result, addr):
    if result.IsSuccess:
        print("success[" + addr + "]")
    else:
        print("falied[" + addr + "]  " + result.Message)

if __name__ == "__main__":
    siemens = SiemensS7Net(SiemensPLCS.S1200, "192.168.9.56")
    if siemens.ConnectServer().IsSuccess == False:
        print("connect falied")
    else:
        # bool read write test
        siemens.WriteBool("M580.6",True)
        printReadResult(siemens.ReadBool("M580.6"), "M580.6")

        # byte read write test
        siemens.WriteByte("M900", 58)
        printReadResult(siemens.ReadByte("M500"), "M500")

        # int16 read write test
        siemens.WriteInt16("M500", 12358)
        printReadResult(siemens.ReadInt16("M500"), "M500")