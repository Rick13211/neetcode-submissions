# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        t1, t2 = head,head
        while t2 and t2.next:
            t1 = t1.next
            t2 = t2.next.next
            if t1==t2:
                return True
        return False