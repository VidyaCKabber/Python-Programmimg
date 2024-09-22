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

    
    def removeNegativeNodes(self):
        if self.root.data < 0:
            self.root = self.root.next
            
        current = self.root
        
        while current and current.next:
            if current.next.data < 0:
                if current.next.next is None:
                    current.next =None
                    self.tail = current
                else:
                    current.next = current.next.next
            else:
                current = current.next
                
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
node1 = ListNode(-10)
node2 = ListNode(20)
node3 = ListNode(30)
node4 = ListNode(0)
node5 = ListNode(-3)
node6 = ListNode(7)
node7 = ListNode(-67)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
# Initialize LinkedList with root node
ll = LinkedList(node1)

# # Print the linked list
# ll.print_all()

ll.removeNegativeNodes()
ll.print_all()

