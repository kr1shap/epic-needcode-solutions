class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minBuying = float("inf")
        i = 0
        while i < len(prices):
            if prices[i] < minBuying:
                minBuying = prices[i]
            maxProfit = maxProfit if maxProfit > prices[i]-minBuying else prices[i]-minBuying
            i+=1
        return maxProfit
