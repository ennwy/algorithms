class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        # [4,5,6,7,0,1,2]
        #. l     m     r
        # 
        # l = 0
        # r = 6
        # m = 3
        # target = 6
        #   

        while l <= r:
            m = l + (r - l) // 2

            if nums[m] == target:
                return m
            elif nums[l] <= nums[m]:
                if nums[l] <= target <= nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[r] >= target >= nums[m]:
                    l = m + 1
                else:
                    r = m - 1

        return -1
