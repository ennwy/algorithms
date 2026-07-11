class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        
        scur = 0
        for i in range(len(nums)):
            if scur == s - scur - nums[i]:
                return i
            scur += nums[i]

        return -1