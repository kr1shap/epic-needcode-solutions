class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        for interval in intervals: 
            left = interval[0]
            right = interval[1]
            if not res: 
                res.append(interval)
                continue
            oldLeft = res[-1][0]
            oldRight = res[-1][1]
            if oldLeft <= left <= right <= oldRight:
                continue
            if oldRight < left:
                res.append(interval)
            else:
                res.pop()
                res.append([min(oldLeft, left), max(oldRight, right)])
        return res
