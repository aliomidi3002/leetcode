# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        left = list1
        right = list2

        if left is None and right is None:
            return None

        sorted_array = ListNode()
        current = sorted_array

        while left is not None and right is not None:
            if left.val < right.val:
                current.next = left
                left = left.next
            else :
                current.next = right
                right = right.next
            current = current.next


        while left is not None:
            current.next = left
            left = left.next
            current = current.next


        while right is not None:
            current.next = right
            right = right.next
            current = current.next
                
        return sorted_array.next