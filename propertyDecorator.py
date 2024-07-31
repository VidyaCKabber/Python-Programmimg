class MyClass:
    def __init__(self, value):
        self.__value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

obj = MyClass(10)
print(obj.value)  # Accessing value as a property
obj.value = 20  # Modifying value as a property
print(obj.value)
