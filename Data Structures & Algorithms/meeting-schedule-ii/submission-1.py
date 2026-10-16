"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0 or not intervals: 
            return 0
        
        intervals.sort(key=lambda x: x.start)
        for interval in intervals:
            print(interval.start, interval.end)

        roomCount = 1
        endTimeHeap = [intervals[0].end]
        for i in range(1, len(intervals)):
            interval = intervals[i]
            oldInterval = intervals[-1]
            # empty out heap
            while endTimeHeap and endTimeHeap[0] <= interval.start:
                heapq.heappop(endTimeHeap)
            # check if we have rooms 
            if roomCount - len(endTimeHeap) <= 0: 
                roomCount+=1
            heapq.heappush(endTimeHeap, interval.end)
        return roomCount



