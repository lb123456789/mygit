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
        self.label1.setGeometry(QtCore.QRect(30, 210, 361, 61))
        self.label1.setObjectName("label1")
        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(360, 150, 75, 23))
        self.pushButton1.setObjectName("pushButton1")
        self.pushButton22 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton22.setGeometry(QtCore.QRect(820, 140, 75, 23))
        self.pushButton22.setObjectName("pushButton22")
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(30, 280, 361, 61))
        self.label2.setObjectName("label2")
        self.lineEdit1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit1.setGeometry(QtCore.QRect(340, 440, 113, 21))
        self.lineEdit1.setObjectName("lineEdit1")
        self.lineEdit2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit2.setGeometry(QtCore.QRect(340, 480, 113, 21))
        self.lineEdit2.setObjectName("lineEdit2")
        self.lineEdit3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit3.setGeometry(QtCore.QRect(340, 520, 113, 21))
        self.lineEdit3.setObjectName("lineEdit3")
        self.lineEdit4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit4.setGeometry(QtCore.QRect(340, 570, 113, 21))
        self.lineEdit4.setObjectName("lineEdit4")
        self.textEdit1 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit1.setGeometry(QtCore.QRect(610, 220, 421, 191))
        self.textEdit1.setObjectName("textEdit1")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(610, 460, 421, 211))
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1127, 26))
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
        self.pushButton1.setText(_translate("MainWindow", "按钮"))
        self.pushButton22.setText(_translate("MainWindow", "PushButton"))
        self.label2.setText(_translate("MainWindow", "TextLabel"))

