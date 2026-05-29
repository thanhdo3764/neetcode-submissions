# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        cur = None if not head else head.next
        if prev: prev.next = None
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev



        