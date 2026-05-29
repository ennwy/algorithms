# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = None

        def found(node: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> bool: # node = 3, p = 5, q = 1
            if not node:
                return False
  
            left = found(node.left, p, q)
            right = found(node.right, p, q)

            curr = (node == p or node == q)

            if (left and right) or ((left or right) and curr):
                nonlocal res
                res = node
                return True
            
            return left or right or curr
        
        found(root, p, q)

        return res

        
            