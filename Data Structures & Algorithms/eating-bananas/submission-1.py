import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def findtime(rate):
            time = 0
            for num in piles:
                time += math.ceil(num/rate)
            return time

        n = len(piles)
        l, r = 1, max(piles)
        res = r
        while l <= r:
            mid = l + (r-l)//2
            curr_h = findtime(mid)
            if curr_h <= h:
                res = mid
                r = mid-1
            else:
                l = mid+1
        return res


            



       
            


                
                    

        




