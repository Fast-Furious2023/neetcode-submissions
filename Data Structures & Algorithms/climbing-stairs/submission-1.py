class Solution:
    def climbStairs(self, n: int) -> int:
        #tabulation

        if n <= 2:
            return n

        first = 1 #ways of climbing 1 stair
        second = 2 #ways of climbing 2 steps stair

        for i in range(3,n+1): #ways of climbing 3 steps stair
            third = first+second 
            first = second #keeping rolling
            second = third
        return second