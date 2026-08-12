class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #sum is divisble by 2--> possible; if not, false

        total = sum(nums)
        n = len(nums)
        if total%2 == 1:
            return False

        target= total//2
        
        curSum = 0

        def helper(idx, c_sum):
            if idx > n - 1:
                return False
            if c_sum == target:
                return True

            return helper(idx+1, c_sum + nums[idx]) or helper(idx+1, c_sum)

        return helper(0, 0)