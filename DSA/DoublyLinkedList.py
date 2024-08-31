class Node:
    def __init__(self, d):
        self.data = d
        self.next = None
        self.prev = None
        
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def append(self, d):
        new_node = Node(d)
        
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size +=1
    
    def prepend(self, d):
        new_node = Node(d)
        
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size +=1    
        
    def delete(self, d):
        if not self.head:
            return False
            
        current = self.head
        
        while current:
            if current.data == d:
                if current == self.head:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                elif current == self.tail:
                    self.tail = current.prev
                    if self.tail:
                        self.tail.next = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                self.size -=1
                return True
            else:
                current = current.next
        return False
        
    def displayForward(self):
        current = self.head
        
        while current:
            print(current.data, end="<->")
            current = current.next
        print("None")
        
    def displayBackward(self):
        current = self.tail
        
        while current:
            print(current.data, end="<->")
            current = current.prev
        print("None")
        
# Example usage
dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.prepend(0)

print("Forward:")
dll.displayForward()

print("Backward:")
dll.displayBackward()

dll.delete(2)
dll.delete(0)

print("After deletion:")
dll.displayForward()
