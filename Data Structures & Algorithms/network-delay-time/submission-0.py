import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [ [] for _ in range(n+1)]
        for u, v, t in times:
            adj[u].append((v,t))

        dist = [float('inf')]*(n+1)

        dist[k] = 0

        pq = [(0,k)]

        while pq:
            time, u = heapq.heappop(pq)

            if time > dist[u]:
                continue

            for v, t in adj[u]:
                if dist[v] > t+dist[u]:
                    dist[v] = t+dist[u]
                    heapq.heappush(pq,(dist[v],v))

        maxtime=max(dist[1:])
        return maxtime if maxtime != float('inf') else -1
         



