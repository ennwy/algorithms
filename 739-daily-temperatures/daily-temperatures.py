class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        res = [0] * len(t) 
        stack = []

        for i in range(len(t)-1, -1, -1):
            while stack and t[stack[-1]] <= t[i]:
                stack.pop()

            if not stack:
                res[i] = 0
            else:
                res[i] = stack[-1] - i
            
            stack.append(i)

        return res






