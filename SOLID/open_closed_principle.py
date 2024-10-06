# Software entities (classes, modules, functions) should be open for extension but closed for modification. 
# This means that you should be able to add new functionality without changing existing code.
# Example: Use interfaces or abstract classes to define behavior, and then implement new classes for different behavior instead of modifying existing ones.

# Bad example
class Shape:
    def area(self, shape_type):
        if shape_type == "circle":
            return 3.14 * radius ** 2
        elif shape_type == "square":
            return side ** 2

# Good example (Extend functionality by adding new classes)
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2
