class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 1: 
            return s
        dp = [[False for i in range(len(s))] for j in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True #single length true by default 

        res = s[0]
        # iterate indexes
        for i in range(len(s)-1, -1, -1):
            for j in range(i+1, len(s)):   
                string = s[i:j+1] # string starting at i, ending at j
                # print(string)
                # print("-----")
                # print(i, j)
                # print(string)
                if len(string) == 2 and string[0] == string[-1]:
                    dp[i][j] = True
                    res = string if len(string) > len(res) else res
                elif i+1 <= j-1 and dp[i+1][j-1] and string[0] == string[-1]:
                    dp[i][j] = True
                    res = string if len(string) > len(res) else res
        return res