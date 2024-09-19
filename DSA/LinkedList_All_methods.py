class Node:
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null
class LinkedList:
    def __init__(self):
        self.head = None  # Initialize head as null

    # Method to insert a new node at the end of the list
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # Method to print the entire LinkedList
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # Method to insert a node at the beginning
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Method to insert after a specific node
    def insert_after(self, prev_node_data, data):
        current = self.head
        while current and current.data != prev_node_data:
            current = current.next
        if current is None:
            print("Previous node not found.")
            return
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node

    # Method to delete a node by value
    def delete_node(self, key):
        current = self.head

        # If the node to be deleted is the head node
        if current and current.data == key:
            self.head = current.next
            current = None
            return

        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        # If the key was not found
        if current is None:
            return

        prev.next = current.next
        current = None

    # Method to search for an element
    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    # Method to reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

# Initialize the LinkedList
llist = LinkedList()

# Append nodes
llist.append(10)
llist.append(20)
llist.append(30)

# Prepend a node
llist.prepend(5)

# Insert after a node
llist.insert_after(10, 15)

# Print the list
llist.print_list()  # Output: 5 -> 10 -> 15 -> 20 -> 30 -> None

# Search for a node
print(llist.search(20))  # Output: True
print(llist.search(100))  # Output: False

# Delete a node
llist.delete_node(15)
llist.print_list()  # Output: 5 -> 10 -> 20 -> 30 -> None

# Reverse the list
llist.reverse()
llist.print_list()  # Output: 30 -> 20 -> 10 -> 5 -> None
