class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
       
        memo = {}

        def helper(i,remain):
            if i == len(nums) and remain == 0:
                return 1 #if remain == 0 else 0
            if i >= len(nums):
                return 0

            if (i,remain) in memo:
                return memo[(i,remain)]
        # add
            add = helper(i+1,remain-nums[i])
        # minus
            minus = helper(i+1,remain+nums[i])

            memo[(i,remain)]=add+minus

            return memo[(i,remain)]

        return helper(0,target)

