from collections import defaultdict
import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        adj = defaultdict(list)
        n = len(grid)

        for i in range(n):
            for j in range(n):
                curr = grid[i][j]
                for d_r, d_c in [(-1,0),(1,0),(0,1),(0,-1)]:
                    if 0 <= i + d_r < n and 0<= j+d_c < n:
                        adj[curr].append((grid[i+d_r][j+d_c],i+d_r,j+d_c))

        min_matrix = [[float('inf')]*n for _ in range(n)]

        min_heap = [(grid[0][0],0,0)]

        while heapq:
            elevation,i,j = heapq.heappop(min_heap)
            if elevation > min_matrix[i][j]:
                continue

            if i == n-1 and j == n-1:
                return elevation
        
            for e,e_i,e_j in adj[grid[i][j]]:
                next_e = max(elevation,e) 
                if next_e < min_matrix[e_i][e_j]:
                    min_matrix[e_i][e_j] = next_e
                    heapq.heappush(min_heap,(next_e,e_i,e_j))

