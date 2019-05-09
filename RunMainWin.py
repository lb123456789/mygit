
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
        self.setWindowTitle("Ui与逻辑分离Demo")

        # 设置按钮btn1状态
        self.btn1 = self.pushButton1
        self.btn1.setText("防护已关闭")
        self.btn1.setCheckable(True)  # 设置已经被点击
        self.btn1.toggle()  # 切换按钮状态
        self.btn1.clicked.connect(self.btnState)
        self.btn1.clicked.connect(lambda: self.wichBtn(self.btn1))

    windowList = []

    def btnState(self):
        if self.btn1.isChecked():
            print("Btn1被单击")
        else:
            print("Btn1未被单击")

    def wichBtn(self, btn):
        the_window = MainCode1()
        self.windowList.append(the_window)
        self.close()
        the_window.show()
        #self.hide()
        i =1
        print(i)
        i = i+1


 #第二个窗口
class MainCode1(QMainWindow,mainUione.Ui_MainWindow):
        def __init__(self):
            QMainWindow.__init__(self)
            mainUione.Ui_MainWindow.__init__(self)
            self.setupUi(self)
            self.setWindowTitle("第二个窗口")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainCode()
    mainWindow.show()
    sys.exit(app.exec_())