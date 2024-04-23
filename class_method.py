class Book:
    TYPES = ('Paperbook', "Hardcover")
    
    def __init__(self, name, book_type, pages):
        self.name = name
        self.book_type = book_type
        self.pages = pages
        
    def __repr__(self):
        return f"<Book {self.name} of {self.book_type} type has {self.pages} pages>"
        
    @classmethod
    def paperbook(cls, name, pages):
        return cls(name, cls.TYPES[0], pages)
    
    @classmethod
    def hardcover(cls, name, pages):
        return cls(name, cls.TYPES[1], pages)
    
    
a = Book.paperbook("Python 101", 100)
print(a)
