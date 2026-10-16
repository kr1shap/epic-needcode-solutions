from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # map s -> hashmap 
        t_hashmap = defaultdict(int)
        for char in t: 
            t_hashmap[char]+=1

        window = defaultdict(int)
        need = len(t_hashmap)
        have = 0
        wind = [-1, -1]
        res = float("infinity")
        l = 0
        for r in range(len(s)):
            window[s[r]] += 1
            if s[r] in t_hashmap and window[s[r]] == t_hashmap[s[r]]:
                have+=1
            while have == need: 
                if (r-l) + 1 < res: 
                    res = (r-l) + 1
                    wind = [l, r]
                window[s[l]] -=1
                if s[l] in t_hashmap and window[s[l]] < t_hashmap[s[l]]:
                    have-=1
                l+=1
        l, r = wind
        return s[l: r+1] if res != float("infinity") else ""

