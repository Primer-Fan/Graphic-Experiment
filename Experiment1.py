from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.Qt import *
import math


class InputDialog(QDialog):
    def __init__(self):
        super(InputDialog, self).__init__()
        self.iniUI()

    def iniUI(self):
        self.setWindowTitle('Input Parameter')
        self.label_num = QLabel('等分点个数')
        self.label_radius = QLabel('半径')
        self.input_num = QLineEdit()
        self.input_radius = QLineEdit()
        self.buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)

        self.grid = QGridLayout()
        self.grid.addWidget(self.label_num, 0, 0)
        self.grid.addWidget(self.input_num, 0, 1)
        self.grid.addWidget(self.label_radius, 1, 0)
        self.grid.addWidget(self.input_radius, 1, 1)
        self.grid.addWidget(self.buttons, 2, 0)

        self.setLayout(self.grid)

    def get_data(self):
        try:
            return int(self.input_num.text()), float(self.input_radius.text())
        except Exception as e:
            QMessageBox.warning(self, '错误', '非法输入')
            print(e)
            return None, None


class Diamond(QWidget):
    def __init__(self, parent=None):
        super(Diamond, self).__init__(parent)

        self.input = InputDialog()
        self.num, self.radius = None, None
        self.initNum()

    def initNum(self):
        if self.input.exec_():
            self.num, self.radius = self.input.get_data()
            if self.num is not None and self.radius is not None:
                if self.num < 5 or self.num > 50:
                    QMessageBox.warning(self, '错误', '等分点数量应该在5-50之间')
                    self.initNum()
                    return
                if self.radius < 200 or self.radius > 400:
                    QMessageBox.warning(self, '错误', '半径应该在200-400之间')
                    self.initNum()
                    return

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        if self.num is None or self.radius is None:
            return None

        painter = QPainter(self)
        pen = QPen(Qt.blue, 1, Qt.SolidLine)
        painter.setPen(pen)

        x, y = list(), list()
        sx, sy = self.size().width() / 2, self.size().height() / 2
        for i in range(self.num):
            x.append(int(self.radius * math.sin(2 * math.pi * i / self.num) + sx))
            y.append(int(self.radius * math.cos(2 * math.pi * i / self.num) + sy))

        for i in range(self.num):
            for j in range(i + 1, self.num):
                painter.drawLine(x[i], y[i], x[j], y[j])
