class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x, y in points:
            if len(heap) < k:
                heappush(heap, (-x*x-y*y, (x,y)))
            elif -heap[0][0] > x*x+y*y:
                heapreplace(heap, (-x*x-y*y, (x,y)))
        

        return [heap[i][1] for i in range(k)]
