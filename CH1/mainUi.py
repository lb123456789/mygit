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
        MainWindow.resize(1056, 736)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(20, 30, 361, 61))
        self.label1.setObjectName("label1")
        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(280, 540, 51, 21))
        self.pushButton1.setObjectName("pushButton1")
        self.pushButton22 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton22.setGeometry(QtCore.QRect(820, 140, 75, 23))
        self.pushButton22.setObjectName("pushButton22")
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(20, 90, 361, 61))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label2.setFont(font)
        self.label2.setMouseTracking(False)
        self.label2.setObjectName("label2")
        self.textEdit1 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit1.setGeometry(QtCore.QRect(610, 240, 421, 191))
        self.textEdit1.setObjectName("textEdit1")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(610, 460, 421, 211))
        self.textEdit.setObjectName("textEdit")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(210, 420, 181, 111))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.lineEdit1 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit1.setObjectName("lineEdit1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit1)
        self.labeltext1 = QtWidgets.QLabel(self.formLayoutWidget)
        self.labeltext1.setObjectName("labeltext1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labeltext1)
        self.lineEdit2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit2.setObjectName("lineEdit2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit2)
        self.lineEdit3 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit3.setObjectName("lineEdit3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit3)
        self.lineEdit4 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit4.setObjectName("lineEdit4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit4)
        self.labeltext2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.labeltext2.setObjectName("labeltext2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labeltext2)
        self.labeltext3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.labeltext3.setObjectName("labeltext3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labeltext3)
        self.labeltext4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.labeltext4.setObjectName("labeltext4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.labeltext4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1056, 23))
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
        self.pushButton1.setText(_translate("MainWindow", "保存"))
        self.pushButton22.setText(_translate("MainWindow", "PushButton"))
        self.label2.setText(_translate("MainWindow", "TextLabel"))
        self.labeltext1.setText(_translate("MainWindow", "姓名"))
        self.labeltext2.setText(_translate("MainWindow", "年龄"))
        self.labeltext3.setText(_translate("MainWindow", "工号"))
        self.labeltext4.setText(_translate("MainWindow", "绩效"))

