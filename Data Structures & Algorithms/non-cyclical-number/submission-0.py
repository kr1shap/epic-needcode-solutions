class Solution:
    def isHappy(self, n: int) -> bool:
        prev = set()
        while n >= 2: # n > 1
            if n in prev:
                return False
            prev.add(n) #add current
            #get sum of squares of digits
            temp = n
            n = 0
            while temp > 0:
                n+=(temp%10)**2
                temp//=10
        return True