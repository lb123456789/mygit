# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainUione.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1103, 783)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.buttonOpenwindow = QtWidgets.QPushButton(self.centralwidget)
        self.buttonOpenwindow.setGeometry(QtCore.QRect(450, 350, 101, 41))
        self.buttonOpenwindow.setObjectName("buttonOpenwindow")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1103, 26))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menuBar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menuBar)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menuBar)
        self.menu_4.setObjectName("menu_4")
        MainWindow.setMenuBar(self.menuBar)
        self.actionAuto = QtWidgets.QAction(MainWindow)
        self.actionAuto.setObjectName("actionAuto")
        self.actionJOG = QtWidgets.QAction(MainWindow)
        self.actionJOG.setObjectName("actionJOG")
        self.actionsifu = QtWidgets.QAction(MainWindow)
        self.actionsifu.setObjectName("actionsifu")
        self.menu_3.addAction(self.actionsifu)
        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.menu_2.menuAction())
        self.menuBar.addAction(self.menu_3.menuAction())
        self.menuBar.addAction(self.menu_4.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.buttonOpenwindow.setText(_translate("MainWindow", "PushButton"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_2.setTitle(_translate("MainWindow", "编辑"))
        self.menu_3.setTitle(_translate("MainWindow", "设定"))
        self.menu_4.setTitle(_translate("MainWindow", "帮助"))
        self.actionAuto.setText(_translate("MainWindow", "Auto"))
        self.actionJOG.setText(_translate("MainWindow", "JOG"))
        self.actionsifu.setText(_translate("MainWindow", "伺服"))

