from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        hashmap = {key: 0 for key in nums}
        
        for ele in nums:
            hashmap[ele] += 1
            
        max_ = max(hashmap.values())
        # print(max_)
        
        for key in hashmap:
            if hashmap.get(key) == max_:
                return key
        
    
    
nums = [3, 2, 3]
nums = [2, 2, 1, 1, 1, 2, 2]
sol = Solution()
print(sol.majorityElement(nums))