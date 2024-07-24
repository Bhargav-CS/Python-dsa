from typing import List

class Solution:
    def sortColors(self, nums:List[int]) -> None:
        nums.sort()
        
        return nums
        
        
        
nums = [2, 0, 2, 1, 1, 0]
sol = Solution()
print(sol.sortColors(nums))