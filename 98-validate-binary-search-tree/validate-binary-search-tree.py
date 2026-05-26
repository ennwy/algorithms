# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, minv, maxv) -> bool:
            if not node:
                return True
            if node.val <= minv or node.val >= maxv:
                return False
            
            return valid(node.left, minv, node.val) & valid(node.right, node.val, maxv)

        return valid(root, float('-inf'), float('inf'))

            