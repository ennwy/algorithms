class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        ans = [0] * len(matrix) # ans = [1 1 0]

        for i in range(len(matrix) - 1): # i = 1
            for j in range(i+1, len(matrix)): # j = 2
                ans[i] += matrix[i][j]
                ans[j] += matrix[i][j]

        return ans
