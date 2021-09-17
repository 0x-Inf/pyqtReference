from PyQt5.QtWidgets import QWidget, QGraphicsOpacityEffect, QApplication
from PyQt5.QtCore import QPropertyAnimation, QParallelAnimationGroup, QPoint
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(600,600)
        self.child = QWidget(self)
        effect = QGraphicsOpacityEffect(self.child)
        self.child.setGraphicsEffect(effect)
        self.child.setStyleSheet("background-color:red;border-radius:15px;")
        self.child.resize(100,100)
        self.anim = QPropertyAnimation(self.child, b"pos")
        self.anim.setEndValue(QPoint(200,200))
        self.anim.setDuration(1500)
        self.anim_2 = QPropertyAnimation(effect, b"opacity")
        self.anim_2.setStartValue(0)
        self.anim_2.setEndValue(1)
        self.anim_2.setDuration(2500)
        self.anim_group = QParallelAnimationGroup()
        self.anim_group.addAnimation(self.anim)
        self.anim_group.addAnimation(self.anim_2)
        self.anim_group.start()


app = QApplication(sys.argv)
window = Window()
window.show()
app.exec_()




