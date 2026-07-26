class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = {}
        for char in s: 
            if char not in res: 
                res[char] = 0
            res[char]+=1
        maxS = ""
        maxl = 0
        for char in res: 
            if res[char] > maxl:
                maxl = res[char]
                maxS = char
            elif res[char] == maxl:
                maxS+=char
        #now do sliding window 
        i = 0
        j = 0
        tempv = 0
        maxw = 0
        print("maxS", maxS)
        for char in 'ABCEDEFGHIJKLMNOPQRSTUVWXYZ':
            i = 0
            j = 0
            tempv = 0
            while i < len(s) and j < len(s):
                # print(s[i:j+1])
                # print("tempk", tempv)
                if s[j] != char: 
                    tempv=tempv+1
                while tempv > k: 
                    if s[i] != char:
                        tempv-=1
                    i+=1
                j+=1
                if abs(j-i) > maxw:
                    maxw = abs(j-i)
        return maxw


        

        