
# -*-coding:utf-8-*-#

# -------------------------------------------------------------------------------
# Name:RunMainWin
# Description:
# Author:Administrator
# Date:2019/4/27
# 文件注解
# -------------------------------------------------------------------------------


import sys
import MainWin

from PyQt5.QtWidgets import QApplication,QMainWindow
if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 创建对象表示整个应用程序

    mainWindow = QMainWindow()
    # 创建应用程序的主窗口

    ui=MainWin.Ui_MainWindow()
    # 向主窗口添加MainWin里面的控件

    ui.setupUi(mainWindow)
    # setupUi这个是MainWin类里面的一个方法，实现向窗口添加控件。

    mainWindow.show()
    # 显示窗口

    sys.exit(app.exec_())
