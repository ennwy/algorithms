class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusts = [0] * (n + 1)
        trusted = [0] * (n + 1)

        for a, b in trust: 
            trusts[a] += 1
            trusted[b] += 1

        for label in range(1, n+1):
            if trusts[label] == 0 and trusted[label] == n-1:
                return label

        return -1