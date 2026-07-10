class Solution:
    def rob(self, nums: List[int]) -> int:
        #two rolling variables
        prev1=0 #the amount of money accumulated by that house
        prev2=0

        for num in nums:
            current = max(prev2 + num, prev1)
            
            prev2= prev1
            prev1= current

        return prev1