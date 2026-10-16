class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [price for price in cost] + [0]
        for i in range(2, len(cost)+1):
            dp[i] += min(dp[i-1], dp[i-2])
        return dp[-1]