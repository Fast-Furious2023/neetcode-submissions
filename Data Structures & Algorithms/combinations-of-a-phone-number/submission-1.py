class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        map = {2:['a','b','c'],
               3:['d','e','f'],
               4:['g','h','i'],
               5:['j','k','l'],
               6:['m','n','o'],
               7:['p','q','r','s'],
               8:['t','u','v'],
               9:['w','x','y','z']}

        if not digits:
            return []
        
        res = []
        n = len(digits)
        def backtrack(start,current):
            if start == n:
                res.append(current)
                return
            
            
            for char in map[int(digits[start])]:
                backtrack(start+1,current+char)

        backtrack(0,'')
        return res