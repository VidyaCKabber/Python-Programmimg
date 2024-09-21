# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        slow = head 
        fast = head

        # Move the slow pointer to the middle node
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Return the middle node (slow pointer)
        return slow

# Helper function to print the linked list from a given node
def print_linked_list(node: Optional[ListNode]):
    current = node
    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next
    print()  # New line for better formatting

# Creating a linked list manually:
# Let's say the linked list is: 1 -> 2 -> 3 -> 4 -> 5

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

# Linking nodes together to form: 1 -> 2 -> 3 -> 4 -> 5
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# Head of the linked list is node1
head = node1

# Create a Solution object and call the middleNode method
solution = Solution()
middle = solution.middleNode(head)

# Print the linked list starting from the middle node
print_linked_list(middle)
