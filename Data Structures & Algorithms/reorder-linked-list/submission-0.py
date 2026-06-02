# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head.next
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        right_half = slow.next
        prev = None
        slow.next = None
        # Reverse right half
        while right_half:
            temp = right_half.next
            right_half.next = prev
            prev = right_half
            right_half = temp
        
        # Zip it up
        left_half = head
        right_half = prev
        while right_half:
            temp1 = left_half.next
            temp2 = right_half.next
            left_half.next = right_half
            right_half.next = temp1
            left_half = temp1
            right_half = temp2
        print(slow.val)