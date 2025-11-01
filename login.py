from PyQt5.QtCore import QRegExp, QPropertyAnimation, QRect, pyqtSignal, QParallelAnimationGroup
from PyQt5.QtGui import QRegExpValidator, QFocusEvent
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit
import json
from func import *                          #自定义函数
from enroll import Ui_Form_2



class HoverLineEdit(QLineEdit):
    hover_started = pyqtSignal()                    #当鼠标在控件内时发射信号
    hover_ended = pyqtSignal()                      #当鼠标离开控件时发射信号
    xuanzhong = pyqtSignal()                        #当控件被选中（焦点）时发射信号
    notxuanzhong = pyqtSignal()                     #当控件没被选中（失去焦点）的时候发射信号

    def enterEvent(self, event):
        super().enterEvent(event)
        self.hover_started.emit()

    def leaveEvent(self, event):
        super().leaveEvent(event)
        self.hover_ended.emit()

    def focusInEvent(self, event):
        super().focusInEvent(event)
        self.xuanzhong.emit()

    def focusOutEvent(self, event):
        super().focusOutEvent(event)
        self.notxuanzhong.emit()




class Ui_Form(object):
    # noinspection PyUnresolvedReferences
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(747, 955)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(170, 10, 450, 830))
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
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 610, 171, 41))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
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
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(140, 550, 171, 41))
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
        self.lineEdit = HoverLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(40, 160, 371, 51))
        self.lineEdit.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"border-radius:10px;\n"
"background-color: rgba(255, 255, 255, 180);\n"
"border: 0px solid black;"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = HoverLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(40, 240, 371, 51))
        self.lineEdit_2.setStyleSheet("QLineEdit{\n"
"border-radius:10px;\n"
"background-color: rgba(255, 255, 255, 180);\n"
"border: 0px solid black;"
"}")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(40, 310, 371, 21))
        self.label_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 0, 4);\n"
