class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if color == image[sr][sc]:
            return image

        orig = image[sr][sc]
        rows, cols = len(image), len(image[0])

        def dfs(r, c):
            if not (0 <= r < rows and 0 <= c < cols and image[r][c] == orig):
                return
            
            image[r][c] = color

            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        dfs(sr, sc)

        return image
            
            

