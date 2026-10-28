# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        position = {value: i for i, value in enumerate(inorder)}
        p_idx = 0

        def build(left, right):
            nonlocal p_idx
            if left > right:
                return

            root_val = preorder[p_idx]
            p_idx += 1

            mid = position[root_val]
            node = TreeNode(root_val)
            
            node.left = build(left, mid-1)
            node.right = build(mid+1, right)

            return node
        
        return build(0, len(inorder) - 1)

