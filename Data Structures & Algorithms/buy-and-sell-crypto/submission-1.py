class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #return maximum profit or if not profitable, 0
        buy, sell = 0, 1
        profit = 0
        while sell < len(prices):
            if prices[buy] < prices[sell]:
                profit = max(profit, prices[sell] - prices[buy])
            else:
                buy = sell
            sell += 1
        return profit