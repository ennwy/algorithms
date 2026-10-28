class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]: # nums = [1 2 3]
        result = [] # [[1 2 3] [1 2] ]

        def backtrack(index: int, path: List[int]): # index = 0, path = [1 2]
            if index == len(nums): 
                result.append(path[:])
                return
            
            path.append(nums[index]) 
            backtrack(index+1, path)

            path.pop()
            backtrack(index+1, path)
        
        backtrack(0, [])

        return result
