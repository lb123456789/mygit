# -*-coding:utf-8-*-#

# -------------------------------------------------------------------------------
# Name:RunMainWin
# Description:
# Author:Administrator
# Date:2019/4/27
# 文件注解111
# -------------------------------------------------------------------------------

import  sys
from PyQt5.QtWidgets import QHBoxLayout,QMainWindow,QApplication,QPushButton, QWidget

class QuitApplication (QMainWindow):
    def __init__(self):
        super(QuitApplication, self).__init__()
        self.resize(600,1200)
        self.setWindowTitle("退出应用程序")

        # 添加一个按钮
        self.button1 = QPushButton("退出应用程序")
        # 将信号与槽绑定
        self.button1.clicked.connect(self.onClick_Button)

        layout = QHBoxLayout()
        layout.addWidget(self.button1)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)

        self.setCentralWidget(mainFrame)


    # 自定义的一个方法——鼠标点击槽
    def onClick_Button(self):
        sender = self.sender()
        print(sender.text()+"按钮被按下")
        app = QApplication.instance()

        app.quit()






if __name__ == "__main__":
    # 创建对象表示整个应用程序
    app = QApplication(sys.argv)
    # 创建应用程序的主窗口
    main = QuitApplication()
    main.show()

    #显示窗口
    sys.exit(app.exec_())
