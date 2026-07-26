class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        ma = 0
        while i < len(s) and j < len(s): 
            if i == j: 
                j+=1
                ma = ma if len(s[i:j]) < ma else len(s[i:j])
                continue
            #now given i and j are not the same 
            while j < len(s) and s[j] not in s[i:j]:
                j+=1
            if j == len(s):
                ma = ma if len(s[i:j]) < ma else len(s[i:j])
                break
            #now from s[i:j] has the stuff 
            ma = ma if len(s[i:j]) < ma else len(s[i:j])
            #dupe char
            dupeC = s[j]
            while i < len(s) and dupeC in s[i:j]:
                i+=1
        return ma
