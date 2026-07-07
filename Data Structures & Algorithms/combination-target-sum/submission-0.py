class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        track = []

        def backtrack(start, remaining):
            if remaining == 0:
                res.append(track[:])
                return 
            if remaining < 0:
                return 

            

            for i in range(start, len(nums)):
                track.append(nums[i])  
                backtrack(i, remaining - nums[i])
                track.pop()
        
        backtrack(0,target)
        return res
