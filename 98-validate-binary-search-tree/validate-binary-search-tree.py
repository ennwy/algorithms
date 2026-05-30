# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validateSubtree(node, minv, maxv) -> bool:
            if not node:
                return True
            
            if not (minv < node.val < maxv):
                return False
            
            return validateSubtree(node.left, minv, node.val) and validateSubtree(node.right, node.val, maxv)

        return validateSubtree(root, float('-inf'), float('inf'))

            