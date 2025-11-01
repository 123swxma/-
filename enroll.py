import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRegExp, pyqtSignal, QPropertyAnimation, QRect, QParallelAnimationGroup, QThread, QPoint, Qt, \
    QObject
from PyQt5.QtGui import QIntValidator, QRegExpValidator, QMouseEvent
from PyQt5 import QtCore, QtGui, QtWidgets
from func import *
import json, re


from zccg import Ui_Form_3
from PyQt5.QtWidgets import QLineEdit, QMainWindow


class xiangyin(QObject):
    xingyin = pyqtSignal()

    def chaohanshu(self):
        self.xingyin.emit()


class HoverLineEdit(QLineEdit):
    hover_started = pyqtSignal()
    hover_ended = pyqtSignal()
    xuanzhong = pyqtSignal()
    notxuanzhong = pyqtSignal()

    def enterEvent(self, event):
        super().enterEvent(event)
        self.hover_started.emit()

    def leaveEvent(self, event):
        super().leaveEvent(event)
        self.hover_ended.emit()

    def focusInEvent(self, event):
        super().focusInEvent(event)  # 调用基类的 focusInEvent 方法
        self.xuanzhong.emit()  # 发射自定义信号

    def focusOutEvent(self, event):
        super().focusOutEvent(event)  # 调用基类的 focusOutEvent 方法
        self.notxuanzhong.emit()  # 发射自定义信号


