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

class NewProcess(Process,): #继承Process类创建一个新类
    def __init__(self,num,adrss,IP):
        self.num = num
        self.adrss = adrss
        super().__init__()
        self.siemens = SiemensS7Net(SiemensPLCS.S1200,IP)
        self.aa = 1

    def run(self):  #重写Process类中的run方法.
        while True:

            read = self.siemens.ReadInt16(self.adrss,100)
            AA =self.aa
            print(str(read.Content))
            print(self.aa)
            self.aa=self.aa+1
            #print('我是进程%d,我的pid是:%d'%(self.num,os.getpid()))
            time.sleep(0.001)

if __name__ == '__main__':
    #p = NewProcess(1,"Q","192.168.9.57")
    p1 = NewProcess(2,"M100","192.168.9.56")
   # p.start()
    p1.start()






