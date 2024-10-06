# Clients should not be forced to depend on methods they don't use.

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
