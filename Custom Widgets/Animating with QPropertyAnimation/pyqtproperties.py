from PyQt5.QtCore import pyqtProperty, QObject, pyqtSignal

class CustomObject(QObject):
    def __init__(self):
        super().__init__()
        self._value = 0   # the default value

    @pyqtProperty(int)
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


obj = CustomObject()
obj.value = 7
print(obj.value)


"""
    Emitting signals when certain attributes are changed using getter/setter methods
"""

class CustomObjectS(QObject):

    valueChanged = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self._value = 0  # the default value

    @pyqtProperty(int)
    def value(self):
        return self._value

    # change the setter function to be as:
    @value.setter
    def value(self, value):
        # here, the check is very important..
        # to prevent unneeded signal being propagated
        if value != self._value:
            self._value = value
            self.valueChanged.emit(value)


obj = CustomObjectS()
obj.value = 7
print(obj.value)







