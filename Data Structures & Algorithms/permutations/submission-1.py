class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        visited = [False]*n

        def backtrack(path):
            if len(path) == n:
                res.append(list(path))
                return
            
            for i in range(n):
                if visited[i]:
                    continue
                else:
                    path.append(nums[i])
                    visited[i]=True
                    backtrack(path)
                    visited[i]=False
                    path.pop()

        backtrack([])
        return res


