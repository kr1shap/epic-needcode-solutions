from collections import defaultdict
import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # create frequency map 
        freq = defaultdict(int)
        for task in tasks: 
            freq[task]+=1
        pq = []

        # make pq 
        for amt in freq.values(): 
            pq.append(-amt)
        heapq.heapify(pq)
        counter = 0
        queue = deque()
        while pq or queue:
            counter+=1
            if pq: 
                negAmt = heapq.heappop(pq)
                if negAmt+1 < 0: 
                    queue.append((negAmt+1,counter+n))
            if queue: 
                negAmt, cd = queue[0]
                if cd <= counter: 
                    heapq.heappush(pq, negAmt)
                    queue.popleft()
        return counter