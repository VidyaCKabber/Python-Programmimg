class Node:
    def __init__(self, d, n=None):
        self.data = d
        self.next = n
        
    def get_data(self):
        return self.data
        
    def set_data(self, d):
        self.data = d
        
    def get_next(self):
        return self.next
        
    def set_next(self, n):
        self.next = n
        
        
class LinkedList:
    def __init__(self, r=None):
        self.root = r
        self.tail = r
        self.size = 0
        
    def insertFirst(self, d):
        this_node = Node(d, self.root)
        self.root = this_node
        
        if self.size == 0:
            self.tail = this_node   
        self.size +=1
        
    def insertLast(self, d):
        new_node = Node(d)
        
        if not self.root:
            self.root = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node
        self.size += 1   
        
    def deleteFirst(self):
        if self.root:
            self.root = self.root.get_next()
            self.size -= 1 
            if self.size == 0:
                self.tail = None
            return True
        return False
                
    def deleteLast(self):
        this_node = self.root
        
        while this_node.get_next() != self.tail:
            this_node = this_node.get_next()
        
        this_node.set_next(None)
        self.tail = this_node
        self.size -= 1
        return True
        
    def remove(self, d):
        this_node = self.root
        prev_node = None
        
        while this_node:
            if this_node.get_data() == d:
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node.get_next()
                    
                if this_node == self.tail:
                    self.tail = prev_node
                self.size -=1
                return True
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False
        
        
    def find(self, d):
        this_node = self.root
        
        while this_node:
            if this_node.get_data() == d:
                return d
            else:
                this_node = this_node.get_next()
        return None
        
    def printAll(self):
        this_node = self.root
        
        while this_node:
            print(this_node.get_data(), end="->")
            this_node = this_node.get_next()

ll = LinkedList()
ll.insertFirst(5)
ll.insertLast(8)
ll.insertFirst(12)
ll.printAll()
ll.deleteFirst()
print(ll.remove(8))
ll.printAll()

        
