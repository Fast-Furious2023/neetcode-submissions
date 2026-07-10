class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #decision tree: at each step, either start new or continue the previous subarray
        #possible: nums[i], dp[i-1]*nums
        #consider negatives, so maintain min and max

        res = nums[0]
        min_prod = nums[0]
        max_prod = nums[0]

        for num in nums[1:]:
            candidates = (num, min_prod*num, max_prod*num)
            min_prod = min(candidates)
            max_prod = max(candidates)
            res = max(res,max_prod)
        
        return res