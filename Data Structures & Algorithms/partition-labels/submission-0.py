from collections import defaultdict
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        idx = 0

        # build freq map 
        freq = defaultdict(int) 
        for i in range(len(s)):
            freq[s[i]]=i
        
        end = 0
        res = []
        length = 0
        for i in range(len(s)):
            char = s[i]
            length+=1
            end = max(freq[s[i]], end)
            if i == end: 
                res.append(length)
                length = 0 
                end = i+1
        return res