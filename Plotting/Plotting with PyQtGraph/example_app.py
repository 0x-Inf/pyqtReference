from PyQt5 import QtWidgets, QtGui, QtCore
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys # We need sys so that we can pass argv to QApplication
import os

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        hour = [1,2,3,4,5,6,7,8,9,10]
        temperature_1 = [30,32,34,32,33,31,29,32,35,45]
        temperature_2 = [50,35,44,22,38,32,27,38,32,44]

        # styling background color
##        self.graphWidget.setBackground('w')
##        self.graphWidget.setBackground('#bbccaa') #hex
##        self.graphWidget.setBackground((100,50,255)) #RGB each 0-255
##        self.graphWidget.setBackground((100,50,255,25)) # RGBA (A = alpha opacity)
##        self.graphWidget.setBackground(QtGui.QColor(100, 50, 254, 25))
        color = self.palette().color(QtGui.QPalette.Window)
        self.graphWidget.setBackground(color)

        # Line color width and style
        pen = pg.mkPen(color=(255, 0, 0), width=5, style=QtCore.Qt.DashLine)
        pen2 = pg.mkPen(color=(255,0,0), width=10, style=QtCore.Qt.DashLine)

        # line Markers
##        self.graphWidget.plot(hour, temperature, symbol='+')

        # Plot titles
##        self.graphWidget.setTitle("Your Title Here")
        self.graphWidget.setTitle("Your Title Here", color="b", size="30pt")
##        self.graphWidget.setTitle("<span style=\"color:blue;font-size:30pt\">Your Title Here</span>")

        # Axis Labels
##        styles = {"color":"#f00", "font-size": "20px"}
##        self.graphWidget.setLabel('left', 'Temperature (°C)', **styles)
##        self.graphWidget.setLabel('bottom', 'Hour (H)', **styles)
        # also supports HTML syntax
        self.graphWidget.setLabel('left', "<span style=\"color:red;font-size:20px\">Temperature (°C)</span>")
        self.graphWidget.setLabel('bottom', "<span style=\"color:red;font-size:20px\">Hour (H)</span>")

        #legend
        self.graphWidget.addLegend()
        
        #Background Grid
        self.graphWidget.showGrid(x=True, y=True)

        # Setting Axis Limits
        self.graphWidget.setXRange(0, 10, padding=0)
        self.graphWidget.setYRange(20, 55, padding=0)
        
        # Plot data: x, y values
        self.plot(hour, temperature_1, "Sensor 1", 'r')
        self.plot(hour, temperature_2, "Sensor2" , 'b')


    def plot(self, x, y, plotname, color):
        pen = pg.mkPen(color=color)
        self.graphWidget.plot(x, y, name=plotname, pen=pen, symbol='+', symbolSize=30, symbolBrush=(color))


        
def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
