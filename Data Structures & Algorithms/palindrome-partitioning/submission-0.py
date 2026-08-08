class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def isPalindrome(s):
            
            l, r = 0, len(s)-1
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            
            return True
        
        res = []
        n = len(s)
        def backtrack(start,path):
            if start == n:
                if isPalindrome(path[-1]):
                    res.append(list(path))
                return
            
            for i in range(2):
                if i == 0:
                    if path and not isPalindrome(path[-1]):
                        continue
                    
                    path.append(s[start])
                    backtrack(start+1,path)
                    path.pop()

                if i == 1 and path:
                    path[-1]=path[-1]+s[start]
                    backtrack(start+1,path)
                    path[-1]=path[-1][:-1]

        backtrack(0,[])
        return res




                




