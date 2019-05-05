# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainUi.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1127, 736)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(440, 450, 54, 12))
        self.label1.setObjectName("label1")
        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(440, 230, 75, 23))
        self.pushButton1.setObjectName("pushButton1")
        self.pushButton22 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton22.setGeometry(QtCore.QRect(790, 310, 75, 23))
        self.pushButton22.setObjectName("pushButton22")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1127, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton22.toggled['bool'].connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label1.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton1.setText(_translate("MainWindow", "PushButton"))
        self.pushButton22.setText(_translate("MainWindow", "PushButton"))

