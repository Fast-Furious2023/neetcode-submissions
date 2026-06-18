class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #return maximum profit or if not profitable, 0
        profit = 0
        for i in range(1,len(prices)):
            sell = max(prices[i:])
            buy = min(prices[:i])
            profit = max(profit, sell - buy)
        return profit

