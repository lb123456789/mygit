
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
from PyQt5.QtWidgets import  QPushButton,QVBoxLayout,QWidget,QApplication,QMainWindow,QTableWidgetItem,QTableWidget
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtCore import *

from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QLabel
from PyQt5.QtGui import QPalette, QBrush, QPixmap

import mainUi
import mainUione

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



 #第二个窗口
class MainCode1(QMainWindow,mainUione.Ui_MainWindow):

        def __init__(self):
            QMainWindow.__init__(self)
            mainUione.Ui_MainWindow.__init__(self)
            self.setupUi(self)
            self.setWindowTitle("第二个窗口")
            # def一个按钮
            self.bnt2 = self.buttonOpenwindow
            self.bnt2.clicked.connect(self.slot_btn_function)

            # 定义一个指示灯
            self.Lamp = self.lampLabel
            pix = QPixmap('0.png')
            self.Lamp.setPixmap(pix)

        # 定义一个按钮槽
        def slot_btn_function(self):
            pix2 = QPixmap('1.png')
            # self.hide()
            # self.F = MainCode()
            # self.F.show()
            self.Lamp.setPixmap(pix2)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainCode()
    mainWindow.show()
    sys.exit(app.exec_())