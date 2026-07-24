class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # iterate through triplets
        # filter out the elements larger than target
        # then for those no larger than, track the largest value for i in range(len(target))
        # to return True, the largest values == target

        
        i_last_valid = -1

        for i in range(len(triplets)):
            can_use = True
            for j in range(len(triplets[0])):
                if triplets[i][j] > target[j]:
                    can_use = False
                    break 
            if can_use:
                if i_last_valid != -1:
                    triplets[i]= [max(a,b) for a, b in zip(triplets[i],triplets[i_last_valid])]
                i_last_valid = i
               

        return triplets[i_last_valid] == target
            

            