
# -*-coding:utf-8-*-#

# -------------------------------------------------------------------------------
# Name:RunMainWin
# Description:
# Author:Administrator
# Date:2019/4/27
# 文件注解
# -------------------------------------------------------------------------------
"""
QLabel控件

setAlignment()：设置文本的对齐方式

setIndent()：设置文本缩进

text()：获取文本内容

setBuddy()：设置伙伴关系

setText()：设置文本内容

selectedText()：返回所选择的字符

setWordWrap()：设置是否允许换行

QLabel常用的信号（事件）：
1.  当鼠标滑过QLabel控件时触发：linkHovered
2.  当鼠标单击QLabel控件时触发：linkActivated

"""


import sys
from PyQt5.QtWidgets import*

from PyQt5.QtGui import*
import pandas as pd
import pymysql


from PyQt5.QtGui import QPalette, QBrush, QPixmap
sys.path.append('.\HslCommunication_Python')

from HslCommunication_Python.HslCommunication import SiemensS7Net
from HslCommunication_Python.HslCommunication import SiemensPLCS
from HslCommunication_Python.HslCommunication import SoftBasic

from CH2 import mainUi
from CH2 import mainUione

from PyQt5.QtSql import  QSqlTableModel
from PyQt5.QtWidgets import QTableView, QApplication
import sys



# 界面软件逻辑处理 MainCode类又提供了一个容器，这个类继承自QMainWindow,mainUi.Ui_MainWindow，
# 在这个类的构造函数中运行类父类的构造函数， 并且把它自己作为参数产地给setupUi，
class MainCode(QMainWindow,mainUi.Ui_MainWindow,):
    # 本类的初始化方法
        def __init__(self):
            QMainWindow.__init__(self)
            mainUi.Ui_MainWindow.__init__(self)
            self.setupUi(self)
            self.setWindowTitle("用户登录")

            # 设置按钮btn1状态
            self.btn1 = self.pushButton1
            self.btn1.clicked.connect(self.slot_btn_function1)

            self .name = self.setNemeEdit1
            self.Password = self.PWDEdit2

        def slot_btn_function1(self):
            self.hide()
            self.Window2 = MainCode1()
            self.Window2.show()

class MainCode1(QMainWindow,mainUione.Ui_MainWindow):

        def __init__(self):
            QMainWindow.__init__(self)
            mainUione.Ui_MainWindow.__init__(self)
            self.setupUi(self)
            self.setWindowTitle("第二个窗口")
            # def一个按钮
            self.bnt2 = self.buttonOpenwindow
            self.bnt2.clicked.connect(self.aa)

            # 定义一个指示灯
            self.Lamp = self.lampLabel1
            pix = QPixmap('0.png')
            self.Lamp.setPixmap(pix)

            # 定义一个按钮读取PLC数据在界面显示
            self.bntRead =self.ButtonRead
            self.bntRead.clicked.connect(lambda:self.ReadIO("M500",1))

            # 整型校验器
            intValidator = QIntValidator(self)

            self.line1 = self.lineEdit1
            self.line2 = self.lineEdit2
            self.line3 = self.lineEdit3

            # 设定line2为整型数据
            self.line2.setValidator(intValidator)

            self.bntWrite = self.ButtonWrite
            self.bntWrite.clicked.connect(lambda: self.WriteIO("M500",self.line2.text()))


            self.table = self.tableView




        # 定义一个按钮槽
        def slot_btn_function(self):
            pix2 = QPixmap('1.png')
            # self.hide()
            # self.F = MainCode()
            # self.F.show()
            self.Lamp.setPixmap(pix2)
        # 读取PLC数据在界面显示
        def ReadIO(self, adds, length):
            siemens = SiemensS7Net(SiemensPLCS.S1200, "192.168.9.56")
            if siemens.ConnectServer().IsSuccess == False:
                print("connect falied")
            else:

                read = siemens.ReadInt16(adds, length)
                print(str(read.Content))
                self.line1.setText(str(read.Content))
                return str(read.Content)
            siemens.ConnectClose()
        def WriteIO(self, adds, value):
            siemens = SiemensS7Net(SiemensPLCS.S1200, "192.168.9.56")
            if siemens.ConnectServer().IsSuccess == False:
                print("connect falied")
            else:
               siemens.WriteInt16(adds,int(value))
               siemens.ConnectClose()


        def aa(self):

            conn = pymysql.connect(host="localhost", port=3306, user="root", passwd="root", db="mysqltest",
                                    charset='utf8')
            cur = conn.cursor()
            hh="select * from"
            YY=" name1"
            cur.execute(hh+YY)
            rows = cur.fetchall()
            row = cur.rowcount  # 取得记录个数，用于设置表格的行数
            vol = len(rows[0])  # 取得字段数，用于设置表格的列数
            cur.close()
            conn.close()
            self.model = QStandardItemModel(row,vol)
            self.model.setHorizontalHeaderLabels(['序号', 'ERP代码', '名称',"规格型号","物料属性","计量单位"])
            # 关联QTableView控件和Model
            self.table.setModel(self.model)

            for i in range(row):
                for j in range(vol):
                    temp_data = rows[i][j]  # 临时记录，不能直接插入表格
                    data = QStandardItem(str(temp_data))  # 转换后可插入表格
                    self.model.setItem(i, j, data)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainCode()
    mainWindow.show()
    sys.exit(app.exec_())