# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None: return []
        res = list()
        queue = [root]
        while queue:
            nodes_in_level = []
            while queue:
                nodes_in_level.append(queue.pop(0))
            res.append([n.val for n in nodes_in_level])
            for n in nodes_in_level:
                if n.left: queue.append(n.left)
                if n.right: queue.append(n.right)
        
        return res

        