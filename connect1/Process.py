import os
import time
from multiprocessing import Pool
from multiprocessing import Process

class NewProcess(Process): #继承Process类创建一个新类
    def __init__(self,num):
        self.num = num
        super().__init__()

    def run(self):  #重写Process类中的run方法.
        while True:
            print('我是进程%d,我的pid是:%d'%(self.num,os.getpid()))
            time.sleep(0.001)
if __name__ == '__main__':

    for i in range(2):
        p = NewProcess(i)
        p.start()
        #p.join()