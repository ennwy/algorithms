class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ps = sorted(zip(position, speed))[::-1]
        fleets = 0
        prev_t = float('-inf')

        for p, s in ps:
            t = (target - p) / s

            if t > prev_t:
                fleets += 1
                prev_t = t

        return fleets
            
            
