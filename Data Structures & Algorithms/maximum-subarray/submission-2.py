class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-float("inf")]*(n+1)
        dp[0]=0

        for i in range(1,n+1):
            
            dp[i] = max(dp[i-1]+nums[i-1],nums[i-1])

        return max(dp[1:])
