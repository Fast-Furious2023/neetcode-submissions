class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        hash_set = set(nums)
        count = {}
        for num in hash_set:
            if num -1 not in hash_set:
                count[num] = 1

        for e in count:
            for i in range(1,len(nums)):
                if e+i in hash_set:
                    count[e] += 1
                else:
                    break
        
        return max(count.values())
