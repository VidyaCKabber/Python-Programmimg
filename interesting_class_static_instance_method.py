
class Animal():

    def __init__(self):
        pass
    @classmethod
    def sound(cls):
         return "ad!"

print(Animal.sound())  # Output: ad!


class Animal1():

    def __init__(self):
        pass
    @staticmethod
    def sound():
         return "ad!"

print(Animal1.sound())  # Output: ad!


class Animal2():

    def __init__(self):
        pass
    def sound(self):
         return "ad!"

print(Animal2.sound())  # TypeError: Animal2.sound() missing 1 required positional argument: 'self'

#fix

class Animal2():

    def __init__(self):
        pass
    def sound(self):
         return "ad!"
a = Animal2()
print(Animal2.sound(a))
