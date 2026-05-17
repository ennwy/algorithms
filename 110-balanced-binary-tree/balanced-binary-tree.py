# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True

        def depth(node) -> int:
            if not node:
                return 0
            
            l = depth(node.left)
            r = depth(node.right)

            if abs(l - r) > 1:
                nonlocal res
                res = False

            return 1 + max(l, r)
        
        depth(root)

        return res