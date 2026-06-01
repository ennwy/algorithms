# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx = {}
        for i in range(len(inorder)):
            idx[inorder[i]] = i

        preorderq = deque(preorder)

        def build(start, end):
            if start > end:
                return None
            
            root = TreeNode(preorderq.popleft())

            mid = idx[root.val]

            root.left = build(start, mid-1)
            root.right = build(mid+1, end)

            return root
        
        return build(0, len(preorder) - 1)

        
        

