class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0

        def dfs(r, c):
            if (
                not 0 <= r < len(grid) or
                not 0 <= c < len(grid[0]) or
                grid[r][c] == '0' or
                (r,c)  in visited
            ): return

            visited.add((r,c))

            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1' and (r,c) not in visited:
                    count += 1
                    dfs(r, c)
        
        return count
