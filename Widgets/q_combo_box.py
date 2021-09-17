from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("My Awesome App")

        widget = QComboBox()
        widget.addItems(["One", "Two", "Three"])

##        #Making the box editable
##        widget.setEditable(True)
##
##        #To use insert rules, apply the flag as follows
##        widget.setInsertPolicy(QComboBox.InsertAlphabetically)
##
##        #You can also limit the number of items allowed in the box
##        widget.setMaxCount(10)

        # The default signal from currentIndexChanged sends the index
        widget.currentIndexChanged.connect( self.index_changed )

        #The same signal can send a text string
        widget.currentIndexChanged[str].connect( self.text_changed )

        self.setCentralWidget(widget)

    def index_changed(self, i): # i is an int
        print(i)

    def text_changed(self, s): # s is a str
        print(s)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
