import sys
import random

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtGui import QPainter, QColor


class MyWidget(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.run)
        self.x, self.y = 400, 300
        self.q = False

        # Обратите внимание: имя элемента такое же как в QTDesigner

    def paintEvent(self, event):
        if self.q:
            qp = QPainter()
            qp.begin(self)
            self.drawing(qp)
            qp.end()
            #self.q = False

    def drawing(self, qp):
        # qp.end()
        r = random.randint(0, 100)
        #qp.setBrush(QColor('Yellow'))
        qp.drawEllipse(random.randint(0, self.x - r // 2), random.randint(0, self.y - r // 2), r, r)
        qp.drawEllipse(10, 20, 5, 5)
        for i in range(1000):
            x = random.randint(1, self.x - 1)
            y = random.randint(1, self.y - 1)
            qp.drawPoint(x, y)
        # Имя элемента совпадает с objectName в QTDesigner

    def run(self):
        self.q = True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
