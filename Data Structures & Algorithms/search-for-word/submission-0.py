class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R, C = len(board), len(board[0])
        visited = set()
        # check if a cell at rol, col matches word[i]
        def dfs(rol, col, i):
            #a valid path is found:
            if i == len(word):
                return True

            # the path is not valid 
            if rol < 0 or rol >= R or col < 0 or col >= C or (rol, col) in visited or board[rol][col] != word[i]:
                return False
            
            # the cell matches char at i in word, then add to set to avoid revisiting
            visited.add((rol,col))

            #explore next cell in paths at four directions
            found = (dfs(rol+1, col, i+1) or 
                    dfs(rol, col+1, i+1) or
                    dfs(rol-1, col, i+1) or
                    dfs(rol, col-1, i+1))
            visited.remove((rol,col))
            return found
        
        for r in range(R):
            for c in range(C):
                if dfs(r,c,0):
                    return True
        return False
        

