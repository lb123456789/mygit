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
        MainWindow.resize(484, 373)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(60, 140, 351, 141))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.labeltext1 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.labeltext1.setFont(font)
        self.labeltext1.setObjectName("labeltext1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labeltext1)
        self.lineEdit1 = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit1.setFont(font)
        self.lineEdit1.setObjectName("lineEdit1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit1)
        self.labeltext2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.labeltext2.setFont(font)
        self.labeltext2.setObjectName("labeltext2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labeltext2)
        self.lineEdit2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit2.setFont(font)
        self.lineEdit2.setObjectName("lineEdit2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit2)
        self.pushButton1 = QtWidgets.QPushButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton1.setFont(font)
        self.pushButton1.setObjectName("pushButton1")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.pushButton1)
        self.labeltext4_2 = QtWidgets.QLabel(self.centralwidget)
        self.labeltext4_2.setGeometry(QtCore.QRect(120, 30, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.labeltext4_2.setFont(font)
        self.labeltext4_2.setObjectName("labeltext4_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 484, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labeltext1.setText(_translate("MainWindow", "用户名"))
        self.labeltext2.setText(_translate("MainWindow", "密 码"))
        self.pushButton1.setText(_translate("MainWindow", "保存"))
        self.labeltext4_2.setText(_translate("MainWindow", "齿轮加工制造生产线"))

