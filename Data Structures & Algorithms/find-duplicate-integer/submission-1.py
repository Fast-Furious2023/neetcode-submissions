class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #use the index as set, iterate through the elements, negate the corresponding index position equal to the value of an element
        #if an index position is found negative before negating, a duplicate value is found
       # for i in range(len(nums)):
        #    if nums[abs(nums[i])] < 0:
         #       return abs(nums[i])
          #  else:
           #     nums[abs(nums[i])] *=-1
        
        #Floyd's cycle detection
        #treat array as linkedlist, element's value as pointer to the next node(as index of next value)
        #find a cycle, and return the cycle entrance

        slow=nums[0]
        fast=nums[0]
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow == fast:
                break
        
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
