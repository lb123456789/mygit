
# -*-coding:utf-8-*-#

# -------------------------------------------------------------------------------
# Name:RunMainWin
# Description:
# Author:Administrator
# Date:2019/4/27
# 文件注解
# -------------------------------------------------------------------------------


import sys
from PyQt5.QtWidgets import  QPushButton,QVBoxLayout,QWidget,QApplication,QMainWindow
from PyQt5.QtGui import QIcon,QPixmap

import mainUi

# 界面软件逻辑处理 MainCode类又提供了一个容器，这个类继承自QMainWindow,mainUi.Ui_MainWindow，
# 在这个类的构造函数中运行类父类的构造函数， 并且把它自己作为参数产地给setupUi，
class MainCode(QMainWindow,mainUi.Ui_MainWindow):

    # 本类的初始化方法
    def __init__(self):
        QMainWindow.__init__(self)
        mainUi.Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("Ui与逻辑分离Demo")

        self.btn_1 = self.pushButton1
        self.btn_1.setText("修改的按钮")

        self.btn_1.setCheckable(True)  # 设置已经被点击

        self.btn_1.toggle()  # 切换按钮状态

        self.btn_1.clicked.connect(self.btnState)

        self.btn_1.clicked.connect(lambda: self.wichBtn(self.btn_1))
        print("开始")


    # 鼠标点击事件处理
    def btnState(self):

        if self.btn_1.isChecked():
            print("Btn_1被单击")

        else:
            print("Btn_1未被单击")
    # 鼠标事件
    def wichBtn(self, btn):
        print("点击的按钮是：", btn.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainCode()
    mainWindow.show()
    sys.exit(app.exec_())