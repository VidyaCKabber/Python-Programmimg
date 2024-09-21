# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head

        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next

        return head

# Helper function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print the linked list
def print_linked_list(head):
    current = head
    values = []
    while current:
        values.append(current.val)
        current = current.next
    print(" -> ".join(map(str, values)))

# Example input
input_values = [1, 1, 2, 3, 3]  # Sorted linked list with duplicates
head = create_linked_list(input_values)

# Create a Solution object and call the deleteDuplicates method
solution = Solution()
print("Original linked list:")
print_linked_list(head)

# Remove duplicates
head = solution.deleteDuplicates(head)

# Print the modified linked list
print("Linked list after removing duplicates:")
print_linked_list(head)
