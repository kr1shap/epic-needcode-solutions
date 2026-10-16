class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort the intervals by the start
        intervals.sort(key= lambda x:x[0])
        # merge intervals? 
        res = []
        count = 0
        for i in range(len(intervals)):
            left = intervals[i][0]
            right = intervals[i][1]
            if not res: 
                res.append(intervals[i])
            else: 
                oldLeft = res[-1][0]
                oldRight = res[-1][1]
                if left < oldRight: 
                    res.pop()
                    res.append([min(oldLeft, left), min(oldRight, right)])
                    count+=1
                else:
                    res.append(intervals[i])
        return count
