import sys
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        colors = ['#053061', '#2166ac', '#4393c3', '#92c5de', '#d1e5f0', '#f7f7f7', '#fddbc7', '#f4a582', '#d6604d', '#b2182b', '#67001f']
        if role == Qt.DisplayRole:
            # Get the raw value
            value = self._data[index.row()][index.column()]

            # Perform per-type checks and render accordingly
            if isinstance(value, datetime):
                # Render time to YYY-MM-DD
                return value.strftime("%Y-%m-%d")

            if isinstance(value, float):
                # Render float to 2 dp
                return "%.2f" % value

            if isinstance(value, str):
                # Render strings with quotes
                return '"%s"' % value

            # Default (anything no captured above: e.g. int)
            return value

        if role == Qt.DecorationRole:
            value = self._data[index.row()][index.column()]
            if isinstance(value, datetime):
                return QtGui.QIcon('calendar.png')

            # ticks and crosses for `bool` values
            if isinstance(value, bool):
                if value:
                    return QtGui.QIcon('tick.png')
                return QtGui.QIcon('cross.png')

            # color blocks
            if (isinstance(value, int) or isinstance(value, float)):
                value = int(value)

                value = max(-5, value) # values < -5 become -5
                value = min(5, value) # values > +5 become +5
                value = value + 5 # -5 become 0 and +5 becomes 10

                return QtGui.QColor(colors[value])

##        if role == Qt.BackgroundRole and index.column() == 2:
##            # See below for the data structure
##            return QtGui.QColor('blue')
        if role == Qt.TextAlignmentRole:
            value = self._data[index.row()][index.column()]

            if isinstance(value, int) or isinstance(value, float):
                return Qt.AlignVCenter + Qt.AlignRight

        if role == Qt.ForegroundRole:
            value = self._data[index.row()][index.column()]

            if(
                (isinstance(value, int) or isinstance(value, float))
                and value < 0
            ):
                return QtGui.QColor('red')

##        if role == Qt.BackgroundRole:
##            value = self._data[index.row()][index.column()]
##            if (isinstance(value, int) or isinstance(value, float)):
##                value = int(value) # convert to integer for indexing
##
##                # Limit to range -5 ... +5, then convert to 0..10
##                value = max(-5, value) # values < -5 become -5
##                value = min(5, value) # values > +5 become +5
##                value = value + 5 # -5 become 0 and +5 becomes 10
##
##                return QtGui.QColor(colors[value])

    def rowCount(self, index):
        # The length of the outer list
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.table = QtWidgets.QTableView()

        data = [
            [True, 9, 2],
            [1, 0, -1],
            [3, 5, False],
            [3, 3, 2],
            [datetime(2019,5,4), 8, 9],
        ]

        self.model = TableModel(data)
        
        self.table.setModel(self.model)

        self.setCentralWidget(self.table)



app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()






