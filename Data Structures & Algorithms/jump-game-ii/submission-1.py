import heapq
class Solution:
    def jump(self, nums: List[int]) -> int:
        # min array for the min steps to get to i
        # min heap:iterate through the numbers that can jump to i
        # update min array[i]

        # n = len(nums)

        # min_array = [float('inf')]*n


        # def count_min_steps(i):
        #     if i == 0:
        #         min_array[0]=0
        #         return
        #     for j in range(i):
        #         if nums[j]+j >= i:
        #             min_array[i] =min(min_array[j] + 1, min_array[i])
                    
        # for i in range(n):
        #     count_min_steps(i)

        # return min_array[n-1]


        # greedy approach: 

        n = len(nums)
        if n <= 1:
            return 0

        current_end = 0
        jumps = 0
        max_dist = 0 # the max end of next jump

        for i in range(n):
            max_dist = max(max_dist, i+nums[i])

            if i == current_end:
                jumps+=1
                current_end=max_dist
            
            if current_end >= n-1:
                return jumps


