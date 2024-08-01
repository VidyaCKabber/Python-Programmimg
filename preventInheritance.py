class NoInheritanceMeta(type):
    def __new__(cls, name, bases, attrs):
        for base in bases:
            if isinstance(base, NoInheritanceMeta):
                raise TypeError(f"Cannot inherit from class {base.__name__}")
        return super().__new__(cls, name, bases, attrs)
        

class BaseClass(metaclass=NoInheritanceMeta):
    pass


class DerivedClass(BaseClass):
    pass

DerivedClass()
