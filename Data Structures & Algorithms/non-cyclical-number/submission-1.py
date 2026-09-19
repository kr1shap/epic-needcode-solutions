class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True: 
            if n == 1: 
                return True
            # get sqaures of digits 
            temp = n 
            res = 0 
            while temp > 0: 
                res+= (temp%10)*(temp%10)
                temp = temp // 10
            n = res
            if n in seen: 
                return False
            seen.add(n)