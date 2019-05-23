import sys
sys.path.append('.\HslCommunication_Python')

from HslCommunication_Python.HslCommunication import SiemensS7Net
from HslCommunication_Python.HslCommunication import SiemensPLCS
from HslCommunication_Python.HslCommunication import SoftBasic

class SiemensTest(object):

    def printReadResult(result, addr):
        if result.IsSuccess:
            print("success[" + addr + "]   " + str(result.Content))
        else:
            print("failed[" + addr + "]   " + result.Message)

    def printWriteResult(result, addr):
        if result.IsSuccess:
            print("success[" + addr + "]")
        else:
            print("falied[" + addr + "]  " + result.Message)

    siemens = SiemensS7Net(SiemensPLCS.S1200, "192.168.9.56")
    if siemens.ConnectServer().IsSuccess == False:
        print("connect falied")
    else:
        i = 1
        while True:

            # int16 read write test
           # siemens.WriteInt16("M500", 10)
          #  siemens.WriteInt16("M502", 20)
           # siemens.WriteInt16("M504", 30)
           # siemens.WriteInt16("M506", 40)

           # printReadResult(siemens.ReadInt16("M500"), "M500")
           # printReadResult(siemens.ReadInt16("M502"), "M502")
            read = siemens.ReadInt16("DB100.20",1000)
            printReadResult(read, "M100")
          #  print(read.Content)

            print(i)
            i=i+1
            """if read.IsSuccess:
                count = siemens.byteTransform.TransInt32(read.Content, 0)
                temp = siemens.byteTransform.TransSingle(read.Content, 4)
                name1 = siemens.byteTransform.TransInt16(read.Content, 8)
                barcode = read.Content[10:20].decode('ascii')
                print(count)
            read = siemens.ReadFromCoreServer(SoftBasic.HexStringToBytes(
                "03 00 00 24 02 F0 80 32 01 00 00 00 01 00 0E 00 05 05 01 12 0A 10 02 00 01 00 00 83 00 03 20 00 04 00 08 3B"))
            if read.IsSuccess:
                # 显示服务器返回的报文
                print(read.Content)
                print()
            else:
                # 读取错误
                print(read.Message)
                """

            siemens.ConnectClose()


            #print(i)
            #i=i+1

def printReadResult(result, addr):
        if result.IsSuccess:
            print("success[" + addr + "]   " + str(result.Content))
        else:
            print("failed[" + addr + "]   " + result.Message)

def printWriteResult(result, addr):
        if result.IsSuccess:
            print("success[" + addr + "]")
        else:
            print("falied[" + addr + "]  " + result.Message)


"""
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
        
        # int16 read write test
        siemens.WriteInt16("M104", -12358)
        printReadResult(siemens.ReadInt16("M104"), "M104")

        # uint16 read write test
        siemens.WriteUInt16("M106", 52358)
        printReadResult(siemens.ReadUInt16("M106"), "M106")

        # int32 read write test
        siemens.WriteInt32("M108", 12345678)
        printReadResult(siemens.ReadInt32("M108"), "M108")

        # int32 read write test
        siemens.WriteInt32("M112", -12345678)
        printReadResult(siemens.ReadInt32("M112"), "M112")

        # uint32 read write test
        siemens.WriteUInt32("M116", 123456789)
        printReadResult(siemens.ReadInt32("M116"), "M116")

        # int64 read write test
        siemens.WriteInt64("M120", 12345678901234)
        printReadResult(siemens.ReadInt64("M120"), "M120")

        # float read write test
        siemens.WriteFloat("M130", 123.456)
        printReadResult(siemens.ReadFloat("M130"), "M130")

        # double read write test
        siemens.WriteDouble("M140", 123.456789)
        printReadResult(siemens.ReadDouble("M140"), "M140")

        # string read write test
        siemens.WriteString("M150", '123456')
        printReadResult(siemens.ReadString("M150",6), "M150")

        # int16 array read write test
        siemens.WriteInt16("M160", [123,456,789,-1234])
        printReadResult(siemens.ReadInt16("M160",4), "M160")

        # read block
        read = siemens.Read("M100",10)
        if read.IsSuccess:
            m100 = read.Content[0]
            m101 = read.Content[1]
            m102 = read.Content[2]
            m103 = read.Content[3]
            m104 = read.Content[4]
            m105 = read.Content[5]
            m106 = read.Content[6]
            m107 = read.Content[7]
            m108 = read.Content[8]
            m109 = read.Content[9]
        else:
            print(read.Message)

        read = siemens.Read("M100",20)
        if read.IsSuccess:
            count = siemens.byteTransform.TransInt32(read.Content,0)
            temp = siemens.byteTransform.TransSingle(read.Content,4)
            name1 = siemens.byteTransform.TransInt16(read.Content,8)
            barcode = read.Content[10:20].decode('ascii')

        read = siemens.ReadFromCoreServer(SoftBasic.HexStringToBytes("03 00 00 24 02 F0 80 32 01 00 00 00 01 00 0E 00 05 05 01 12 0A 10 02 00 01 00 00 83 00 03 20 00 04 00 08 3B"))
        if read.IsSuccess:
            # 显示服务器返回的报文
            print(read.Content)
        else:
            # 读取错误
            print(read.Message)

        siemens.ConnectClose()
"""