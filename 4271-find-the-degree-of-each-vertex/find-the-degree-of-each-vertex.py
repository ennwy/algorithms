class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        if len(matrix) == 1:
            return [0]


        ans = [0] * len(matrix) # ans = [1 1 0]

        for i in range(len(matrix) - 1): # i = 1
            for j in range(i+1, len(matrix)): # j = 2
                if matrix[i][j] == 1:
                    ans[i] += 1
                    ans[j] += 1

        return ans
