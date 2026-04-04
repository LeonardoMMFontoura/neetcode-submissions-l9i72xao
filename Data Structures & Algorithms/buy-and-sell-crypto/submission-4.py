class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
        minPrice = prices[0]
        maxSum = 0
        for price in prices[1:]:
            minPrice = min(minPrice, price)
            maxSum = max(maxSum, price - minPrice)
        return maxSum