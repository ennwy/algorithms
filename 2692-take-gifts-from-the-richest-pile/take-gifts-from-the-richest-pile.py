class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(len(gifts)):
            gifts[i] = -gifts[i]

        heapify(gifts)

        for _ in range(k):
            root = int(sqrt(-heappop(gifts)))
            heappush(gifts, -root)
        
        return -sum(gifts)