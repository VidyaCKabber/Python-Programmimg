class C:
    def __init__(self):
        self.__a = 2
    
    # def set_a(self, a):
    #     self.a = a
        
    @property
    def a(self):
        return self.__a
        
    # @a.setter
    # def a(self, i):
    #     self.__a = i
        


c_instance = C()
# Call the method that shows variables from A and B
c_instance.a = 8
print(c_instance.a)
# AttributeError: property 'a' of 'C' object has no setter

