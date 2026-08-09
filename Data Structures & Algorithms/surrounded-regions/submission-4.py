from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # 1. find all the 'O' cells along the edges
        # 2. use bfs to mark all the other 'O' connected the above
        # 3. the remaining 'O's apart from steps 1 and 2 are surrounded regions

        m, n = len(board), len(board[0])
        table = [False]*(m*n)
        queue = deque()

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    table[i*n+j] = True
                    if i == 0 or j == 0 or i == m-1 or j == n-1:
                        table[i*n+j] = False
                        queue.append((i,j))

        directions = [(1,0),(-1,0),(0,1),(0,-1)]
       
        
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = dr+r, dc+c
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == 'O':
                    idx = nr*n+nc
                    if table[idx]==True:
                        table[nr*n+nc]=False
                        
                        queue.append((nr,nc))
        
        for idx in range(len(table)):
            if table[idx] == True:
                r, c = idx//n, idx%n
                board[r][c]='X'


