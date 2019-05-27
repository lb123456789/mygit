
import sys
sys.path.append('.\HslCommunication_Python')

from HslCommunication_Python.HslCommunication import SiemensS7Net
from HslCommunication_Python.HslCommunication import SiemensPLCS
from HslCommunication_Python.HslCommunication import SoftBasic
import os
import  time
from multiprocessing import Pool
from multiprocessing import Process

"西门子读写类"

def data1(interval):
        siemens = SiemensS7Net(SiemensPLCS.S1200,"192.168.9.56")
        read = siemens.ReadInt16("M100",2)
        print(str(read.Content))
        t_start = time.time()
        time.sleep(interval)  # 程序将会被挂起interval秒
        t_end = time.time()
def data2(interval):
            t_start = time.time()
            time.sleep(interval)  # 程序将会被挂起interval秒
            t_end =	time.time()
            time.sleep(interval)
            i= 1
            print(i)
            i = i+1
if __name__ == "__main__":
        p1 = Process(target=data1, args=(0.01,))
        p2 = Process(target=data2, name="dongGe", args=(0.01,))
        p1.start()
        p2.start()



