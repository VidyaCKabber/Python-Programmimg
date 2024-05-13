class Match:
    def __init__(self, a, b):
       self.a = a
       self.b = b

    def __str__(self):
        return 1
    
    def __eq__(self, other):
        return self.a * self.b == other.a * other.b

test = Match(4, 5)
test_1 = Match(5, 4)
print(test == test_1)
