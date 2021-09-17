import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton
from PyQt5.uic import loadUi

class Window(QMainWindow):

    def __init__(self, parent=None):

        super().__init__(parent)
        self.centralWidget = QPushButton("Employee...")

        self.centralWidget.clicked.connect(self.onEmployeeBtnClicked)
        self.setCentralWidget(self.centralWidget)

    def onEmployeeBtnClicked(self):
        dlg = EmployeeDlg(self)
        dlg.exec()


class EmployeeDlg(QDialog):
    """"Employee Dialog"""
    def __init__(self, parent=None):
        super().__init__(parent)
        # Load thr dialog's GUI
        loadUi("employee.ui", self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
        
        
