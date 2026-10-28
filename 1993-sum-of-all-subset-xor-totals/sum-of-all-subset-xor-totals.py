class Solution:
    def subsetXORSum(self, nums: list[int]) -> int: # num = [1, 3]
        total = 0 # (3) + (1) + (2)

        def backtrack(index, curr_sum): # index = 0, curr_sum = 0
            if index == len(nums):
                nonlocal total
                total += curr_sum
                return
            
            backtrack(index+1, curr_sum)

            curr_sum = curr_sum ^ nums[index]
            backtrack(index+1, curr_sum)

        backtrack(0, 0)

        return total