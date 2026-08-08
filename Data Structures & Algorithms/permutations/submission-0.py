class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def backtrack(path):
            if len(path) == n:
                res.append(list(path))
                return
            
            for i in range(n):
                if nums[i] in path:
                    continue
                else:
                    path.append(nums[i])
                    backtrack(path)
                    path.pop()
        backtrack([])
        return res


