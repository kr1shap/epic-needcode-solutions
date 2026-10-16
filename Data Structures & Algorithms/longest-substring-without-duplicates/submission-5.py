from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0 
        currMap = set()
        l = 0 
        r = 0
        while l <= r and r < len(s):
            if l == r == 0: 
                currMap.add(s[l])
                maxLen = 1
                r+=1
                continue
            else: 
                # continue moving left 
                while s[r] in currMap and l <= r: 
                    currMap.remove(s[l])
                    l+=1
                currMap.add(s[r])
                maxLen = max(maxLen, r-l+1)
                r+=1
        return maxLen
