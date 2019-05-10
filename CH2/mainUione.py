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
        MainWindow.resize(1003, 783)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lampLabel = QtWidgets.QLabel(self.centralwidget)
        self.lampLabel.setGeometry(QtCore.QRect(320, 250, 91, 91))
        self.lampLabel.setObjectName("lampLabel")
        self.lampLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.lampLabel_2.setGeometry(QtCore.QRect(320, 460, 91, 91))
        self.lampLabel_2.setObjectName("lampLabel_2")
        self.buttonOpenwindow = QtWidgets.QPushButton(self.centralwidget)
        self.buttonOpenwindow.setGeometry(QtCore.QRect(210, 180, 93, 28))
        self.buttonOpenwindow.setObjectName("buttonOpenwindow")
        self.lampCloesButton = QtWidgets.QPushButton(self.centralwidget)
        self.lampCloesButton.setGeometry(QtCore.QRect(150, 240, 93, 28))
        self.lampCloesButton.setObjectName("lampCloesButton")
        self.lampOpenButton = QtWidgets.QPushButton(self.centralwidget)
        self.lampOpenButton.setGeometry(QtCore.QRect(280, 240, 93, 28))
        self.lampOpenButton.setObjectName("lampOpenButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1003, 26))
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
        self.actionzhuxiao = QtWidgets.QAction(MainWindow)
        self.actionzhuxiao.setObjectName("actionzhuxiao")
        self.actiontuichu = QtWidgets.QAction(MainWindow)
        self.actiontuichu.setObjectName("actiontuichu")
        self.menu.addAction(self.actionzhuxiao)
        self.menu.addAction(self.actiontuichu)
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
        self.lampLabel.setText(_translate("MainWindow", "TextLabel"))
        self.lampLabel_2.setText(_translate("MainWindow", "TextLabel"))
        self.buttonOpenwindow.setText(_translate("MainWindow", "PushButton"))
        self.lampCloesButton.setText(_translate("MainWindow", "灯开"))
        self.lampOpenButton.setText(_translate("MainWindow", "灯关"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_2.setTitle(_translate("MainWindow", "编辑"))
        self.menu_3.setTitle(_translate("MainWindow", "设定"))
        self.menu_4.setTitle(_translate("MainWindow", "帮助"))
        self.actionAuto.setText(_translate("MainWindow", "Auto"))
        self.actionJOG.setText(_translate("MainWindow", "JOG"))
        self.actionsifu.setText(_translate("MainWindow", "伺服"))
        self.actionzhuxiao.setText(_translate("MainWindow", "注销 "))
        self.actiontuichu.setText(_translate("MainWindow", "退出"))

