"""Defining python properties"""

# Using a decorator
class MyCustomClass:

    def __init__(self):
        self._value = None

    @property
    def value(self):
        print("getting the value", self._value)
        return self._value

    @value.setter
    def value(self, value):
        print("setting the value", value)
        self._value = value


obj = MyCustomClass()

a = obj.value
print(a)
obj.value = 'hello'
b = obj.value
print(b)

# using a function

class MyCustomClassB:

    def __init__(self):
        self._value = None

    def getValue(self):
        print("getting the value", self._value)
        return self._value

    def setValue(self, value):
        print("setting the value", value)
        self._value = value

    value = property(getValue, setValue )


obj2 = MyCustomClassB()

c = obj2.value
print(c)
obj2.value = 'hello'
d = obj2.value
print(d)



    
