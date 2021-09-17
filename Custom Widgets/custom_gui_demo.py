from PyQt5 import QtCore, QtGui, QtWidgets
from power_bar import PowerBar

rainbow_colors = ["#5e4fa2", "#3288bd", "#66c2a5", "#abdda4",
                  "#e6f598", "#ffffbf", "#fee08b", "#fdae61",
                  "#f46d43", "#d53e4f", "#9e0142"]

synth_vibe = ["#49006a", "#7a0177", "#ae017e", "#dd3497", "#f768a1", "#fa9fb5",
              "#fcc5c0", "#fde0dd", "#fff7f3"]

app = QtWidgets.QApplication([])
bar = PowerBar(synth_vibe)
bar.setBarPadding(5)
bar.setBarSolidPercent(0.4)
bar.setBackgroundColor('red')
bar.show()
app.exec_()
