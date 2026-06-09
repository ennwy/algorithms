class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x, y in points:
            heappush(heap, (x*x+y*y, (x,y)))
        
        res = []
        while len(res) < k:
            res.append(heappop(heap)[1])

        return res
