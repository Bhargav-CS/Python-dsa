from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums_set = set()
        
        for ele in nums:
            if ele not in nums_set:
                nums_set.add(ele)
            else:
                return ele
            
    
# nums = [1, 3, 4, 2, 2]
# nums = [3, 3, 3, 3, 3]
nums = [3, 1, 3, 4, 2]
sol = Solution()
print(sol.findDuplicate(nums))