1. Single Responsibility Principle (SRP)
A class should have only one reason to change, meaning it should have only one job.

python
Copy code
# Bad example
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_payroll(self):
        return self.salary

    def generate_report(self):
        return f"Employee Report for {self.name}"

# Good example (Separate responsibilities into different classes)
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Payroll:
    def calculate_payroll(self, employee):
        return employee.salary

class Report:
    def generate_report(self, employee):
        return f"Employee Report for {employee.name}"
2. Open/Closed Principle (OCP)
Classes should be open for extension but closed for modification.

python
Copy code
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
3. Liskov Substitution Principle (LSP)
Objects of a subclass should be replaceable with objects of the superclass without altering the behavior.

python
Copy code
# Bad example
class Bird:
    def fly(self):
        print("Flying")

class Penguin(Bird):
    def fly(self):
        raise Exception("Penguins can't fly")

# Good example
class Bird(ABC):
    @abstractmethod
    def move(self):
        pass

class Sparrow(Bird):
    def move(self):
        print("Flying")

class Penguin(Bird):
    def move(self):
        print("Swimming")
4. Interface Segregation Principle (ISP)
Clients should not be forced to depend on methods they don't use.

python
Copy code
# Bad example
class Worker:
    def work(self):
        pass

    def eat(self):
        pass

class Robot(Worker):
    def work(self):
        print("Robot is working")

    def eat(self):
        raise NotImplementedError("Robot can't eat")

# Good example
class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass

class Human(Workable, Eatable):
    def work(self):
        print("Human is working")

    def eat(self):
        print("Human is eating")

class Robot(Workable):
    def work(self):
        print("Robot is working")
5. Dependency Inversion Principle (DIP)
High-level modules should not depend on low-level modules. Both should depend on abstractions.

python
Copy code
# Bad example
class BackendDeveloper:
    def write_code(self):
        return "Writing Python code"

class FrontendDeveloper:
    def write_code(self):
        return "Writing JavaScript code"

class Project:
    def __init__(self):
        self.backend = BackendDeveloper()
        self.frontend = FrontendDeveloper()

    def develop(self):
        return f"{self.backend.write_code()} and {self.frontend.write_code()}"

# Good example (Depend on abstractions, not concretions)
class Developer(ABC):
    @abstractmethod
    def write_code(self):
        pass

class BackendDeveloper(Developer):
    def write_code(self):
        return "Writing Python code"

class FrontendDeveloper(Developer):
    def write_code(self):
        return "Writing JavaScript code"

class Project:
    def __init__(self, developers):
        self.developers = developers

    def develop(self):
        return " and ".join([dev.write_code() for dev in self.developers])

# Usage
backend = BackendDeveloper()
frontend = FrontendDeveloper()
project = Project([backend, frontend])
print(project.develop())
These examples show how SOLID principles help keep code organized, scalable, and easy to maintain.






You said:
oops concepts
ChatGPT said:
ChatGPT
Here are the main Object-Oriented Programming (OOP) concepts with simple Python examples:

1. Encapsulation
Encapsulation is the bundling of data (attributes) and methods (functions) into a single unit or class. It also restricts direct access to some of an object’s components, which is known as data hiding.

python
Copy code
class Employee:
    def __init__(self, name, salary):
        self.name = name          # public attribute
        self.__salary = salary     # private attribute (name mangling with __)

    def get_salary(self):          # Getter method
        return self.__salary

    def set_salary(self, salary):  # Setter method
        self.__salary = salary

# Usage
emp = Employee("Alice", 50000)
print(emp.name)        # Accessible
print(emp.get_salary())  # Accessing private attribute through getter method
2. Inheritance
Inheritance is a mechanism where a class (child class) inherits attributes and behaviors (methods) from another class (parent class).

python
Copy code
class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):  # Dog class inherits from Animal
    def speak(self):
        return "Dog barks"

# Usage
dog = Dog()
print(dog.speak())  # Output: Dog barks (overrides parent method)
3. Polymorphism
Polymorphism means "many forms" and allows objects of different classes to be treated as objects of a common superclass. It allows the same method to be used in different ways.

Example of Polymorphism with Method Overriding:
python
Copy code
class Bird:
    def fly(self):
        print("Birds can fly")

class Penguin(Bird):
    def fly(self):
        print("Penguins cannot fly")

# Usage
bird = Bird()
penguin = Penguin()

bird.fly()     # Output: Birds can fly
penguin.fly()  # Output: Penguins cannot fly
Example of Polymorphism with Function:
python
Copy code
class Dog:
    def sound(self):
        return "Bark"

class Cat:
    def sound(self):
        return "Meow"

# Function that takes different objects
def animal_sound(animal):
    print(animal.sound())

dog = Dog()
cat = Cat()

animal_sound(dog)  # Output: Bark
animal_sound(cat)  # Output: Meow
4. Abstraction
Abstraction hides the complexity of the system and shows only the essential features of an object. In Python, abstraction is achieved by using abstract classes and abstract methods.

python
Copy code
from abc import ABC, abstractmethod

class Shape(ABC):  # Abstract class
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

# Usage
circle = Circle(5)
square = Square(4)

print(circle.area())  # Output: 78.5
print(square.area())  # Output: 16
5. Association
Association defines a relationship between two unrelated classes where one class uses another. It can be one-to-one, one-to-many, or many-to-many.

python
Copy code
class Author:
    def __init__(self, name):
        self.name = name

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author  # Association with Author class

# Usage
author = Author("George Orwell")
book = Book("1984", author)

print(f"'{book.title}' by {book.author.name}")  # Output: '1984' by George Orwell
6. Composition
Composition is a strong form of association where the composed object (child) cannot exist independently without the parent object.

python
Copy code
class Engine:
    def __init__(self, power):
        self.power = power

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.engine = Engine(150)  # Car has an engine (composition)

# Usage
car = Car("Toyota", "Corolla")
print(car.engine.power)  # Output: 150
7. Aggregation
Aggregation is a weaker form of association where the child object can exist independently of the parent.

python
Copy code
class Department:
    def __init__(self, name):
        self.name = name

class Employee:
    def __init__(self, name, department):
        self.name = name
        self.department = department  # Aggregation

# Usage
dept = Department("HR")
emp = Employee("Alice", dept)

print(f"{emp.name} works in {emp.department.name} department")  # Output: Alice works in HR department
Summary
Encapsulation: Bundles data and methods, restricts access.
Inheritance: Enables class reusability.
Polymorphism: Allows one method to have multiple forms.
Abstraction: Hides complexity, shows essential features.
Association: A relationship between two unrelated classes.
Composition: Strong association, dependent relationship.
Aggregation: Weak association, independent relationship.
