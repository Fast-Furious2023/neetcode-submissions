class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #-n1=n2+n3, two sum & target==-n1
        res = []
        n = len(nums)
        nums.sort()
        for i in range(n):
            if nums[i]>0:
                break

        for i in range(n):
            target = -nums[i]
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l,r=i+1,n-1
            while l < r:
                if nums[l]+nums[r]>target:
                    r -= 1
                elif nums[l]+nums[r]<target:
                    l += 1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    while r > l and nums[r] == nums[r-1]:
                        r -= 1
                    while r>l and nums[l] == nums[l+1]:
                        l += 1
                    l += 1
                    r -= 1
         
        return res



