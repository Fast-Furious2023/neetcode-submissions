class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum_full = n*(n+1)//2
        sum_n = sum(nums)
        return sum_full - sum_n

        