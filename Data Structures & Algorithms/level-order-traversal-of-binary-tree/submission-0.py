# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        curr_list = []
        curr_level = 0
        queue =  [(root, 0)]
        if not root:
            return []
        

        while queue:
            node, level = queue.pop(0)
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
            if level ==  curr_level:
                curr_list.append(node.val)
            else:
                curr_level = level
                ans.append(curr_list)
                curr_list = [node.val]
        ans.append(curr_list)
        return ans        