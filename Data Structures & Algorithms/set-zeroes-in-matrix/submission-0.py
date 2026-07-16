class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # 1st iteration: find 0 and mark the corresponding row and column using top row and left column
        # 2nd iteration: update the cells in corresponding row and column
        m, n = len(matrix), len(matrix[0])
        topleft = -1
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    if i == 0:
                        topleft = 0
                    else:
                        matrix[i][0]=0
                        matrix[0][j]=0

        for i in range(1,m):
            for j in range(1,n):
                if matrix[0][j] ==0 or matrix[i][0] ==0:
                    matrix[i][j] = 0
        
        if matrix[0][0] == 0:
            for i in range(m):
                matrix[i][0] = 0
        if topleft == 0:
            for i in range(n):
                matrix[0][i]=0
        
        