
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
import xdrlib ,sys
import xlrd
import re
import xlrd
import xlrd
from PyQt5.QtWidgets import  QPushButton,QVBoxLayout,QWidget,QApplication,QMainWindow,QTableWidgetItem,QTableWidget
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtCore import *

import mainUi



worksheet = xlrd.open_workbook('2018.xlsx')
sheet_names= worksheet.sheet_names()#获取excel中所有工作表名
sheet2 = worksheet.sheet_by_name('2007测试表')#根据Sheet名获取数据
sheet2 = worksheet.sheet_by_index(0)#根据索引获取数据，索引为0开始，1表示获取第二张工作表数据
#获取行数和列数
nrows = sheet2.nrows - 1
ncols = sheet2.ncols
print('行数',nrows)
print('列数',ncols)
rows = sheet2.row_values(1)   #表示获取Sheet2中第2行数据
print('获取Sheet2中第2行数据',rows)

cols10 = sheet2.col_values(2)   #表示获取Sheet2中第3列数据（数据保存为list）
print('获取Sheet2中第3列数据',cols10)

cell=sheet2.cell(0,1)   #表示获取Sheet2中(0,1)单元格的数据（数据保存为list）
print('获取Sheet2中(0,1)单元格的数据',cell)

print (sheet2.name,sheet2.nrows,sheet2.ncols)
#print (sheet2.cell(1,0).value.encode('utf-8'))

print ('ctype=',sheet2.cell(1,0).ctype)

print('获取单元格A1值',sheet2.cell(1,1).value)  #获取单元格A1值，column与row依然可用

for i in range(1,5,1):
        print(sheet2.cell(i,1).value) #更加方便实用
        c=sheet2.cell(i,1).value
        print(c)
        if c.find('22.3'):
            print("没有找到所需要的数")
        else:
            print("找到所需要的数")
            A=sheet2.cell(i,0).value
            print(sheet2.cell(i,0).value)
            B=sheet2.cell(i,1).value
            print(sheet2.cell(i,1).value)
            C=sheet2.cell(i,2).value
            print(sheet2.cell(i,2).value)
            D=sheet2.cell(i,3).value
print(sheet2.cell(i,3).value)
print("HAHAHAHAHAHAHAHAHA")




# 界面软件逻辑处理 MainCode类又提供了一个容器，这个类继承自QMainWindow,mainUi.Ui_MainWindow，
# 在这个类的构造函数中运行类父类的构造函数， 并且把它自己作为参数产地给setupUi，
class MainCode(QMainWindow,mainUi.Ui_MainWindow):






    # 本类的初始化方法
    def __init__(self):
        QMainWindow.__init__(self)
        mainUi.Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("Ui与逻辑分离Demo")

        # 设置按钮btn1状态
        self.btn1 = self.pushButton1
        self.btn1.setText("防护已关闭")
        self.btn1.setCheckable(True)  # 设置已经被点击
        self.btn1.toggle()  # 切换按钮状态
        self.btn1.clicked.connect(self.btnState)
        self.btn1.clicked.connect(lambda: self.wichBtn(self.btn1))

        # 标签文本初始化
        self.lab1 = self.label1
        self.lab2 = self.label2

        # 获取文本lineEdit
        self.LineEdit1 = self.lineEdit1
        print("开始")



    # 鼠标点击事件处理
    def btnState(self):
        if self.btn1.isChecked():
            print("Btn1被单击")
            self.lab1.setText("你好，按钮被单击了")
            self.btn1.setText("防护已打开")

        else:
            print("Btn1未被单击")
            self.lab1.setText("你好，按钮被单击了1212")
            self.btn1.setText("防护已关闭")

    # 鼠标事件
    def wichBtn(self, btn):
        self.lab2.setText(self.LineEdit1.text())
        print("点击的按钮是：", btn.text())
        print("点击的按钮是：", self.lab2.text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainCode()
    mainWindow.show()
    sys.exit(app.exec_())