####初始化登录信息
import sys
from PyQt5.QtWidgets import  QPushButton,QVBoxLayout,QWidget,QApplication,QMainWindow,QTableWidgetItem,QTableWidget
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtCore import *


# 保存登录信息
def save_login_info(self):
    settings = QSettings("config.ini", QSettings.IniFormat)  # 方法1：使用配置文件
    # settings = QSettings("mysoft","myapp")                        #方法2：使用注册表
    settings.setValue("account", self.lineEdit_account.text())
    settings.setValue("password", self.lineEdit_password.text())
    settings.setValue("remeberpassword", self.checkBox_remeberpassword.isChecked())
    settings.setValue("autologin", self.checkBox_autologin.isChecked())
   # 保存登录信息
    def save_login_info(self):
        settings = QSettings("config.ini", QSettings.IniFormat)        #方法1：使用配置文件
        #settings = QSettings("mysoft","myapp")                        #方法2：使用注册表
        settings.setValue("account",self.lineEdit_account.text())
        settings.setValue("password", self.lineEdit_password.text())
        settings.setValue("remeberpassword", self.checkBox_remeberpassword.isChecked())
        settings.setValue("autologin", self.checkBox_autologin.isChecked())


if __name__ == "__main__":

    self.init_login_info()