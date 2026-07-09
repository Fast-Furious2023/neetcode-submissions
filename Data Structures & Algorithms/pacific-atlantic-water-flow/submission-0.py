class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #reverse traversing: flow to cells higher or equal

        pacific_reachable = set()
        atlantic_reachable = set()

        R, C = len(heights), len(heights[0])


        def dfs(r,c,collection):
            
            collection.add((r,c)) 
               
            
            for dr, dc in [(0,1),(1,0),(-1,0),(0,-1)]:
                nr, nc = r + dr, c + dc
                if (0 <= nr < R and
                    0 <= nc < C and
                    (nr,nc) not in collection and
                    heights[nr][nc] >= heights[r][c]):
                 
                    dfs(nr,nc,collection)
        
        for c in range(C):
            dfs(0,c,pacific_reachable)
            dfs(R-1,c, atlantic_reachable)
        for r in range(R):
            dfs(r,0, pacific_reachable)
            dfs(r,C-1,atlantic_reachable)
        
        res = []
        for r in range(R):
            for c in range(C):
                if (r,c) in pacific_reachable and (r,c) in atlantic_reachable:
                    res.append([r,c])
        return res
