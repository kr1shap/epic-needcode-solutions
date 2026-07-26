class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        memo[1] = 1
        memo[2] = 2
        memo[3] = 3

        def f(x: int) -> int: 
            if x in memo: 
                return memo[x]
            else:
                memo[x] = f(x-1) + f(x-2)
                return memo[x]
            
        return f(n)

        