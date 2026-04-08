class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ps = sorted(zip(position, speed))[::-1]
        fleets = 0
        prev_t = None
        print(ps)

        for p, s in ps:
            t = (target - p) / s

            if not prev_t or t > prev_t:
                fleets += 1
                prev_t = t

        return fleets
            
            
