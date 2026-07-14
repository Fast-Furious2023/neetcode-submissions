class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        n = len(intervals)

        intervals.sort()

        res=[intervals[0]]

        for i in range(1,n):
            if res[-1][1] >= intervals[i][0]: 
                
                
                res[-1][1]=max(intervals[i][1],res[-1][1])
               
            else:
                res.append(intervals[i])
        return res

       


