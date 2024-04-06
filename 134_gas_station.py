class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(gas)
        if n == 0:
            return -1
        if n == 1:
            if gas[0] >= cost[0]:
                return 0
            else:
                return -1
        start = 0
        end = 1
        curr_gas = gas[start] - cost[start]
        while start != end:
            if curr_gas < 0:
                start = (start - 1 + n) % n
                curr_gas += gas[start] - cost[start]
            else:
                curr_gas += gas[end] - cost[end]
                end = (end + 1) % n
        if curr_gas >= 0:
            return start
        else:
            return -1
        

gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
sol = Solution()
print(sol.canCompleteCircuit(gas, cost)) # 3