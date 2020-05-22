from PyQt5.Qt import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class CLine(object):
    def __init__(self):
        self.begin_point, self.end_point = QPoint(0, 0), QPoint(0, 0)

    def set_begin_point(self, point: QPoint):
        self.begin_point = point

    def set_end_point(self, point: QPoint):
        self.end_point = point

    def draw_line(self, painter: QPainter):
        if self.begin_point.x() > self.end_point.x():
            self.begin_point, self.end_point = self.end_point, self.begin_point

        if self.end_point.y() >= self.begin_point.y():
            if self.end_point.y() - self.begin_point.y() <= self.end_point.x() - self.begin_point.x():
                self._draw_line1(painter)
            else:
                self._draw_line2(painter)
        else:
            if self.begin_point.y() - self.end_point.y() <= self.end_point.x() - self.begin_point.x():
                self._draw_line3(painter)
            else:
                self._draw_line4(painter)


    def _draw_line1(self, painter: QPainter):   # 斜率 0 <= k <= 1
        x, y = self.begin_point.x(), self.begin_point.y()
        dx, dy = self.end_point.x() - self.begin_point.x(), self.end_point.y() - self.begin_point.y()
        e = -dx
        while x <= self.end_point.x():
            painter.drawPoint(x, y)
            x, e = x + 1, e + 2 * dy
            if e >= 0:
                y, e = y + 1, e - 2 * dx

    def _draw_line2(self, painter: QPainter):   # 斜率 k > 1
        x, y = self.begin_point.x(), self.begin_point.y()
        dx, dy = self.end_point.x() - self.begin_point.x(), self.end_point.y() - self.begin_point.y()
        e = -dy
        while y <= self.end_point.y():
            painter.drawPoint(x, y)
            y, e = y + 1, e + 2 * dx
            if e >= 0:
                x, e = x + 1, e - 2 * dy

    def _draw_line3(self, painter: QPainter):   # 斜率 -1 <= k < 0
        x, y = self.begin_point.x(), self.begin_point.y()
        dx, dy = self.end_point.x() - self.begin_point.x(), self.end_point.y() - self.begin_point.y()
        e = -dx
        while x <= self.end_point.x():
            painter.drawPoint(x, y)
            x, e = x + 1, e + 2 * dy
            if e <= 0:
                y, e = y - 1, e + 2 * dx

    def _draw_line4(self, painter: QPainter):
        x, y = self.begin_point.x(), self.begin_point.y()
        dx, dy = self.end_point.x() - self.begin_point.x(), self.end_point.y() - self.begin_point.y()
        e = -dy
        while y >= self.end_point.y():
            painter.drawPoint(x, y)
            y, e = y - 1, e - 2 * dx
            if e <= 0:
                x, e = x + 1, e - 2 * dy


class DrawLine(QWidget):
    def __init__(self, parent=None):
        super(DrawLine, self).__init__(parent)

        self.setMouseTracking(True)
        self.pixmap = QPixmap(self.parent().width(), self.parent().height())
        self.pixmap.fill(Qt.white)
        self.line = CLine()

    def paintEvent(self, event: QPaintEvent):
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pixmap)

    def mouseMoveEvent(self, event: QMouseEvent):
        status = self.parent().statusBar()
        message = '鼠标位置: X: {}, Y: {}'.format(event.pos().x(), event.pos().y())
        status.showMessage(message)

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.line.set_begin_point(event.pos())

    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.line.set_end_point(event.pos())
            painter = QPainter(self.pixmap)
            pen = QPen(Qt.black, 2, Qt.SolidLine)
            painter.setPen(pen)
            self.line.draw_line(painter)
            self.update()
