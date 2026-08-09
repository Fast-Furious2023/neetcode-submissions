from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #bfs: find the minum dis from a fresh fruit to a rotten
        #the answer is the max of all distances

        m, n = len(grid), len(grid[0])
        queue = deque()
        count_fresh = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    queue.append((i,j))
                if grid[i][j]==1:
                    count_fresh+=1

        
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        mx = 0
        largest = 0

        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc]==1:
                    queue.append((nr,nc))
                    grid[nr][nc]=grid[r][c]+1
                    mx += 1
                    largest = max(largest,grid[nr][nc])
        
        if count_fresh == 0:
            return 0
            
        if mx != count_fresh:
            return -1
                    
        return largest-2


                    

        