class Solution:
    def subsetXORSum(self, nums: list[int]) -> int: # num = [1, 3]
        def backtrack(index, xor): # index = 0, curr_sum = 0
            if index == len(nums):
                return xor
            
            return backtrack(index+1, xor) + backtrack(index+1, xor ^ nums[index])

        

        return backtrack(0, 0)