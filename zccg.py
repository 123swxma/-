from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QPoint, pyqtSignal, QObject
from PyQt5.QtWidgets import QMainWindow

class xinhao(QObject):
    xinhao = pyqtSignal()

    def fasheng(self):
        xinhao.emit()



class Ui_Form_3(QMainWindow):

    def setupUi(self, Form):
        self.xinhoa = xinhao()
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 400, 300))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 0, 400, 300))
        self.label.setStyleSheet("border-image: url(:/beijing/regs/bj1.png);\n"
"border-top-left-radius :10px;\n"
"border-bottom-left-radius :10px;\n"
"border-top-right-radius :10px;\n"
"border-bottom-right-radius :10px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(110, 20, 181, 91))
        self.label_2.setStyleSheet("font: 20pt \"微软雅黑\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(120, 90, 151, 101))
        self.label_3.setStyleSheet("border-image: url(:/zh/sc/zh.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(110, 220, 161, 41))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    border-radius:10px;\n"
"    background-color: rgba(255, 255, 255, 190);\n"
"    \n"
"    font: 10pt \"微软雅黑\";\n"
"    \n"
"}\n"
"QPushButton:hover{\n"
                                      "background-color: rgba(255, 255, 255, 190);\n")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "  注册成功"))
        self.pushButton.setText(_translate("Form", "确定"))

        self.pushButton.clicked.connect(self.denglu)