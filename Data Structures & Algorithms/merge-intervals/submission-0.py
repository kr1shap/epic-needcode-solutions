class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        for interval in intervals: 
            left = interval[0]
            right = interval[1]
            if not res: 
                res.append(interval)
            else: 
                prevInt = res[-1]
                prevL = prevInt[0]
                prevR = prevInt[1]
                if left > prevR: #non overlapping
                    res.append(interval)
                    continue 
                if prevL <= left <= prevR and prevL <= right <= prevR: 
                    continue #do not append 
                if right > prevR: 
                    res.pop(-1)
                    newInt = [min(left, prevL), right]
                    res.append(newInt)
        return res
                

            # cases 
            # [1, 2] [2, 3] (right longer than prev right)
            # [1, 2], [1, 3] # extend 
            # [1, 2], [1, 1] # fully contained 
            # [1, 2], [3, 4] non overlapping