# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp  = head
        length = 0
        while temp:
            length+=1
            temp = temp.next
        if n == length:
            return head.next
        count = length - n-1
        temp = head
        while count>=1:
            count -=1
            temp = temp.next
        temp.next = temp.next.next
        return head