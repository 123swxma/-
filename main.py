from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QMouseEvent
from login import Ui_Form
from enroll import Ui_Form_2
from zccg import Ui_Form_3
import sys, qtdata


class DraggableMainWindow(QMainWindow, Ui_Form):
    def __init__(self):
        super(DraggableMainWindow, self).__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setupUi(self)
        self.dragging = False
        self.drag_position = QPoint()

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.dragging = True
            self.drag_position = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event: QMouseEvent):
        if self.dragging:
            self.move(event.globalPos() - self.drag_position)
            event.accept()

    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.dragging = False
            event.accept()

    def zichuangko(self):
        self.chuangko = ui_2()
        self.chuangko.show()


class ui_2(Ui_Form_2):
    def __init__(self):
        super(ui_2, self).__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setupUi(self)
        self.dragging = False
        self.drag_position = QPoint()

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.dragging = True
            self.drag_position = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event: QMouseEvent):
        if self.dragging:
            self.move(event.globalPos() - self.drag_position)
            event.accept()

    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.dragging = False
            event.accept()

    def login(self):
        self.mainw = DraggableMainWindow()  #打开登录窗口
        self.mainw.show()

    def zccg(self):  #打开“注册成功”窗口
        self.ui_3 = ui_3()
        self.ui_3.show()


class ui_3(Ui_Form_3):
    def __init__(self):
        super(ui_3, self).__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setupUi(self)
        self.dragging = False
        self.drag_position = QPoint()

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.dragging = True
            self.drag_position = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event: QMouseEvent):
        if self.dragging:
            self.move(event.globalPos() - self.drag_position)
            event.accept()

    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.dragging = False
            event.accept()

    def denglu(self):
        self.mainw = DraggableMainWindow()
        self.mainw.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = DraggableMainWindow()
    ui.show()
    sys.exit(app.exec_())
