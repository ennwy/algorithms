class Solution:
    def carFleet(self, target: int, positions: List[int], speeds: List[int]) -> int:
        cars = sorted(zip(positions, speeds), reverse=True)

        fleets = 0
        maxtime = 0
        for pos, speed in cars:
            time = (target - pos) / speed

            if time > maxtime:
                fleets += 1
                maxtime = time

        return fleets





