class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = {}
        s2 = {}
        for i in range(0, len(s)):
            s1[s[i]] = s1.get(s[i], 0) + 1
        for i in range(0, len(t)):
            s2[t[i]] = s2.get(t[i], 0) + 1
        return s1 == s2

        