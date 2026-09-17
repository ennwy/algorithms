class Solution:
    def carFleet(self, target: int, positions: List[int], speeds: List[int]) -> int:
        cars = sorted(zip(positions, speeds), reverse=True)

        fleets = 0
        prevtime = -1
        for pos, speed in cars:
            time = (target - pos) / speed

            if time > prevtime:
                fleets += 1
                prevtime = time

        return fleets





