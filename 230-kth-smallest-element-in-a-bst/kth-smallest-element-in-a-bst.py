# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = 0
        counter = 0

        def inorder(node: Optional[TreeNode]): # node = 2, 1
            if not node: 
                return

            inorder(node.left)

            nonlocal counter
            
            counter += 1
            if counter == k:
                nonlocal res
                res = node.val
            
            inorder(node.right)

        inorder(root)

        return res


            


        