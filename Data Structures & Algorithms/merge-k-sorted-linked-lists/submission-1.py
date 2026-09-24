# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:   
    def merge2Lists(self , list1, list2):
        if list1 is None:
            return list2
        dummyHead = ListNode(-1)
        temp = dummyHead
        temp1 = list1
        temp2 = list2
        while temp1 and temp2:
            val1 = temp1.val
            val2 = temp2.val
            if val1<=val2: 
                temp.next = ListNode(val1)
                temp=temp.next
                temp1= temp1.next
            else:
                temp.next = ListNode(val2)
                temp = temp.next
                temp2 = temp2.next
        while temp1:
            val1 = temp1.val
            temp.next = ListNode(val1)
            temp=temp.next
            temp1= temp1.next
        while temp2:
            val2 = temp2.val
            temp.next = ListNode(val2)
            temp = temp.next
            temp2 = temp2.next
        return dummyHead.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists)==0:
            return None
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.merge2Lists(l1, l2))
            lists = mergedLists
            
        return lists[0]
        