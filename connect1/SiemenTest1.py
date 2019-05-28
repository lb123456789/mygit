import sys
sys.path.append('.\HslCommunication_Python')

from HslCommunication_Python.HslCommunication import SiemensS7Net
from HslCommunication_Python.HslCommunication import SiemensPLCS
from HslCommunication_Python.HslCommunication import SoftBasic

siemens = SiemensS7Net(SiemensPLCS.S1200, "127.0.0.1")

if siemens.ConnectServer().IsSuccess == False:
        print("connect falied")

        # int16 read write test
        siemens.WriteInt16("M102", 12358)