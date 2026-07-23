import heapq
class Solution:
    def jump(self, nums: List[int]) -> int:
        #min array for the min steps to get to i
        #min heap:iterate through the numbers that can jump to i
        #update min array[i]

        n = len(nums)

        min_array = [float('inf')]*n


        def count_min_steps(i):
            if i == 0:
                min_array[0]=0
                return
            for j in range(i):
                if nums[j]+j >= i:
                    min_array[i] =min(min_array[j] + 1, min_array[i])
                    
        for i in range(n):
            count_min_steps(i)

        return min_array[n-1]