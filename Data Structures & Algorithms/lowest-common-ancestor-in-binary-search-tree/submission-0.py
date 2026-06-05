# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ancestors = list()
        cur = root
        while True:
            ancestors.append(cur.val)
            if p.val == cur.val:
                return p
            elif q.val == cur.val:
                return q
            elif p.val < cur.val:
                if q.val > cur.val:
                    return cur
                cur = cur.left
            else:
                if q.val < cur.val:
                    return cur
                cur = cur.right
        