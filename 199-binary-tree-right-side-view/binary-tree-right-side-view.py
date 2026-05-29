# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        view = []
        maxdepth = 0

        def rightTraverse(node: Optional[TreeNode], depth) -> int:
            if not node:
                return
            
            nonlocal maxdepth
            if depth > maxdepth:
                nonlocal view
                view.append(node.val)
                maxdepth = depth
            
            rightTraverse(node.right, depth+1)
            rightTraverse(node.left, depth+1)
        
        rightTraverse(root, 1)
        
        return view


        


