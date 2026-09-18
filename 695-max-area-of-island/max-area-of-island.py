class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        def unvisited(r, c) -> bool:
            return 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 1

        directions = ((1,0), (-1, 0), (0, -1), (0, 1))
        
        def add_neightbours(r, c, q):
            for dr, dc in directions:
                if unvisited(dr+r, dc+c):
                    grid[dr+r][dc+c] = 0
                    q.append((dr+r, dc+c))
        
        def bfs(r, c) -> int:
            q = deque()
            q.append((r,c))
            grid[r][c] = 0

            area = 0

            while q:
                cr, cc = q.popleft()
                area += 1
                
                add_neightbours(cr, cc, q)
            
            return area

        maxarea = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    maxarea = max(maxarea, bfs(r, c))
        
        return maxarea