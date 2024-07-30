from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        nums[n-k:], nums[:n-k] = nums[:n-k], nums[n-k:]
        
        return nums
    
# nums = [1,2,3,4,5,6,7]
# k = 3
nums = [-1,-100,3,99]
k = 2
# nums = [1, 2, 3]
# k = 4
sol = Solution()
print(sol.rotate(nums, k))

