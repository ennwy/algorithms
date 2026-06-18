class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        q = deque()
        fresh = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh +=1
    
        t = 0
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in ((1,0),(-1,0),(0,-1),(0,1)):
                    cr, cc = r + dr, c + dc

                    if 0 <= cr < rows and 0 <= cc < cols and grid[cr][cc] == 1: 
                        fresh -= 1
                        grid[cr][cc] = 2
                        q.append((cr,cc))     
            t += 1

        return t if fresh == 0 else -1
        
