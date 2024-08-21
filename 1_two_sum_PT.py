from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dic = {}
        for i in range(len(nums)):
            if target - nums[i] in dic:
                return [dic[target - nums[i]], i]
            dic[nums[i]] = i

        
        return []
    
    
# nums = [2,7,11,15]
# target = 9

nums = [3,2,4]
target = 6

sol = Solution()
print(sol.twoSum(nums, target))
        
        