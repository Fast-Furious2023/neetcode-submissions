class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #return maximum amount of water: 
        #min(heights[i], heights[j]) * (j-i)

        l, r = 0, len(heights) - 1
        amount = min(heights[l], heights[r]) * (r-l)
        while l < r:
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            amount = max(amount,  min(heights[l], heights[r]) * (r-l))
            
        return amount