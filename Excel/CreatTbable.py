# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         CreatTbable
# Description:
# Author:       Administrator
# Date:         2019/5/7
# 文件注解：创建一个表格，运行后直接弹出
# -------------------------------------------------------------------------------

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class MyTable(QTableWidget):
    def __init__(self,parent=None):
        super(MyTable, self).__init__(parent)
        self.setWindowTitle("我是一个表格")
        self.setWindowIcon(QIcon("male.png"))
        self.resize(920, 240)

        # 设置表格有两行五列。
        self.setColumnCount(5)
        self.setRowCount(3)

        # 设置第一列与第四列宽度为100px
        self.setColumnWidth(0, 100)
        self.setColumnWidth(4, 120)

        # 设置第一行高度为30px。
        self.setRowHeight(0, 30)
        self.table()

    def table(self):
        # 添加表格的文字内容.
        self.setItem(0, 0, QTableWidgetItem(" 你的名字"))
        self.setItem(0, 1, QTableWidgetItem("性别"))
        self.setItem(0, 2, QTableWidgetItem("出生日期"))
        self.setItem(0, 3, QTableWidgetItem("职业"))
        self.setItem(0, 4, QTableWidgetItem("收入"))

        # 设置表头
        self.setHorizontalHeaderLabels(["第一列", "第二列", "第三列", "第四列", "第五列"])
        self.setVerticalHeaderLabels(["第一行", "第二行", "第三行"])

        # 在表中添加一张图片
        lbp = QLabel()
        lbp.setPixmap(QPixmap("Male.png"))
        self.setCellWidget(1, 1, lbp)

        # 添加一个自己设置了大小和类型的文字。
        twi = QTableWidgetItem("新海诚")
        twi.setFont(QFont("Times", 10, ))
        self.setItem(1, 0, twi)

        self.setItem(1, 1, QTableWidgetItem("男"))

        # 添加一个弹出的日期选择，设置默认值为当前日期,显示格式为年月日。
        dte = QDateTimeEdit()
        dte.setDateTime(QDateTime.currentDateTime())
        dte.setDisplayFormat("yyyy/MM/dd")
        dte.setCalendarPopup(True)
        self.setCellWidget(1, 2, dte)
        # 添加了一个下拉选择框
        cbw = QComboBox()
        cbw.addItem("医生")
        cbw.addItem("老师")
        cbw.addItem("律师")
        self.setCellWidget(1, 3, cbw)

        sb = QSpinBox()
        sb.setRange(1000, 10000)
        # 设置最开始显示的数字
        sb.setValue(5000)
        # 这个是显示数字的进制，默认是十进制。
        sb.setDisplayIntegerBase(10)
        # 设置后辍
        sb.setSuffix("元")
        # 设置前辍
        sb.setPrefix("RMB: ")
        sb.setSingleStep(100)
        self.setCellWidget(1, 4, sb)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myTable = MyTable()
    myTable.show()
    app.exit(app.exec_())