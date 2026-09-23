# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        tempHead = ListNode(None, None)
        temp = tempHead
        temp1 = list1
        temp2 = list2
        while temp1 and temp2:
            val1 = temp1.val
            val2 = temp2.val
            if val1<=val2:
                temp.next = temp1
                temp1 = temp1.next
            else:
                temp.next = temp2
                temp2 = temp2.next
            temp = temp.next
        while temp1:
            temp.next = temp1
            temp1 = temp1.next
            temp = temp.next
        while temp2:
            temp.next = temp2
            temp2  = temp2.next
            temp = temp.next
        return tempHead.next
        