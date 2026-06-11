class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for n in nums:
            counts[n] += 1
        
        heap = []
        for n, c in counts.items():
            heappush(heap, (-c, n))
        
        res = []
        while len(res) < k:
            res.append(heappop(heap)[1])

        return res
                
        
        # counts = defaultdict(int)

        # for n in nums:
        #     counts[n] += 1
        
        # freq = [[] for _ in range(len(nums) + 1)]

        # for n, count in counts.items():
        #     freq[count].append(n)

        # res = []
        # for i in range(len(freq) - 1, 0, -1):
        #     for n in freq[i]:
        #         res.append(n)
        #         k -= 1
                
        #         if k == 0:
        #             return res
        
        # return res
