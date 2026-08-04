class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check condition 1: all numbers 1-9; condition 2: no duplicate for each row, column,subgrid
       
        row_set = [set() for _ in range(9)]
        column_set = [set() for _ in range(9)]
        subgrid_set = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                val = board[i][j]

                if val == '.':
                    continue
                
                grid_index = (i//3)*3 + j//3
                
                if val in row_set[i] or val in column_set[j] or val in subgrid_set[grid_index]:
                    return False
                
                row_set[i].add(val)
                column_set[j].add(val)
                subgrid_set[grid_index].add(val)

        return True




