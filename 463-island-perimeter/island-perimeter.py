class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 0:
                    continue
    
                res += y == 0 or grid[y-1][x] == 0
                res += x == 0 or grid[y][x-1] == 0
                res += y == len(grid) - 1 or grid[y+1][x] == 0
                res += x == len(grid[0]) - 1 or grid[y][x+1] == 0
                
        return res
                

