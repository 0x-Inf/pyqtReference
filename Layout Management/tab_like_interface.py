from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys

class Color(QWidget):

    def __init__(self, color, *args, **kwargs):
        super(Color, self).__init__(*args, **kwargs)
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

# Using stacked layout to create tab like interface
##class MainWindow(QMainWindow):
##
##    def __init__(self, *args, **kwargs):
##        super(MainWindow, self).__init__(*args, **kwargs)
##        
##        self.setWindowTitle("My Tabbed App")
##
##        pagelayout = QVBoxLayout()
##        button_layout = QHBoxLayout()
##        layout = QStackedLayout()
##
##        pagelayout.addLayout(button_layout)
##        pagelayout.addLayout(layout)
##
##        for n, color in enumerate(['red','green', 'blue','yellow']):
##            btn = QPushButton( str(color) )
##            btn.pressed.connect( lambda n=n: layout.setCurrentIndex(n) )
##            button_layout.addWidget(btn)
##            layout.addWidget(Color(color))
##
##        widget = QWidget()
##        widget.setLayout(pagelayout)
##        self.setCentralWidget(widget)

# Using a Qt built-in TabWidget that provides the tab like interface out of the box
class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("My Awesome App")

        tabs = QTabWidget()
        tabs.setDocumentMode(True)
        tabs.setTabPosition(QTabWidget.North)
        tabs.setMovable(True)

        for n, color in enumerate(['red','green','blue','yellow']):
            tabs.addTab( Color(color), color)

        self.setCentralWidget(tabs)
        
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
