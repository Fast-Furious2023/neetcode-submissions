class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # check at each station whether the gas accumulated >= the cost to next station
        # prep = gas - cost -> if positive, can travel to next stop, otherwise, need more gas from before
        # our trip must start from a non-negative value in prep
        # next station i: prep[i]+prep[i-1] >= 0 -> successful
        total_gas = sum(gas)
        total_cost = sum(cost)
        if total_gas < total_cost:
            return -1
        res_i = 0
        total = 0

        total = 0 # history_oil at i
        for i in range(len(gas)):
            total += gas[i]-cost[i]
            if total < 0:
                total = 0
                res_i = i+1
        return res_i
