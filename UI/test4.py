# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         test4
# Description:  
# Author:       Administrator
# Date:         2019/6/8
# 文件注解
#-------------------------------------------------------------------------------
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QMenu
from PyQt5.QtGui import QIcon
import sys
class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.InitUI()
    def InitUI(self):
        self.statusBar().showMessage('准备就绪')

        self.setGeometry(300,300,400,300)
        self.setWindowTitle('早点毕业吧--上下文菜单')

        exitAct = QAction(QIcon('exit.png'), '退出(&E)', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('退出程序')
        exitAct.triggered.connect(qApp.quit)

        saveMenu = QMenu('保存方式(&S)', self)
        saveAct = QAction(QIcon('save.png'),'保存...', self)
        saveAct.setShortcut('Ctrl+S')
        saveAct.setStatusTip('保存文件')
        saveasAct = QAction(QIcon('saveas.png'),'另存为...(&O)', self)
        saveasAct.setStatusTip('文件另存为')
        saveMenu.addAction(saveAct)
        saveMenu.addAction(saveasAct)

        newAct = QAction(QIcon('new.png'),'新建(&N)',self)
        newAct.setShortcut('Ctrl+N')
        newAct.setStatusTip('新建文件')

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('文件(&F)')
        fileMenu.addAction(newAct)
        fileMenu.addMenu(saveMenu)
        fileMenu.addSeparator()
        fileMenu.addAction(exitAct)

        self.show()

    def contextMenuEvent(self, event):
    #要使用上下文菜单，我们必须重新实现contextMenuEvent()方法。
       cmenu = QMenu(self)

       newAct = cmenu.addAction("新建")
       opnAct = cmenu.addAction("保存")
       quitAct = cmenu.addAction("退出")
       action = cmenu.exec_(self.mapToGlobal(event.pos()))#使用exec_()方法显示上下文菜单。 从事件对象获取鼠标指针的坐标。 mapToGlobal()方法将窗口小部件坐标转换为全局屏幕坐标。
       if action == quitAct:
           qApp.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
