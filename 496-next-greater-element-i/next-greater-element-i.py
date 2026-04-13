class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        ng = {}

        for n in nums2:
            while stack and stack[-1] < n:
                ng[stack.pop()] = n
            stack.append(n)
        
        res = []
        for n in nums1:
            res.append(ng.get(n, -1))
        
        return res