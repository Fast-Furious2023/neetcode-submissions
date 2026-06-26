class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #use the index as set, iterate through the elements, negate the corresponding index position equal to the value of an element
        #if an index position is found negative before negating, a duplicate value is found
        for i in range(len(nums)):
            if nums[abs(nums[i])] < 0:
                return abs(nums[i])
            else:
                nums[abs(nums[i])] *=-1
        

