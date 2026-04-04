class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
        minPrice = prices[0]
        bestProfit = 0
        for r in range(1, len(prices)):
            profit = prices[r] - minPrice
            bestProfit = max(bestProfit, profit)
            if prices[r] < minPrice:
                minPrice = prices[r]
        return bestProfit