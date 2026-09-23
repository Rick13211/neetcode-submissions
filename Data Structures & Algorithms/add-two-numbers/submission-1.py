# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        tempHead = ListNode(-1)
        temp = tempHead
        temp1,temp2  = l1,l2
        carry = 0
        while temp1 and temp2:
            add = temp1.val+temp2.val+carry
            if add>=10:
                temp.next = ListNode(add%10)
                carry = add//10
            else:
                temp.next = ListNode(add)
                carry = 0
            temp=temp.next
            temp1 = temp1.next
            temp2 = temp2.next
        while temp1:
            add = temp1.val+carry
            if add>=10:
                temp.next = ListNode(add%10)
                carry = add//10
            else:
                temp.next = ListNode(add)
                carry = 0
            temp=temp.next
            temp1 = temp1.next
        while temp2:
            add = temp2.val+carry
            if add>=10:
                temp.next = ListNode(add%10)
                carry = add//10
            else:
                temp.next = ListNode(add)
                carry = 0
            temp=temp.next
            temp2 = temp2.next
        if carry != 0:
            temp.next = ListNode(carry)
        return tempHead.next


        