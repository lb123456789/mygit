# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         QLabelDemo
# Description:  
# Author:       Administrator
# Date:         2019/5/5
# 文件注解
# -------------------------------------------------------------------------------

import  sys
from PyQt5.QtWidgets import QHBoxLayout,QMainWindow,QApplication,QLabel, QWidget
from PyQt5.QtGui import QPalette

class QLabelDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)