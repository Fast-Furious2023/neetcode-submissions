class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        par = ['(',')']

        def backtrack(right,left, path): #right <= left <= n
            if right == n:
                res.append(''.join(path))
                return
            
            for i in range(2):
               
                if par[i]=='(' and left < n:
                    path.append('(')
                    backtrack(right,left+1,path)
                    path.pop()

                if par[i]==')' and right < left:
                    path.append(')')
                    
                    backtrack(right+1,left,path)
                    path.pop()
        backtrack(0,0,[])
        return res


         

              
 

        