"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda tup: tup.start)
        last = Interval(-5, -1)
        for inter in intervals:
            # start is in the interval 
            if last.start < inter.start < last.end: 
                return False
            # end is in the interval 
            if last.start < inter.end < last.end: 
                return False
            # start equals start
            if last.start == inter.start: 
                return False
            if last.end == inter.end: 
                return False
            
            # s
            # if inter.end == last.end and inter.start == last.start:
            #     return False 
            # if last.start < inter.start < last.end:
            #     return False
            # if last.start < inter.start < last.end:
            #     return False
            # if last.start < inter.end < last.end:
            #     return False
            # if last.start < inter.end < last.end:
            #     return False
            last = inter
        return True
