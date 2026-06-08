class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]

        heapify(stones)

        # y = -5, x = 2
 
        while stones:
            y = -heappop(stones)
            if not stones:
                return y

            x = -heappop(stones)

            if y > x:
                heappush(stones, -(y - x))
        
        return 0

            


