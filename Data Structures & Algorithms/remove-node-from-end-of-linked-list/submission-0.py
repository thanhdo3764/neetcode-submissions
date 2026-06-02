# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr = dummy
        lookahead = head
        for i in range(n):
            lookahead = lookahead.next
        
        while lookahead:
            curr = curr.next
            lookahead = lookahead.next
        
        curr.next = curr.next.next
        return dummy.next