class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        q = deque()
        visited = set()
        freshcount = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                
                if grid[r][c] == 1:
                    freshcount +=1
        
        def rotOrange(r: int, c: int) -> bool:
            if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visited or grid[r][c] != 1: 
                return False
            
            visited.add((r,c))
            q.append((r,c))

            return True

        t = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = 2

                rotOrange(r+1, c)
                rotOrange(r-1, c)
                rotOrange(r, c+1)
                rotOrange(r, c-1)
            t += 1

        if len(visited) < freshcount:
            return -1

        return max(t - 1, 0)
        
