class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        buyP = 293810381029808
        for price in prices: 
            maxP = max(maxP, price-buyP)
            buyP = min(buyP, price)
        return maxP               