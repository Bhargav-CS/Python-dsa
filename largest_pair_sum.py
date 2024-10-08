from typing import List
import heapq

class Solution:
    def pairsum(self, arr:List[int]) -> int:
        heapq.heapify(arr)
        arr = heapq.nlargest(2, arr)
        return sum(arr)
    
# arr = [12, 34, 10, 6, 40]
arr = [10, 20, 30]
sol = Solution()
print(sol.pairsum(arr))