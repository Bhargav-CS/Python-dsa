from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heapq.heapify(nums)
        
        for _ in range(len(nums) - k + 1):
            a = heapq.heappop(nums)
            
        return a
        

# nums = [3, 2, 1, 5, 6, 4]
# k = 2

nums = [3,2,3,1,2,4,5,5,6]
k = 4

sol = Solution()
print(sol.findKthLargest(nums, k))