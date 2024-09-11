from typing import List
import heapq

class Solution:
    
    def minCost(self, arr:List[int]) ->  int :
        
        heapq.heapify(arr)
        cost = 0
        while len(arr) > 1:
            
            first = heapq.heappop(arr)
            second = heapq.heappop(arr)
            
            
            combined_cost = first + second
            cost += combined_cost
            
            
            heapq.heappush(arr, combined_cost)
        
        return cost
        
        
        
arr = [4, 3, 2, 6]
# arr = [4, 2, 7, 6, 9]
sol = Solution()
print(sol.minCost(arr))