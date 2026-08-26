import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)
        while len(stones) > 1: 
            #pop off two stones 
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)
            #convert values into non-negative
            stone1 = -stone1
            stone2 = -stone2
            if stone1 == stone2: 
                continue
            if stone1 < stone2: 
                stone2 -= stone1
                heapq.heappush(stones, -stone2)
            else: 
                stone1 -= stone2
                heapq.heappush(stones, -stone1)
        return -stones[0] if len(stones) == 1 else 0

        