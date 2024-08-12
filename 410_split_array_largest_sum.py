from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canShip(capacity):
            total = 0
            days_needed = 1
            for weight in nums:
                if total + weight > capacity:
                    days_needed += 1
                    total = 0
                total += weight
            return days_needed <= k

        left, right = max(nums), sum(nums)
        
        while left < right:
            mid = (left + right) // 2
            if canShip(mid):
                right = mid
            else:
                left = mid + 1           
        return left   
    
# nums = [7,2,5,10,8]
# k = 2

nums = [1,2,3,4,5]
k = 2

sol = Solution()
print(sol.splitArray(nums, k))