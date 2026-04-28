class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextg = dict()
        stack = []

        for n in nums2:
            while stack and n > stack[-1]:
                nextg[stack.pop()] = n
            stack.append(n)

        res = []
        for n in nums1:
            res.append(nextg.get(n, -1))
        
        return res