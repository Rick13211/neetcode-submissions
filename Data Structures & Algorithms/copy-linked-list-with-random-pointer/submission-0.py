"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        map = {None:None}
        temp = head
        while temp:
            map[temp] = Node(temp.val)
            temp = temp.next
        temp = head
        while temp:
            copy= map[temp]
            copy.next = map[temp.next]
            copy.random = map[temp.random]
            temp = temp.next
        return map[head]

