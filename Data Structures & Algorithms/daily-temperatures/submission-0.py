class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #while iterating, push the current element(represented by index) to an additional stack when it is smaller than or equal to the top, otherwise, a warmer temp is found
        former_temp = []
        res = [0]*len(temperatures)

        for i in range(len(temperatures)):
            if not former_temp:
                former_temp.append(i)
            else:
                while former_temp and temperatures[i] > temperatures[former_temp[-1]]:
                    res[former_temp[-1]]=i-former_temp[-1]
                    former_temp.pop()
                former_temp.append(i)
        
        return res