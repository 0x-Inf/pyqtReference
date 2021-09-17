import sys
from random import randint, choice
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(400, 300)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)
        self.draw_something()


    def draw_something(self):
        colors = ['#FFD141', '#376F9F', '#0D1F2D', '#E9EBEF', '#EB5160']
        
        painter = QtGui.QPainter(self.label.pixmap())
        pen = QtGui.QPen()
        pen.setWidth(3)
        pen.setColor(QtGui.QColor('green'))
        painter.setPen(pen)

##        # Filling drawn shapes
##        brush = QtGui.QBrush()
##        brush.setColor(QtGui.QColor('#FFD141'))
##        brush.setStyle(Qt.Dense1Pattern)
##        painter.setBrush(brush)
##        painter.drawLine(10, 10, 300, 200)
##        painter.drawPoint(200,150)
##        for n in range(10000):
##            # pen = painter.pen() you could get the active pen here
##            pen.setColor(QtGui.QColor(choice(colors)))
##            painter.setPen(pen)
##            painter.drawPoint(
##                200+randint(-100, 100), # x
##                150+randint(-100, 100)  # y
##                )
##        # drawing line
##        painter.drawLine(
##            QtCore.QPoint(100, 100),
##            QtCore.QPoint(300, 200)
##        )
        # drawing rectangles
##        painter.drawRect(50, 50, 100, 100)
##        painter.drawRect(60, 60, 150, 100)
##        painter.drawRect(70, 70, 100, 150)
##        painter.drawRect(80, 80, 150, 100)
##        painter.drawRect(90, 90, 100, 150)
##        # draw multiple rect with single `drawRect`
##        painter.drawRects(
##            QtCore.QRect(50, 50, 100, 100),
##            QtCore.QRect(60, 60, 150, 100),
##            QtCore.QRect(70, 70, 100, 150),
##            QtCore.QRect(80, 80, 150, 100),
##            QtCore.QRect(90, 90, 100, 150)
##            )

##        # drawing rounded rectangles
##        painter.drawRoundedRect(40, 40, 100, 100, 10, 10)
##        painter.drawRoundedRect(80, 80, 100, 100, 10, 50)
##        painter.drawRoundedRect(120, 120, 100, 100, 50, 10)
##        painter.drawRoundedRect(160, 160, 100, 100, 50, 50)

##        # drawing ellipses
##        painter.drawEllipse(10, 10, 100, 100)
##        painter.drawEllipse(10, 10, 150, 200)
##        painter.drawEllipse(10, 10, 200, 300)
##
##        painter.drawEllipse(QtCore.QPoint(100, 100), 10, 10)
##        painter.drawEllipse(QtCore.QPoint(100, 100), 15, 20)
##        painter.drawEllipse(QtCore.QPoint(100, 100), 20, 30)
##        painter.drawEllipse(QtCore.QPoint(100, 100), 25, 40)
##        painter.drawEllipse(QtCore.QPoint(100, 100), 30, 50)
##        painter.drawEllipse(QtCore.QPoint(100, 100), 35, 60)

        # Text
        font = QtGui.QFont()
        font.setFamily('Times')
        font.setBold(True)
        font.setPointSize(40)
        painter.setFont(font)

        # painter.drawText(100, 100, 'Hello, world!')
        painter.drawText(100, 100, 100, 100, Qt.AlignHCenter, 'Hello, world!')
        
        painter.end()

        
app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()










