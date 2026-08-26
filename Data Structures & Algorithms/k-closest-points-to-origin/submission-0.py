class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def computeDistance(one:List[float], two:List[float]) -> float: 
            return math.sqrt((one[0] - two[0])**2 + (one[1] - two[1])**2)

        # use heap of max size k, minheap
        minheap = []
        for i in range(0, len(points)):
            distance = computeDistance([0,0], points[i])
            tup = (-distance, points[i])
            heapq.heappush(minheap, tup)
            if len(minheap) > k: 
                heapq.heappop(minheap)
        #return values 
        res = []
        for (negdist, point) in minheap: 
            res.append(point)
        return res
        