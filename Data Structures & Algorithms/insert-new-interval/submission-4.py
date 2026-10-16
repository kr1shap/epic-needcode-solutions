import bisect
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        if not intervals: 
            return [newInterval]

        left = bisect.bisect_left(intervals,newInterval[0], key=lambda x:x[0])
        if left >= len(intervals):
            intervals.append(newInterval)
        else:
            intervals.insert(left, newInterval)
        for i in range(len(intervals)):
            if i == 0: 
                res.append(intervals[i])
                continue
            else: 
                left = intervals[i][0]
                right = intervals[i][1]
                leftOld = res[-1][0]
                rightOld = res[-1][1]
                if leftOld <= left <= right <= rightOld: 
                    continue
                if rightOld < left: 
                    res.append(intervals[i])
                    continue
                if left <= rightOld:
                    res.pop()
                    res.append([min(left, leftOld), max(right, rightOld)])
        return res
 

        