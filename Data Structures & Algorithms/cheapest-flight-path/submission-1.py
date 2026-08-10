from collections import defaultdict, deque
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        adj = defaultdict(list) 
        for f, t, price in flights:
            adj[f].append((t,price))

        stops = [float('inf')]*n
        stops[src]=0

        prices = [float('inf')]*n
        prices[src]=0

        heap = [(0,src,0)]

        while heap:
            p, airport, stop = heapq.heappop(heap)

            if airport == dst:
                return p

            if stop > k : 
                continue

            for i, price in adj[airport]:
                if stops[i] > stop + 1 or prices[i] > p+price:
                    heapq.heappush(heap,(price+p,i,stop+1))
                    stops[i] = stop + 1
                    prices[i] = p + price

        return -1
                    







        