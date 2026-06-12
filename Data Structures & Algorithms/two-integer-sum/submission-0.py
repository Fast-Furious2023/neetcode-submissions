class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookingfor = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if nums[i] in lookingfor:
                return [lookingfor[nums[i]], i]
            lookingfor[diff] = i
