import sys
import random
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt


COLORS = [
    # 17 undertones https://lospec.com/palette-list/17undertones
    '#000000', '#141923', '#414168', '#3a7fa7', '#35e3e3', '#8fd970', '#5ebb49',
    '#458352', '#dcd37b', '#fffee5', '#ffd035', '#cc9245', '#a15c3e', '#a42f3b',
    '#f45b7a', '#c24998', '#81588d', '#bcb0c2', '#ffffff',
    ]
SPRAY_PARTICLES = 100
SPRAY_DIAMETER = 10


class Canvas(QtWidgets.QLabel):
    
    def __init__(self):
        super().__init__()
        pixmap = QtGui.QPixmap(600, 300)
        self.setPixmap(pixmap)

        self.last_x, self.last_y = None, None
        self.pen_color = QtGui.QColor('#ffffff')
        
        self.mode_line = False
        self.mode_spray = False

    def set_pen_color(self, c):
        self.pen_color = QtGui.QColor(c)

    def set_mode(self, mode):
        if mode == 'line':
            self.mode_line =True
            self.mode_spray = False
        elif mode == 'spray':
            self.mode_spray = True
            self.mode_line = False

##    # For spray
##    def mouseMoveEvent(self, e):
##        painter = QtGui.QPainter(self.pixmap())
##        pen = painter.pen()
##        pen.setWidth(1)
##        pen.setColor(self.pen_color)
##        painter.setPen(pen)
##
##        for n in range(SPRAY_PARTICLES):
##            xo = random.gauss(0, SPRAY_DIAMETER)
##            yo = random.gauss(0, SPRAY_DIAMETER)
##            painter.drawPoint(e.x() + xo, e.y() + yo)
##
##        self.update()

    
    def mouseMoveEvent(self, e):
        if self.mode_line:
            
            if self.last_x is None: # First event
                self.last_x = e.x()
                self.last_y = e.y()
                return # Ignore the first time
            
            painter = QtGui.QPainter(self.pixmap())
            pen = painter.pen()
            pen.setColor(self.pen_color)
            painter.setPen(pen)
            painter.drawLine(self.last_x, self.last_y, e.x(), e.y())
            painter.end()
            self.update()

            # Update the origin for next time
            self.last_x = e.x()
            self.last_y = e.y()
        elif self.mode_spray:
            painter = QtGui.QPainter(self.pixmap())
            pen = painter.pen()
            pen.setWidth(1)
            pen.setColor(self.pen_color)
            painter.setPen(pen)

            for n in range(SPRAY_PARTICLES):
                xo = random.gauss(0, SPRAY_DIAMETER)
                yo = random.gauss(0, SPRAY_DIAMETER)
                painter.drawPoint(e.x() + xo, e.y() + yo)

            self.update()
        else:
            painter = QtGui.QPainter(self.pixmap())
            pen = painter.pen()
            pen.setWidth(1)
            pen.setColor(self.pen_color)
            painter.setPen(pen)

            for n in range(SPRAY_PARTICLES):
                xo = random.gauss(0, SPRAY_DIAMETER)
                yo = random.gauss(0, SPRAY_DIAMETER)
                painter.drawPoint(e.x() + xo, e.y() + yo)

            self.update()


    def mouseReleaseEvent(self, e):
        self.last_x = None
        self.last_y = None

class QPaletteButton(QtWidgets.QPushButton):

    def __init__(self, color):
        super().__init__()
        self.setFixedSize(QtCore.QSize(24,24))
        self.color = color
        self.setStyleSheet("background-color: %s" % color)
        

class MainWindow(QtWidgets.QMainWindow):
    
    def __init__(self):
        super().__init__()

        self.canvas = Canvas()

        w = QtWidgets.QWidget()
        l = QtWidgets.QVBoxLayout()
        w.setLayout(l)
        l.addWidget(self.canvas)

        palette = QtWidgets.QHBoxLayout()
        self.add_palette_buttons(palette)
        l.addLayout(palette)

        mode_selection = QtWidgets.QHBoxLayout()
        line_button = QtWidgets.QPushButton("Line")
        spray_button = QtWidgets.QPushButton("Spray")
        mode_selection.addWidget(line_button)
        mode_selection.addWidget(spray_button)

        line_button.pressed.connect(lambda mode='line': self.canvas.set_mode(mode))
        spray_button.pressed.connect(lambda mode='spray':self.canvas.set_mode(mode))


        l.addLayout(mode_selection)

        self.setCentralWidget(w)

    def add_palette_buttons(self, layout):
        for c in COLORS:
            b = QPaletteButton(c)
            b.pressed.connect(lambda c=c: self.canvas.set_pen_color(c))
            layout.addWidget(b)



app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