class Ui_Form_2(QMainWindow):
    def setupUi(self, Form):
        self.shtow = xiangyin()
        Form.setObjectName("Form")
        Form.resize(614, 956)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(80, 40, 450, 830))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                 "border-top-left-radius :45px;\n"
                                 "border-bottom-left-radius :45px;\n"
                                 "border-top-right-radius :45px;\n"
                                 "border-bottom-right-radius :45px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 0, 450, 830))
        self.label.setStyleSheet("border-image: url(:/beijing/regs/bj1.png);\n"
                                 "border-top-left-radius :45px;\n"
                                 "border-bottom-left-radius :45px;\n"
                                 "border-top-right-radius :45px;\n"
                                 "border-bottom-right-radius :45px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setGeometry(QtCore.QRect(210, 10, 217, 52))
        self.frame_4.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_3.setStyleSheet("\n"
                                        "QPushButton{\n"
                                        "    border:none;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "    padding-bottom:5px;\n"
                                        "}")
        self.pushButton_3.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/zuixiaohua /regs/减.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_5.setStyleSheet("\n"
                                        "QPushButton{\n"
                                        "    border:none;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "    padding-bottom:5px;\n"
                                        "}")
        self.pushButton_5.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/guanbi/regs/cha.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon1)
        self.pushButton_5.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(140, 580, 171, 41))
        font = QtGui.QFont()
        font.setStrikeOut(False)
        font.setKerning(False)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton{\n"
                                      "    border-radius:10px;\n"
                                      "    background-color: rgba(255, 255, 255, 180);\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover\n"
                                      "{\n"
                                      "    background-color:rgb(234,244,252);\n"
                                      "    border:1px solid rgb(44,169,225);\n"
                                      "}\n"
                                      "QPushButton:pressed\n"
                                      "{\n"
                                      "    border:1px solid rgb(44,169,225);\n"
                                      "    background-color:rgb(235,246,247);   \n"
                                      "    padding-left:2px; \n"
                                      "    padding-top:2px;\n"
                                      "    font-weight:bold;\n"
                                      "    color: rgb(0, 79, 115);\n"
                                      "}\n"
                                      "\n"
                                      "\n"
                                      "")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit2 = HoverLineEdit(self.frame)
        self.lineEdit2.setGeometry(QtCore.QRect(40, 240, 370, 50))
        self.lineEdit2.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lineEdit2.setStyleSheet("QLineEdit{\n"
                                     "border-radius:10px;\n"
                                     "background-color: rgba(255, 255, 255, 180);\n"
                                     "border: 0px solid black;\n"
                                     "}")
        self.lineEdit2.setObjectName("lineEdit2")
        self.lineEdit3 = HoverLineEdit(self.frame)
        self.lineEdit3.setGeometry(QtCore.QRect(40, 330, 370, 50))
        self.lineEdit3.setStyleSheet("QLineEdit{\n"
                                     "border-radius:10px;\n"
                                     "background-color: rgba(255, 255, 255, 180);\n"
                                     "border: 0px solid black;\n"
                                     "}\n"
                                     "\n"
                                     "\n"
                                     "")
        self.lineEdit3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit3.setObjectName("lineEdit3")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(40, 300, 371, 21))
        self.label_3.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                   "color: rgb(255, 0, 4);\n"
                                   "font: 10pt \"Agency FB\";")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.lineEdit = HoverLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(40, 150, 370, 50))
        self.lineEdit.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lineEdit.setStyleSheet("QLineEdit{\n"
                                    "border-radius:10px;\n"
                                    "background-color: rgba(255, 255, 255, 180);\n"
                                    "border: 0px solid black;\n"
                                    "}")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit4 = HoverLineEdit(self.frame)
        self.lineEdit4.setGeometry(QtCore.QRect(40, 420, 370, 50))
        self.lineEdit4.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lineEdit4.setStyleSheet("QLineEdit{\n"
                                     "border-radius:10px;\n"
                                     "background-color: rgba(255, 255, 255, 180);\n"
                                     "border: 0px solid black;\n"
                                     "}\n"
                                     "\n"
                                     "\n"
                                     "")
        self.lineEdit4.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit4.setObjectName("lineEdit4")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(40, 210, 371, 21))
        self.label_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                   "color: rgb(255, 0, 4);\n"
                                   "font: 10pt \"微软雅黑\";")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(40, 470, 371, 21))
        self.label_5.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                   "color: rgb(255, 0, 4);\n"
                                   "font: 10pt \"微软雅黑\";")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(40, 390, 371, 21))
        self.label_4.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                   "color: rgb(255, 0, 4);\n"
                                   "font: 10pt \"微软雅黑\";")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(160, 660, 81, 31))
        self.label_6.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                   "font: 10pt \"微软雅黑\";\n"
                                   "")
        self.label_6.setObjectName("label_6")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 660, 51, 31))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
                                        "    \n"
                                        "    background-color: rgba(255, 255, 255, 0);\n"
                                        "    \n"
                                        "    font: 10pt \"微软雅黑\";\n"
                                        "    text-decoration: underline;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "    \n"
                                        "    color: rgb(38, 0, 255);\n"
                                        "}")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        self.pushButton_5.clicked.connect(Form.close)
        self.pushButton_2.clicked.connect(Form.close)  # type: ignore
        self.pushButton_3.clicked.connect(Form.showMinimized)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "注册"))
        self.pushButton.setText(_translate("Form", "注册账号"))
        self.lineEdit2.setPlaceholderText(_translate("Form", "账号："))
        self.lineEdit3.setPlaceholderText(_translate("Form", "密码："))
        self.lineEdit.setPlaceholderText(_translate("Form", "手机号"))
        self.lineEdit4.setPlaceholderText(_translate("Form", "确认密码："))
        self.label_6.setText(_translate("Form", "已有账号？"))
        self.pushButton_2.setText(_translate("Form", "登录"))


        self.pushButton_2.clicked.connect(self.login)
        self.pushButton.clicked.connect(self.enroll)
        self.lineEdit.textEdited.connect(self.bk1)
        self.lineEdit2.textEdited.connect(self.bk2)
        self.lineEdit3.textEdited.connect(self.bk3)
        self.lineEdit4.textEdited.connect(self.bk4)
        self.lineEdit.hover_started.connect(self.donghua)
        self.lineEdit.hover_ended.connect(self.fahui)
        self.lineEdit2.hover_started.connect(self.donghual2_2)
        self.lineEdit2.hover_ended.connect(self.fahui)
        self.lineEdit3.hover_started.connect(self.donghual2_3)
        self.lineEdit3.hover_ended.connect(self.fahui)
        self.lineEdit4.hover_started.connect(self.donghual2_4)
        self.lineEdit4.hover_ended.connect(self.fahui)

        self.shtow.xingyin.connect(self.zccg)                            #当自定义信号被发射时，关闭当前界面并打开“注册成功界面”


        reg = QRegExp("[0-9]+$")
        intvac = QRegExpValidator(reg)
        self.lineEdit.setValidator(intvac)

        reg = QRegExp("[0-9A-Za-z]+$")
        intvac = QRegExpValidator(reg)
        self.lineEdit2.setValidator(intvac)

        reg = QRegExp("[0-9A-Za-z]+$")
        intvac = QRegExpValidator(reg)
        self.lineEdit3.setValidator(intvac)

        reg = QRegExp("[0-9A-Za-z]+$")
        intvac = QRegExpValidator(reg)
        self.lineEdit4.setValidator(intvac)






    def bk1(self):
        self.lineEdit.setStyleSheet(
            "border-radius:10px;\n""background-color: rgba(255, 255, 255, 180);\n" "border: 0px solid red;")
        self.label_2.setText("")

    def bk2(self):
        self.lineEdit2.setStyleSheet(
            "border-radius:10px;\n""background-color: rgba(255, 255, 255, 180);\n" "border: 0px solid red;")
        self.label_3.setText("")

    def bk3(self):
        self.lineEdit3.setStyleSheet(
            "border-radius:10px;\n""background-color: rgba(255, 255, 255, 180);\n" "border: 0px solid red;")
        self.label_4.setText("")

    def bk4(self):
        self.lineEdit4.setStyleSheet(
            "border-radius:10px;\n""background-color: rgba(255, 255, 255, 180);\n" "border: 0px solid red;")
        self.label_5.setText("")

    def enroll(self):
        sjh = re.compile(r'^1[3-9]\d{9}$')
        with open('res/qtdata.json', 'r', encoding="UTF-8") as f:
            datajs = json.load(f)
            id = datajs[0]
            sd = datajs[1]
        if self.lineEdit.text() == "":
            self.lineEdit.setStyleSheet(
                "border-radius:10px;\n""background-color: rgba(255, 255, 255, 180);\n" "border: 2px solid red;")
            self.label_2.setText("请输入手机号")


        if self.lineEdit2.text() == "":
            self.lineEdit2.setStyleSheet(
                "border-radius:10px;\n""background-color: rgba(255, 255, 255, 180);\n" "border: 2px solid red;")
            self.label_3.setText("请输入账号")

        if self.lineEdit3.text() == "":
            self.lineEdit3.setStyleSheet(
                "border-radius:10px;\n""background-color: rgba(255, 255, 255, 180);\n" "border: 2px solid red;")
            self.label_4.setText("请输入密码")

        if self.lineEdit.text() != "" and self.lineEdit2.text() != "" and self.lineEdit3.text() != "":
            data = self.lineEdit.text()
            if sjh.match(data) is None:
                self.lineEdit.setStyleSheet(
                    "border-radius:10px;\n""background-color: rgba(255, 255, 255, 180);\n" "border: 2px solid red;")
                self.label_2.setText("无效手机号")

            elif self.lineEdit.text() in id:
                self.lineEdit.setStyleSheet(
                    "border-radius:10px;\n""background-color: rgba(255, 255, 255, 180);\n" "border: 2px solid red;")
                self.label_2.setText("手机号已被绑定")

            elif self.lineEdit2.text() in sd:
                self.lineEdit2.setStyleSheet(
                    "border-radius:10px;\n""background-color: rgba(255, 255, 255, 180);\n" "border: 2px solid red;")
                self.label_3.setText("该账号已存在")

            elif self.lineEdit4.text() == "":
                self.lineEdit4.setStyleSheet(
                    "border-radius:10px;\n""background-color: rgba(255, 255, 255, 180);\n" "border: 2px solid red;")
                self.label_5.setText("请再次输入认密码")


            elif self.lineEdit4.text() != self.lineEdit3.text():
                self.lineEdit4.setStyleSheet(
                    "border-radius:10px;\n""background-color: rgba(255, 255, 255, 180);\n" "border: 2px solid red;")
                self.label_5.setText("两次密码不一致")


            else:
                data1 = self.lineEdit.text()
                data2 = self.lineEdit2.text()
                data3 = self.lineEdit3.text()
                id[data1] = data2
                sd[data2] = data3
                data = [id, sd]
                with open("res/qtdata.json", "w", encoding="UTF-8") as f:
                    json.dump(data, f, ensure_ascii=False, indent=4)
                self.shtow.chaohanshu()
                self.close()





    def donghua(self):
        x, y, k, h = kj(self.lineEdit)
        x1, y1, k1, h1 = kj(self.lineEdit2)
        x2, y2, k2, h2 = kj(self.lineEdit3)
        x3, y3, k3, h3 = kj(self.lineEdit4)
        x4, y4, k4, h4 = kj(self.label_2)
        x5, y5, k5, h5 = kj(self.label_3)
        x6, y6, k6, h6 = kj(self.label_4)
        x7, y7, k7, h7 = kj(self.label_5)
        self.camd = QPropertyAnimation(self.lineEdit, b'geometry')
        self.camd.setDuration(50)
        self.camd.setStartValue(QRect(x, y, k, h))
        self.camd.setEndValue(QRect(x - 5, y - 5, k + 10, h + 10))
        self.binxin = QParallelAnimationGroup(self)

        self.camd2 = QPropertyAnimation(self.lineEdit2, b'geometry')
        self.camd2.setDuration(50)
        self.camd2.setStartValue(QRect(x1, y1, k1, h1))
        self.camd2.setEndValue(QRect(x1, y1 + 5, k1, h1))

        self.camd3 = QPropertyAnimation(self.lineEdit3, b'geometry')
        self.camd3.setDuration(50)
        self.camd3.setStartValue(QRect(x2, y2, k2, h2))
        self.camd3.setEndValue(QRect(x2, y2 + 5, k2, h2))

        self.camd4 = QPropertyAnimation(self.lineEdit4, b'geometry')
        self.camd4.setDuration(50)
        self.camd4.setStartValue(QRect(x3, y3, k3, h3))
        self.camd4.setEndValue(QRect(x3, y3 + 5, k3, h3))

        self.camdla1 = QPropertyAnimation(self.label_2, b'geometry')
        self.camdla1.setDuration(50)
        self.camdla1.setStartValue(QRect(x4, y4, k4, h4))
        self.camdla1.setEndValue(QRect(x4, y4 + 5, k4, h4))

        self.camdla2 = QPropertyAnimation(self.label_3, b'geometry')
        self.camdla2.setDuration(50)
        self.camdla2.setStartValue(QRect(x5, y5, k5, h5))
        self.camdla2.setEndValue(QRect(x5, y5 + 5, k5, h5))

        self.camdla3 = QPropertyAnimation(self.label_4, b'geometry')
        self.camdla3.setDuration(50)
        self.camdla3.setStartValue(QRect(x6, y6, k6, h6))
        self.camdla3.setEndValue(QRect(x6, y6 + 5, k6, h6))


        self.camdla4 = QPropertyAnimation(self.label_5, b'geometry')
        self.camdla4.setDuration(50)
        self.camdla4.setStartValue(QRect(x7, y7, k7, h7))
        self.camdla4.setEndValue(QRect(x7, y7 + 5, k7, h7))



        self.binxin.addAnimation(self.camd)
        self.binxin.addAnimation(self.camd2)
        self.binxin.addAnimation(self.camd3)
        self.binxin.addAnimation(self.camd4)
        self.binxin.addAnimation(self.camdla1)
        self.binxin.addAnimation(self.camdla2)
        self.binxin.addAnimation(self.camdla3)
        self.binxin.addAnimation(self.camdla4)
        self.binxin.start()

    def fahui(self):
        x, y, k, h = kj(self.lineEdit)
        x1, y1, k1, h1 = kj(self.lineEdit2)
        x2, y2, k2, h2 = kj(self.lineEdit3)
        x3, y3, k3, h3 = kj(self.lineEdit4)
        x4, y4, k4, h4 = kj(self.label_2)
        x5, y5, k5, h5 = kj(self.label_3)
        x6, y6, k6, h5 = kj(self.label_4)
        x7, y7, k7, h5 = kj(self.label_5)
        self.camd = QPropertyAnimation(self.lineEdit, b'geometry')
        self.camd.setDuration(50)
        self.camd.setStartValue(QRect(x, y, k, h))
        self.camd.setEndValue(QRect(40, 150, 370, 50))
        self.binxin2 = QParallelAnimationGroup(self)

        self.comd2 = QPropertyAnimation(self.lineEdit2, b'geometry')
        self.comd2.setDuration(50)
        self.comd2.setStartValue(QRect(x1, y1, k1, h1))
        self.comd2.setEndValue(QRect(40, 240, 370, 50))

        self.comd3 = QPropertyAnimation(self.lineEdit3, b'geometry')
        self.comd3.setDuration(50)
        self.comd3.setStartValue(QRect(x2, y2, k2, h2))
        self.comd3.setEndValue(QRect(40, 330, 370, 50))

        self.camd4 = QPropertyAnimation(self.lineEdit4, b'geometry')
        self.camd4.setDuration(50)
        self.camd4.setStartValue(QRect(x3, y3, k3, h3))
        self.camd4.setEndValue(QRect(40, 420, 370, 50))

        self.comdla1 = QPropertyAnimation(self.label_2, b'geometry')
        self.comdla1.setDuration(50)
        self.comdla1.setStartValue(QRect(x4, y4, k4, h4))
        self.comdla1.setEndValue(QRect(40, 210, 371, 21))

        self.comdla2 = QPropertyAnimation(self.label_3, b'geometry')
        self.comdla2.setDuration(50)
        self.comdla2.setStartValue(QRect(x5, y5, k5, h5))
        self.comdla2.setEndValue(QRect(40, 300, 371, 21))

        self.comdla3 = QPropertyAnimation(self.label_4, b'geometry')
        self.comdla3.setDuration(50)
        self.comdla3.setStartValue(QRect(x6, y6, k6, h5))
        self.comdla3.setEndValue(QRect(40, 390, 371, 21))

        self.comdla4 = QPropertyAnimation(self.label_5, b'geometry')
        self.comdla4.setDuration(50)
        self.comdla4.setStartValue(QRect(x7, y7, k7, h5))
        self.comdla4.setEndValue(QRect(40, 470, 371, 21))


        self.binxin2.addAnimation(self.camd)
        self.binxin2.addAnimation(self.comd2)
        self.binxin2.addAnimation(self.comd3)
        self.binxin2.addAnimation(self.camd4)
        self.binxin2.addAnimation(self.comdla1)
        self.binxin2.addAnimation(self.comdla2)
        self.binxin2.addAnimation(self.comdla3)
        self.binxin2.addAnimation(self.comdla4)
        self.binxin2.start()


    def donghual2_2(self):
        x, y, k, h = kj(self.lineEdit)
        x1, y1, k1, h1 = kj(self.lineEdit2)
        x2, y2, k2, h2 = kj(self.lineEdit3)
        x3, y3, k3, h3 = kj(self.lineEdit4)
        x4, y4, k4, h4 = kj(self.label_2)
        x5, y5, k5, h5 = kj(self.label_3)
        x6, y6, k6, h6 = kj(self.label_4)
        x7, y7, k7, h7 = kj(self.label_5)
        self.camd = QPropertyAnimation(self.lineEdit, b'geometry')
        self.camd.setDuration(50)
        self.camd.setStartValue(QRect(x, y, k, h))
        self.camd.setEndValue(QRect(x, y - 5, k, h))
        self.binxin = QParallelAnimationGroup(self)

        self.camd2 = QPropertyAnimation(self.lineEdit2, b'geometry')
        self.camd2.setDuration(50)
        self.camd2.setStartValue(QRect(x1, y1, k1, h1))
        self.camd2.setEndValue(QRect(x1 - 5, y1 - 5, k1 + 10, h1 + 10))

        self.camd3 = QPropertyAnimation(self.lineEdit3, b'geometry')
        self.camd3.setDuration(50)
        self.camd3.setStartValue(QRect(x2, y2, k2, h2))
        self.camd3.setEndValue(QRect(x2, y2 + 5, k2, h2))

        self.camd4 = QPropertyAnimation(self.lineEdit4, b'geometry')
        self.camd4.setDuration(50)
        self.camd4.setStartValue(QRect(x3, y3, k3, h3))
        self.camd4.setEndValue(QRect(x3, y3 + 5, k3, h3))

        self.camdla1 = QPropertyAnimation(self.label_2, b'geometry')
        self.camdla1.setDuration(50)
        self.camdla1.setStartValue(QRect(x4, y4, k4, h4))
        self.camdla1.setEndValue(QRect(x4, y4 - 5, k4, h4))

        self.camdla2 = QPropertyAnimation(self.label_3, b'geometry')
        self.camdla2.setDuration(50)
        self.camdla2.setStartValue(QRect(x5, y5, k5, h5))
        self.camdla2.setEndValue(QRect(x5, y5 + 5, k5, h5))

        self.camdla3 = QPropertyAnimation(self.label_4, b'geometry')
        self.camdla3.setDuration(50)
        self.camdla3.setStartValue(QRect(x6, y6, k6, h6))
        self.camdla3.setEndValue(QRect(x6, y6 + 5, k6, h6))


        self.camdla4 = QPropertyAnimation(self.label_5, b'geometry')
        self.camdla4.setDuration(50)
        self.camdla4.setStartValue(QRect(x7, y7, k7, h7))
        self.camdla4.setEndValue(QRect(x7, y7 + 5, k7, h7))

        self.binxin.addAnimation(self.camd)
        self.binxin.addAnimation(self.camd2)
        self.binxin.addAnimation(self.camd3)
        self.binxin.addAnimation(self.camd4)
        self.binxin.addAnimation(self.camdla1)
        self.binxin.addAnimation(self.camdla2)
        self.binxin.addAnimation(self.camdla3)
        self.binxin.addAnimation(self.camdla4)
        self.binxin.start()


    def donghual2_3(self):
        x, y, k, h = kj(self.lineEdit)
        x1, y1, k1, h1 = kj(self.lineEdit2)
        x2, y2, k2, h2 = kj(self.lineEdit3)
        x3, y3, k3, h3 = kj(self.lineEdit4)
        x4, y4, k4, h4 = kj(self.label_2)
        x5, y5, k5, h5 = kj(self.label_3)
        x6, y6, k6, h6 = kj(self.label_4)
        x7, y7, k7, h7 = kj(self.label_5)
        self.camd = QPropertyAnimation(self.lineEdit, b'geometry')
        self.camd.setDuration(50)
        self.camd.setStartValue(QRect(x, y, k, h))
        self.camd.setEndValue(QRect(x, y - 5, k, h))
        self.binxin = QParallelAnimationGroup(self)

        self.camd2 = QPropertyAnimation(self.lineEdit2, b'geometry')
        self.camd2.setDuration(50)
        self.camd2.setStartValue(QRect(x1, y1, k1, h1))
        self.camd2.setEndValue(QRect(x1, y1 - 5, k1, h1))

        self.camd3 = QPropertyAnimation(self.lineEdit3, b'geometry')
        self.camd3.setDuration(50)
        self.camd3.setStartValue(QRect(x2, y2, k2, h2))
        self.camd3.setEndValue(QRect(x2 - 5, y2 - 5, k2 + 10, h2 + 10))

        self.camd4 = QPropertyAnimation(self.lineEdit4, b'geometry')
        self.camd4.setDuration(50)
        self.camd4.setStartValue(QRect(x3, y3, k3, h3))
        self.camd4.setEndValue(QRect(x3, y3 + 5, k3, h3))
        self.camdla1 = QPropertyAnimation(self.label_2, b'geometry')
        self.camdla1.setDuration(50)
        self.camdla1.setStartValue(QRect(x4, y4, k4, h4))
        self.camdla1.setEndValue(QRect(x4, y4 - 5, k4, h4))

        self.camdla2 = QPropertyAnimation(self.label_3, b'geometry')
        self.camdla2.setDuration(50)
        self.camdla2.setStartValue(QRect(x5, y5, k5, h5))
        self.camdla2.setEndValue(QRect(x5, y5 - 5, k5, h5))

        self.camdla3 = QPropertyAnimation(self.label_4, b'geometry')
        self.camdla3.setDuration(50)
        self.camdla3.setStartValue(QRect(x6, y6, k6, h6))
        self.camdla3.setEndValue(QRect(x6, y6 + 5, k6, h6))

        self.camdla4 = QPropertyAnimation(self.label_5, b'geometry')
        self.camdla4.setDuration(50)
        self.camdla4.setStartValue(QRect(x7, y7, k7, h7))
        self.camdla4.setEndValue(QRect(x7, y7 + 5, k7, h7))

        self.binxin.addAnimation(self.camd)
        self.binxin.addAnimation(self.camd2)
        self.binxin.addAnimation(self.camd3)
        self.binxin.addAnimation(self.camd4)
        self.binxin.addAnimation(self.camdla1)
        self.binxin.addAnimation(self.camdla2)
        self.binxin.addAnimation(self.camdla3)
        self.binxin.addAnimation(self.camdla4)
        self.binxin.start()

    def donghual2_4(self):
        x, y, k, h = kj(self.lineEdit)
        x1, y1, k1, h1 = kj(self.lineEdit2)
        x2, y2, k2, h2 = kj(self.lineEdit3)
        x3, y3, k3, h3 = kj(self.lineEdit4)
        x4, y4, k4, h4 = kj(self.label_2)
        x5, y5, k5, h5 = kj(self.label_3)
        x6, y6, k6, h6 = kj(self.label_4)
        x7, y7, k7, h7 = kj(self.label_5)
        self.camd = QPropertyAnimation(self.lineEdit, b'geometry')
        self.camd.setDuration(50)
        self.camd.setStartValue(QRect(x, y, k, h))
        self.camd.setEndValue(QRect(x, y - 5, k, h))
        self.binxin = QParallelAnimationGroup(self)

        self.camd2 = QPropertyAnimation(self.lineEdit2, b'geometry')
        self.camd2.setDuration(50)
        self.camd2.setStartValue(QRect(x1, y1, k1, h1))
        self.camd2.setEndValue(QRect(x1, y1 - 5, k1, h1))

        self.camd3 = QPropertyAnimation(self.lineEdit3, b'geometry')
        self.camd3.setDuration(50)
        self.camd3.setStartValue(QRect(x2, y2, k2, h2))
        self.camd3.setEndValue(QRect(x2, y2 - 5, k2, h2))

        self.camd4 = QPropertyAnimation(self.lineEdit4, b'geometry')
        self.camd4.setDuration(50)
        self.camd4.setStartValue(QRect(x3, y3, k3, h3))
        self.camd4.setEndValue(QRect(x3 - 5, y3 - 5, k3 + 10, h3 + 10))

        self.camdla1 = QPropertyAnimation(self.label_2, b'geometry')
        self.camdla1.setDuration(50)
        self.camdla1.setStartValue(QRect(x4, y4, k4, h4))
        self.camdla1.setEndValue(QRect(x4, y4 - 5, k4, h4))

        self.camdla2 = QPropertyAnimation(self.label_3, b'geometry')
        self.camdla2.setDuration(50)
        self.camdla2.setStartValue(QRect(x5, y5, k5, h5))
        self.camdla2.setEndValue(QRect(x5, y5 - 5, k5, h5))

        self.camdla3 = QPropertyAnimation(self.label_4, b'geometry')
        self.camdla3.setDuration(50)
        self.camdla3.setStartValue(QRect(x6, y6, k6, h6))
        self.camdla3.setEndValue(QRect(x6, y6 - 5, k6, h6))

        self.camdla4 = QPropertyAnimation(self.label_5, b'geometry')
        self.camdla4.setDuration(50)
        self.camdla4.setStartValue(QRect(x7, y7, k7, h7))
        self.camdla4.setEndValue(QRect(x7, y7 + 5, k7, h7))

        self.binxin.addAnimation(self.camd)
        self.binxin.addAnimation(self.camd2)
        self.binxin.addAnimation(self.camd3)
        self.binxin.addAnimation(self.camd4)
        self.binxin.addAnimation(self.camdla1)
        self.binxin.addAnimation(self.camdla2)
        self.binxin.addAnimation(self.camdla3)
        self.binxin.addAnimation(self.camdla4)
        self.binxin.start()


