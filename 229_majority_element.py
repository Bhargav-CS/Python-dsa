from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        n = len(nums) // 3
        
        hashmap = {key: 0 for key in nums}
        
        for ele in nums:
            hashmap[ele] += 1
            
        ans = []
        for key in hashmap:
            if hashmap.get(key) > n:
                ans.append(key)
                
        return ans
    
    
nums = [3, 2, 3]
sol = Solution()
print(sol.majorityElement(nums))