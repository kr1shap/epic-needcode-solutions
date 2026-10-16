from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0 
        currMap = defaultdict(int)

        # bbbb
        # 1: maxLen = 1, l = 0, r = 1
        # 2: maxLen = 
        l = 0 
        r = 0
        while l <= r and r < len(s):
            if l == r == 0: 
                currMap[s[l]]+=1
                maxLen = 1
                r+=1
                continue
            else: 
                currMap[s[r]]+=1
                # continue moving left 
                while currMap[s[r]] > 1 and l <= r: 
                    currMap[s[l]]-=1
                    l+=1
                maxLen = max(maxLen, r-l+1)
                r+=1
        return maxLen
