import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Experiment1 import Diamond
from Experiment2 import DrawLine

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.experiment = dict()

        self.experiment['实验一 绘制金刚石图案'] = Diamond
        self.experiment['实验二 绘制任意斜率直线段'] = DrawLine

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

        for k, v in self.experiment.items():
            action = QAction(k, self)
            action.triggered.connect(
                (lambda x: lambda: self.setCentralWidget(x(self)))(v)
            )
            draw_menu.addAction(action)

        # diamond_action = QAction('&Diamond', self)
        # diamond_action.triggered.connect(
        #     (lambda x: lambda: self.setCentralWidget(x(self)))(Diamond)
        # )
        # draw_menu.addAction(diamond_action)

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