class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def rob_liner(nums):
            prev2,prev1=0,0
            for num in nums:
                prev2, prev1 = prev1, max(prev2+num, prev1)
            return prev1
        
        if len(nums) == 1:
            return nums[0]

        return max(rob_liner(nums[:-1]), rob_liner(nums[1:]))