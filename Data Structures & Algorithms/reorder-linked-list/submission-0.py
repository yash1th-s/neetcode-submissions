# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        first = head
        slow.next = None

        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        second = prev

        while second:
            tmp1 = first.next
            first.next = second
            tmp2 = second.next 
            second.next = tmp1
            second = tmp2
            first = tmp1
        
