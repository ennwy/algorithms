# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        def build(preorder, inorder):
            if len(inorder) == 0:
                return None

            mid = preorder[0]
            i = inorder.index(mid)
            
            node = TreeNode(mid)
            
            node.left = build(preorder[1:i+1], inorder[:i])
            node.right = build(preorder[i+1:], inorder[i+1:])

            return node
        
        return build(preorder, inorder)

