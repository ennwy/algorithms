class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusts = defaultdict(int)
        trusted = defaultdict(int)

        for a, b in trust: 
            trusts[a] += 1
            trusted[b] += 1

        for label in range(1, n+1):
            if label not in trusts and trusted[label] == n-1:
                return label

        return -1