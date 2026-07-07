class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(start, track):
            res.append(list(track))
            for i in range(start, len(nums)):
                track.append(nums[i])
                backtrack(i+1, track)
                track.pop()
        backtrack(0,[])
        return res


