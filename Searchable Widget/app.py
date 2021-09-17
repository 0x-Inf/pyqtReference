from PyQt5 import QtWidgets, uic
import sys
from PyQt5.QtWidgets import (
    QMainWindow, QApplication, QWidget, QVBoxLayout,QWidget, QLineEdit,
    QLabel, QPushButton, QScrollArea,QHBoxLayout,QSpacerItem,QSizePolicy,
    QCompleter
    )
from PyQt5.QtCore import QObject, Qt, pyqtSignal
from PyQt5.QtGui import QPainter, QFont, QColor, QPen

from customwidgets import OnOffWidget

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.controls = QWidget() # Controls container widget
        self.controlsLayout = QVBoxLayout() # Controls container layout
        # List of names, widgets are stored in a dictionary by these keys.
        widget_names = [
            "Heater", "Stove", "Living Room Light", "Balcony Light",
            "Fan", "Room Light", "Oven", "Desk Light",
            "Bedroom Heater", "Wall Switch"
            ]
        self.widgets = []

        # Iterate the names, creating a new OfOffwidget for each one,
        # adding it it the Layout and storing a reference in the se;f.widgets List
        for name in widget_names:
            item = OnOffWidget(name)
            self.controlsLayout.addWidget(item)
            self.widgets.append(item)

        spacer = QSpacerItem(1, 1, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.controlsLayout.addItem(spacer)
        self.controls.setLayout(self.controlsLayout)

        # Scroll Area Properties
        self.scroll = QScrollArea()
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.controls)

        # Search bar.
        self.searchbar = QLineEdit()
        self.searchbar.textChanged.connect(self.update_display)

        #Adding Completer
        self.completer = QCompleter(widget_names)
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.searchbar.setCompleter(self.completer)

        # Add the items to VBoxLayout (applied to container widget)
        # which encompasses to the whole window
        container = QWidget()
        containerLayout = QVBoxLayout()
        containerLayout.addWidget(self.searchbar)
        containerLayout.addWidget(self.scroll)
        
        container.setLayout(containerLayout)
        self.setCentralWidget(container)

        self.setGeometry(600, 100, 800,600)
        self.setWindowTitle('Control Panel')

    def update_display(self, text):

        for widget in self.widgets:
            if text.lower() in widget.name.lower():
                widget.show()
            else:
                widget.hide()


app = QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())

        
