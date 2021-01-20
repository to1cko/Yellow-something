import sys
import random

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QWidget
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(180, 250, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "PushButton"))


class MyWidget(QWidget, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)
        self.x, self.y = 400, 300
        self.q = False

        # Обратите внимание: имя элемента такое же как в QTDesigner6-

    def paintEvent(self, event):
        if self.q:
            qp = QPainter()
            qp.begin(self)
            self.drawing(qp)
            qp.end()
            #self.update()

    def drawing(self, qp):
        size = self.size()
        r = random.randint(10, 100)
        qp.setBrush(QColor(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)))
        qp.drawEllipse(random.randint(0, size.width() - r // 2), random.randint(0, size.height() - r // 2), r, r)
        qp.setPen(Qt.red)
        self.q = False
        # Имя элемента совпадает с objectName в QTDesigner

    def run(self):
        self.q = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
