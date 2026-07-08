class Solution:
    def maxAreaOfIsland(self, grid: List[List[str]]) -> int:
        visited = set()

        def area(r, c) -> int:
            if r >= len(grid) or r < 0 or c >= len(grid[0]) or c < 0 or grid[r][c] == 0 or (r, c) in visited:
                return 0
            
            visited.add((r, c))

            return 1 + area(r + 1, c) + area(r - 1, c) + area(r, c + 1) + area(r, c - 1)
        
        maxa = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    a = area(r, c)
                    maxa = max(maxa, a)

        return maxa
                



