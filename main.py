import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Experiment1 import Diamond

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.experiment = dict()

        self.experiment['实验一 绘制金刚石图案'] = Diamond

        self.about = '姓名:\t范家铭\n班级:\t计科17-3\n学号:\t201701060503'
        self.initUI()

    def initUI(self):

        self.setWindowTitle('图形学实验')
        self.resize(1200, 800)

        menu = self.menuBar()
        fileMenu = menu.addMenu('&File')
        draw_menu = menu.addMenu('&Draw')

        exit_action = QAction('&Exit', self)
        exit_action.triggered.connect(self.close)
        fileMenu.addAction(exit_action)

        diamond_action = QAction('&Diamond', self)
        diamond_action.triggered.connect(
            (lambda x: lambda: self.setCentralWidget(x(self)))(Diamond)
        )
        draw_menu.addAction(diamond_action)

        about_action = QAction('&About', self)
        about_action.triggered.connect(
            lambda: QMessageBox.about(self, 'about', self.about)
        )
        menu.addAction(about_action)

    def keyPressEvent(self, event: QKeyEvent):
        if self.centralWidget() is not None:
            self.centralWidget().keyPressEvent(event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())