"font: 10pt \"Agency FB\";")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.checkBox = QtWidgets.QCheckBox(self.frame)
        self.checkBox.setGeometry(QtCore.QRect(110, 450, 91, 19))
        self.checkBox.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"font: 75 9pt \"Agency FB\";")
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_2.setGeometry(QtCore.QRect(250, 450, 91, 19))
        self.checkBox_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"font: 75 9pt \"Agency FB\";")
        self.checkBox_2.setObjectName("checkBox_2")

        self.retranslateUi(Form)
        self.pushButton_5.clicked.connect(Form.close) # type: ignore
        self.pushButton_3.clicked.connect(Form.showMinimized) # type: ignore
        self.pushButton_2.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)



    def put(self):
        x, y, k, h = kj(self.pushButton)
        self.putdh = QPropertyAnimation(self.pushButton, b'geometry')
        self.putdh.setDuration(80)
        self.putdh.setStartValue(QRect(x, y, k, h))
        self.putdh.setKeyValueAt(0.5, QRect(150, 555, 151, 31))
        self.putdh.setEndValue(QRect(140, 550, 171, 41))
        self.putdh.start()





    def dhbutton(self):
        x, y, k, h = kj(self.lineEdit)
        x1 ,y1, k1, h1 = kj(self.label_2)
        x2, y2, k2, h2 = kj(self.lineEdit_2)
        self.comd = QPropertyAnimation(self.lineEdit, b'geometry')
        self.comd.setDuration(50)
        self.comd.setStartValue(QRect(x, y, k, h))
        self.comd.setEndValue(QRect(35, 155, 380, 60))

        self.comd2 = QPropertyAnimation(self.label_2, b'geometry')
        self.comd2.setDuration(50)
        self.comd2.setStartValue(QRect(x1, y1, k1, h1))
        self.comd2.setEndValue(QRect(40, 315, 371, 21))

        self.comd3 = QPropertyAnimation(self.lineEdit_2, b'geometry')
        self.comd3.setDuration(50)
        self.comd3.setStartValue(QRect(x2, y2, k2, h2))
        self.comd3.setEndValue(QRect(40, 245, 371, 51))


        self.bingxing = QParallelAnimationGroup(self)
        self.bingxing.addAnimation(self.comd)
        self.bingxing.addAnimation(self.comd2)
        self.bingxing.addAnimation(self.comd3)
        self.bingxing.start()

    def dhbutton2(self):
        x, y, k, h = kj(self.lineEdit)
        x1 ,y1, k1, h1 = kj(self.label_2)
        x2, y2, k2, h2 = kj(self.lineEdit_2)
        self.comd = QPropertyAnimation(self.lineEdit, b'geometry')
        self.comd.setDuration(50)
        self.comd.setStartValue(QRect(x, y, k, h))
        self.comd.setEndValue(QRect(40, 160, 371, 51))

        self.comd2 = QPropertyAnimation(self.label_2, b'geometry')
        self.comd2.setDuration(50)
        self.comd2.setStartValue(QRect(x1, y1, k1, h1))
        self.comd2.setEndValue(QRect(40, 310, 371, 21))

        self.comd3 = QPropertyAnimation(self.lineEdit_2, b'geometry')
        self.comd3.setDuration(50)
        self.comd3.setStartValue(QRect(x2, y2, k2, h2))
        self.comd3.setEndValue(QRect(40, 240, 371, 51))

        self.bingxing = QParallelAnimationGroup(self)
        self.bingxing.addAnimation(self.comd)
        self.bingxing.addAnimation(self.comd2)
        self.bingxing.addAnimation(self.comd3)
        self.bingxing.start()

    def dhbuttonmm1(self):
        x, y, k, h = kj(self.lineEdit)
        x1 ,y1, k1, h1 = kj(self.label_2)
        x2, y2, k2, h2 = kj(self.lineEdit_2)
        self.comda1 = QPropertyAnimation(self.lineEdit_2, b'geometry')
        self.comda1.setDuration(50)
        self.comda1.setStartValue(QRect(x2, y2, k2, h2))
        self.comda1.setEndValue(QRect(35, 235, 380, 60))

        self.comda2 = QPropertyAnimation(self.label_2, b'geometry')
        self.comda2.setDuration(50)
        self.comda2.setStartValue(QRect(x1, y1, k1, h1))
        self.comda2.setEndValue(QRect(40, 315, 371, 21))

        self.comda3 = QPropertyAnimation(self.lineEdit, b'geometry')
        self.comda3.setDuration(50)
        self.comda3.setStartValue(QRect(40, 160, 371, 51))
        self.comda3.setEndValue(QRect(40, 155, 371, 51))



        self.bingxing = QParallelAnimationGroup(self)
        self.bingxing.addAnimation(self.comda1)
        self.bingxing.addAnimation(self.comda2)
        self.bingxing.addAnimation(self.comda3)
        self.bingxing.start()

    def dhbuttonmm2(self):
        x, y, k, h = kj(self.lineEdit)
        x1, y1, k1, h1 = kj(self.label_2)
        x2, y2, k2, h2 = kj(self.lineEdit_2)

        self.comda1 = QPropertyAnimation(self.lineEdit_2, b'geometry')
        self.comda1.setDuration(50)
        self.comda1.setStartValue(QRect(x2, y2, k2, h2))
        self.comda1.setEndValue(QRect(40, 240, 371, 51))

        self.comda2 = QPropertyAnimation(self.label_2, b'geometry')
        self.comda2.setDuration(50)
        self.comda2.setStartValue(QRect(x1, y1, k1, h1))
        self.comda2.setEndValue(QRect(40, 310, 371, 21))

        self.comda3 = QPropertyAnimation(self.lineEdit, b'geometry')
        self.comda3.setDuration(50)
        self.comda3.setStartValue(QRect(x, y, k, h))
        self.comda3.setEndValue(QRect(40, 160, 371, 51))

        self.bingxing = QParallelAnimationGroup(self)
        self.bingxing.addAnimation(self.comda1)
        self.bingxing.addAnimation(self.comda2)
        self.bingxing.addAnimation(self.comda3)
        self.bingxing.start()


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "登录"))
        self.pushButton_2.setText(_translate("Form", "注册"))
        self.pushButton.setText(_translate("Form", "登录"))
        self.lineEdit.setPlaceholderText(_translate("Form", "账号："))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "密码："))
        self.checkBox.setText(_translate("Form", "记住密码"))
        self.checkBox_2.setText(_translate("Form", "自动登录"))

        self.pushButton_2.clicked.connect(self.zichuangko)
        self.lineEdit.hover_started.connect(self.dhbutton)
        self.lineEdit.hover_ended.connect(self.dhbutton2)
        self.lineEdit_2.hover_started.connect(self.dhbuttonmm1)
        self.lineEdit_2.hover_ended.connect(self.dhbuttonmm2)
        self.pushButton.clicked.connect(self.login)
        self.pushButton.clicked.connect(self.put)
        self.lineEdit.textEdited.connect(self.dj1)
        self.lineEdit_2.textEdited.connect(self.dj2)
        self.lineEdit_2.returnPressed.connect(self.login)
        self.lineEdit.xuanzhong.connect(self.xuanzhong)
        self.lineEdit.notxuanzhong.connect(self.notxuanzhong)



        reg = QRegExp("[0-9A-Za-z]+$")
        intvac = QRegExpValidator(reg)
        self.lineEdit.setValidator(intvac)

        reg2 = QRegExp("[0-9A-Za-z]+$")
        intvac = QRegExpValidator(reg)
        self.lineEdit_2.setValidator(intvac)







    def login(self):
        with open('res\qtdata.json', 'r', encoding="UTF-8") as f:
            datajs = json.load(f)
            id = datajs[0]
            sd = datajs[1]
        if self.lineEdit.text() == "" and self.lineEdit_2.text() == "":
            self.label_2.setText("账号和密码不能为空")
            self.lineEdit.setStyleSheet("border-radius:10px;\n"
"background-color: rgba(255, 255, 255, 180);\n"
"border: 2px solid red;")
            self.lineEdit_2.setStyleSheet("border-radius:10px;\n"
"background-color: rgba(255, 255, 255, 180);\n"
"border: 2px solid red;")

        elif self.lineEdit.text() == "":
            self.lineEdit.setStyleSheet(
                "border-radius:10px;\n""background-color: rgba(255, 255, 255, 180);\n" "border: 2px solid red;")
            self.label_2.setText("请输入入账号")


        elif self.lineEdit.text() not in sd:
            self.lineEdit.setStyleSheet(
                "border-radius:10px;\n""background-color: rgba(255, 255, 255, 180);\n" "border: 2px solid red;")
            self.label_2.setText("账号不存在")

        elif self.lineEdit_2.text() != sd[self.lineEdit.text()]:
            self.label_2.setText("账号或密码错误")
            self.lineEdit_2.setText("")
            self.lineEdit.setStyleSheet("border-radius:10px;\n""background-color: rgba(255, 255, 255, 180);\n" "border: 0px solid red;")
            self.lineEdit_2.setStyleSheet("border-radius:10px;\n" "background-color: rgba(255, 255, 255, 180);\n" "border: 2px solid red;")

        elif self.lineEdit_2.text() == sd[self.lineEdit.text()]:
            self.label_2.setText("")





    def dj1(self):
        self.lineEdit.setStyleSheet(
            "border-radius:10px;\n""background-color: rgba(255, 255, 255, 180);\n" "border: 0px solid black;")
        self.label_2.setText("")

    def dj2(self):
        self.lineEdit_2.setStyleSheet(
            "border-radius:10px;\n""background-color: rgba(255, 255, 255, 180);\n" "border: 0px solid black;")
        self.label_2.setText("")

    def xuanzhong(self):
        pass

    def notxuanzhong(self):
        pass
