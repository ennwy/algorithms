class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counter = defaultdict(int)
        for n in arr:
            counter[n] = counter.get(n, 0) + 1

        heap = []
        for count in counter.values():
            heappush(heap, -count)
        
        length = len(arr)
        res = 0
        while length > len(arr) // 2: 
            length = length + heappop(heap)
            res += 1

        return res
