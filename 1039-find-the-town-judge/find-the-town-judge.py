class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusts = defaultdict(list)
        trusted = defaultdict(int)


        for a, b in trust: 
            trusts[a].append(b)
            trusted[b] += 1

        for label in range(1, n+1):
            if label not in trusts and trusted[label] == n-1:
                return label

        return -1