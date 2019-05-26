
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
        siemens = SiemensS7Net(SiemensPLCS.S1200,"127.0.0.1")
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

    while True:
        p1 = Process(target=data1, args=(1,))
        p2 = Process(target=data2, name="dongGe", args=(1,))
        p1.start()
        p2.start()
"""

import multiprocessing
import time

def worker_1(interval):
    print("worker_1")
    time.sleep(interval)
    print("nd worker_1")

def worker_2(interval):
    print ("worker_2")
    time.sleep(interval)
    print("end worker_2")

def worker_3(interval):
    print("worker_3")
    time.sleep(interval)
    print("end worker_3")

if __name__ == "__main__":
    p1 = multiprocessing.Process(target = worker_1, args = (2,))
    p2 = multiprocessing.Process(target = worker_2, args = (3,))
    p3 = multiprocessing.Process(target = worker_3, args = (4,))

    p1.start()
    p2.start()
    p3.start()

    print("The number of CPU is:" + str(multiprocessing.cpu_count()))
    for p in multiprocessing.active_children():
        print("child   p.name:" + p.name + "\tp.id" + str(p.pid))
    print("END!!!!!!!!!!!!!!!!!")

"""



