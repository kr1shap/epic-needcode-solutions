class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0 
        buy = 10191029109808
        for i in range(len(prices)):
            buy = min(buy, prices[i])
            maxP = max(maxP, prices[i]-buy)
        return maxP if maxP > 0 else 0