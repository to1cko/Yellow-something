import sys
import random

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt


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
            #self.update()

    def drawing(self, qp):
        size = self.size()
        r = random.randint(10, 100)
        qp.setBrush(QColor('Yellow'))
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
