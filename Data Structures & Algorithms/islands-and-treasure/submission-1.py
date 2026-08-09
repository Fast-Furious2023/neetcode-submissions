from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #bfs to find the nearest 0, if connected
        inf = 2147483647
        m = len(grid)
        n = len(grid[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        
        queue = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    queue.append((i,j))

        while queue:
            r, c = queue.popleft()
            for d_r, d_c in directions:
                n_r, n_c = d_r + r, d_c + c
                
                if 0 <= n_r < m and 0 <= n_c < n and grid[n_r][n_c] == inf:
                    queue.append((n_r,n_c))
                    grid[n_r][n_c] = grid[r][c]+1
                       
              

      



                    

                            


            