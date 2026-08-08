class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(i,sum_sofar,path):
            if sum_sofar == target:
                res.append(list(path))
                return
            
            for j in range(i,len(candidates)):
                if sum_sofar + candidates[j] > target:
                    break
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                
                path.append(candidates[j])
                backtrack(j+1, sum_sofar + candidates[j],path)
                path.pop()
            
        backtrack(0,0,[])
        return res



