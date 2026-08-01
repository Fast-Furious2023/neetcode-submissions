from functools import lru_cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        @lru_cache(maxsize=None)
        def dfs(day,empty_handed):

            if day >= len(prices):
                return 0

            if empty_handed:
                buy = dfs(day+1,False) - prices[day]
                skip = dfs(day+1,True)
                return max(buy,skip)
            else:
                sell = dfs(day+2,True)+prices[day]
                skip = dfs(day+1,False)
                return max(sell,skip)
                
        return dfs(0,True)