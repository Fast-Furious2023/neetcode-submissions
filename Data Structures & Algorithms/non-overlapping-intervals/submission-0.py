class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = [intervals[0]]
        count = 0

        for i in range(1,len(intervals)):
            if intervals[i][0] < res[-1][1]:
                count += 1
                res[-1][1] = min(res[-1][1],intervals[i][1])
            else:
                res.append(intervals[i])

        return count
