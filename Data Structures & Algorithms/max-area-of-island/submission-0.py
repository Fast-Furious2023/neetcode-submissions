class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #dfs
        #sink the land in place
        m, n = len(grid), len(grid[0])

        def dfs(r,c):
            if r < 0 or r >= m or c < 0 or c>= n or grid[r][c] == 0:
                return 0 
            
            grid[r][c]=0 # sink the land

            return 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)

        max_area = 0

        for i in range(m):
            for j in range(n):
            
                if grid[i][j] == 1:
                    current = dfs(i,j)
                    max_area = max(max_area,current)
        
        return max_area





       


        
