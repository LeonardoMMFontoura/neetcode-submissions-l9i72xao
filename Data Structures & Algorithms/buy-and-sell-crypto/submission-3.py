class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
        minPrice = prices[0]
        bestProfit = 0
        for r in range(1, len(prices)):
            bestProfit = max(bestProfit, prices[r] - minPrice)
            minPrice = min(minPrice, prices[r])
        return bestProfit