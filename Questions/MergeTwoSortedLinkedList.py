# Merge Two Sorted Lists
# Problem: Merge two sorted linked lists and return it as a new sorted list.
# Example:
# Input: l1 = [1,2,4], l2 = [1,3,4]
# Output: [1,1,2,3,4,4]


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MergeTwoList:
    def mergeSortedList(self, l1 : ListNode, l2 : ListNode) -> ListNode:
        dummy = ListNode()
        curr = dummy

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next

            curr = curr.next
        
        if l1:
            curr.next = l1
    
        if l2:
            curr.next = l2
    
        return dummy.next


    def listToLinkedList(self, lst):
        dummy = ListNode()
        curr = dummy

        for val in lst:
            curr.next = ListNode(val)
            curr = curr.next

        return dummy.next
    
    def linkedListToList(self, ll: ListNode):
        result = []
        head = ll
        curr = head

        while curr:
            result.append(curr.val)
            curr = curr.next
        return result


l1 = [1,2,4]
l2 = [1,3,4]

obj = MergeTwoList()
lst_1 = obj.listToLinkedList(l1)
lst_2 = obj.listToLinkedList(l1)

out = obj.mergeSortedList(lst_1, lst_2)
res = obj.linkedListToList(out)
print(res)



