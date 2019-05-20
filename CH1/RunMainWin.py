
# -*-coding:utf-8-*-#

# -------------------------------------------------------------------------------
# Name:RunMainWin
# Description:
# Author:Administrator
# Date:2019/4/27
# 文件注解
# -------------------------------------------------------------------------------
"""
QLabel控件

setAlignment()：设置文本的对齐方式

setIndent()：设置文本缩进

text()：获取文本内容

setBuddy()：设置伙伴关系

setText()：设置文本内容

selectedText()：返回所选择的字符

setWordWrap()：设置是否允许换行

QLabel常用的信号（事件）：
1.  当鼠标滑过QLabel控件时触发：linkHovered
2.  当鼠标单击QLabel控件时触发：linkActivated

"""




import sys

from PyQt5.QtWidgets import  QPushButton,QVBoxLayout,QWidget,QApplication,QMainWindow,QLineEdit
from PyQt5.QtGui import QIntValidator,QDoubleValidator,QRegExpValidator
from PyQt5.QtCore import QRegExp

# mainUi 来之CH1文件夹
from CH1 import mainUi





# 界面软件逻辑处理 MainCode类又提供了一个容器，这个类继承自QMainWindow,mainUi.Ui_MainWindow，
# 在这个类的构造函数中运行类父类的构造函数， 并且把它自己作为参数产地给setupUi，
class MainCode(QMainWindow,mainUi.Ui_MainWindow):

    # 本类的初始化方法
    def __init__(self):
        super().__init__()
        QMainWindow.__init__(self)
        mainUi.Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("Ui与逻辑分离Demo")

        # 设置按钮btn1状态
        self.btn1 = self.pushButton1
        self.btn1.setText("防护已关闭")
        self.btn1.setCheckable(True)  # 设置已经被点击
        self.btn1.toggle()  # 切换按钮状态
        self.btn1.clicked.connect(self.btnState)
        self.btn1.clicked.connect(lambda: self.wichBtn(self.btn1))

        # 标签文本初始化
        self.lab1 = self.label1
        self.lab2 = self.label2

        # 获取文本lineEdit
        self.LineEdit1 = self.lineEdit1
        self.LineEdit2 = self.lineEdit2
        self.LineEdit3 = self.lineEdit3
        self.LineEdit4 = self.lineEdit4
        # 校验
        self.IntEdit = self.intLineEdit
        self.DoubleEdit = self.doubleLineEdit
        self.ValidatorEdit = self.validatorLineEdit
        print("开始")

        # 未激活使用时候，灰色显示内容
        self.LineEdit1.setPlaceholderText("Normal")
        self.LineEdit2.setPlaceholderText("NoEcho")
        self.LineEdit3.setPlaceholderText("Password")
        self.LineEdit4.setPlaceholderText("PasswordEchoOnEdit")

        # 设置回显示模式
        # 通用
        self.LineEdit1.setEchoMode(QLineEdit.Normal)
        # 看不见
        self.LineEdit2.setEchoMode(QLineEdit.NoEcho)
        # 看见的是密码模式***
        self.LineEdit3.setEchoMode(QLineEdit.Password)
        #  刚开始可以看见，跳转下看到的是****
        self.LineEdit4.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        # 创建校验器[1,99]
        intValidator = QIntValidator(self)
        intValidator.setRange(1,99)

        # 浮点数校验器[360,-360];精度小数点后2位
        doubleValidator = QDoubleValidator(self)
        doubleValidator.setRange(-360,360)
        doubleValidator.setNotation(QDoubleValidator.StandardNotation)
        doubleValidator.setDecimals(2)

        # 字符和数组
        reg = QRegExp("[a-zA-Z0-9]+$")
        validator = QRegExpValidator(self)
        validator.setRegExp(reg)

        # 设置校验器
        self.IntEdit.setValidator(intValidator)
        self.DoubleEdit.setValidator(doubleValidator)
        self.ValidatorEdit.setValidator(validator)


    # 鼠标点击事件处理
    def btnState(self):
        if self.btn1.isChecked():
            print("Btn1被单击")
            self.lab1.setText("你好，按钮被单击了")
            self.btn1.setText("防护已打开")

        else:
            print("Btn1未被单击")
            self.lab1.setText("你好，按钮被单击了1212")
            self.btn1.setText("防护已关闭")

    # 鼠标事件
    def wichBtn(self, btn):
        self.lab2.setText(self.LineEdit1.text())
        print("点击的按钮是：", btn.text())
        print("点击的按钮是：", self.lab2.text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainCode()
    mainWindow.show()

    sys.exit(app.exec_())