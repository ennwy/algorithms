class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canFinish(k: int) -> bool:
            hours = 0

            for p in piles:
                hours += p // k
                if p % k != 0:
                    hours += 1
                
                if hours > h:
                    return False
            return True

        l, r = 1, max(piles) + 1
        while l < r:
            m = l + (r - l) // 2

            if canFinish(m):
                r = m
            else:
                l = m + 1
        
        return l
