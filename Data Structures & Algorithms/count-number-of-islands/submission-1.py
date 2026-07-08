class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[0])
        counter = 0
        def dfs(r,c):
            if grid[r][c] =="0":
                return
            

            for dr, dc in [(0,1),(1,0),(-1,0),(0,-1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc <C and grid[nr][nc] == "1" :
                    grid[nr][nc] = 0
                    dfs(nr,nc)
                   
            
        
        for r in range(R):
            for c in range(C):
                if grid[r][c] == "1":
                  dfs(r,c)
                  counter += 1
        return counter