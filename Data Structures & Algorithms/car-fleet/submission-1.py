class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #use a hashtable for O(1) lookup
        table = {}
        n = len(position)
        res=0
        ahead = 0 #the time the car ahead of it reaches destination

        for i in range(n):
            table[position[i]]=speed[i]

        p_sorted = sorted(position)

        for i in range(n-1,-1,-1):
            pos = p_sorted[i]
            spd = table[pos]
            hour = (target-pos)/spd
            if hour > ahead:
                res+=1
                ahead = hour
            
        return res




