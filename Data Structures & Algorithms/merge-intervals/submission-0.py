class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        n = len(intervals)

        intervals.sort()

        res.append(intervals[0])

        for i in range(1,n):
            if res[-1][1] >= intervals[i][0]: 
                start = res[-1][0]
                end = res[-1][1]
                res.pop()
                res.append([start,max(intervals[i][1],end)])
               
            else:
                res.append(intervals[i])
        return res

       


