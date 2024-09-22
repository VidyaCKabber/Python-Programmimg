# Deleting a node from the front, from the end, after a node or before a node
class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next
        
class LinkedList:
    def __init__(self, r):
        self.root = r
        self.tail = r
        
        while self.tail and self.tail.next:
            self.tail = self.tail.next  # Ensure tail is the last node

    
    def deleteFirstNode(self):
        if not self.root:
            return
        
        # if only one node
        if self.root == self.tail:
            self.root = self.tail = None
        else: 
            self.root = self.root.next
    
    def deleteLastNode(self):
        if not self.root:
            return
        
        current = self.root
        # if only one node
        if self.root == self.tail:
            self.root = self.tail = None
        else:
            while current.next != self.tail:
                current = current.next
                
            current.next = None
            self.tail = current
    
    def deleteAfterTheNode(self, node):
        current = self.root
        
        while current and current.data != node.data:
            current = current.next
            
        if current and current.next:
            current.next = current.next.next
            if current.next is None:
                current.next = None
                self.tail = current
            
        
        
    def deleteBeforeTheNode(self, node):
        if not self.root or self.root == node.data:
            return
        
        prev = None
        current = self.root
        
        while current.next and current.next.data != node.data:
            prev = current
            current = current.next
        
        if current.next and current.next.data == node.data:
            if prev:
                prev.next = current.next
            else:
                self.root = current.next
                
                
    def print_all(self):
        current = self.root
        if not current:
            print("List is empty")
        else:
            print("Linked List:", end=" ")
            while current:
                print(current.data, end=" -> " if current.next else "\n")
                current = current.next

# Example usage:
# Create a linked list with some nodes
node1 = ListNode(10)
node2 = ListNode(20)
node3 = ListNode(30)
node4 = ListNode(0)
node5 = ListNode(3)
node6 = ListNode(7)
node7 = ListNode(67)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
# Initialize LinkedList with root node
ll = LinkedList(node1)

# Print the linked list
ll.print_all()

ll.deleteFirstNode()
ll.print_all()

ll.deleteLastNode()
ll.print_all()

ll.deleteAfterTheNode(node5)
ll.print_all()

ll.deleteBeforeTheNode(node3)
ll.print_all()
            
            
        
    
