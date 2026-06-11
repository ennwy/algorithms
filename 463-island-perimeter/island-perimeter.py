class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x]:
                    res += 4

                    if y and grid[y-1][x]:
                        res -= 2
                    if x and grid[y][x-1]:
                        res -= 2
                
        return res
                

