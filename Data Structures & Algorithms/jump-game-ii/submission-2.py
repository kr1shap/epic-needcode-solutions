class Solution:
    def jump(self, nums: List[int]) -> int:
        # dp approach 
        # dp[i] = min num of jumps to reach i, from 0 
        # nums = [2,4,1,1,1,1]
        # for dp[1] -> would be 1. dp[0] = 0
        # is 1 because 

        # OR for a given point 
        # compute its min 
        # for i in range(i+1, i+1+nums[i]): dp[i] = min(dp[i], dp[cur] + 1)
        # dp[i] = min(dp[i])
        if not nums: 
            return 0
        dp = [92831098301 for i in range(len(nums))]
        dp[0] = 0

        for j in range(nums[0]):
            if 1+j >= len(nums):
                break
            dp[1+j] = 1

        for i in range(1, len(nums)):
            # print("======= i = ", i )
            # print(dp)
            for j in range(nums[i]):
                if i + j + 1 >= len(nums):
                    break
                dp[i+j+1] = min(dp[i+j+1], dp[i]+1)
        return 0 if dp[-1] == 92831098301 else dp[-1]
            