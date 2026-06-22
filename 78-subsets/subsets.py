class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def backtrack(i: int):
            if i == len(nums):
                res.append(subset[:])   # копія! не сам subset
                return

            # вибір 1: взяти nums[i]
            subset.append(nums[i])
            backtrack(i + 1)

            # відкат: прибрати nums[i]
            subset.pop()

            # вибір 2: не брати nums[i]
            backtrack(i + 1)

        backtrack(0)
        return res