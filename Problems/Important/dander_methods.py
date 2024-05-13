class Match:
    def __repr__(self):
       return "__repr__ is called"

    def __str__(self):
        return "__str__ is called"
    
    def __len__(self):
        return len("Vidya")

test = Match()
print(test)
print(len(test))
print(repr(test))
