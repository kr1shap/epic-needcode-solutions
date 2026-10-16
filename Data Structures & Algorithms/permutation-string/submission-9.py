from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        s1_d = defaultdict(int)
        for char in s1:
            s1_d[char]+=1
        s2_d = defaultdict(int)
        for i in range(len(s1)):
            s2_d[s2[i]]+=1
        if s1_d == s2_d:
            return True
        # sliding window 
        l = 1
        r = len(s1)
        while r < len(s2):
            charL = s2[l-1]
            charR = s2[r]
            s2_d[charL]-=1
            s2_d[charR]+=1
            if s2_d[charL] == 0:
                del s2_d[charL]
            if s2_d == s1_d:
                return True
            r+=1
            l+=1
        return False
