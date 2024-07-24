from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        
        left = 0
        right = 1
        max_sum = nums[left]
        curr_sum = nums[left]


        while right < n:
            curr_sum = curr_sum + nums[right]
            max_sum = max(max_sum, curr_sum)
            
            # print("current sum", curr_sum, "max sum", max_sum)
            
            # print("max_sum is", max_sum, nums[right])
            if curr_sum < nums[right]:
                left = right
                right = left + 1
                curr_sum = nums[left]
                max_sum = max(curr_sum, max_sum)
                
            else:
                right += 1
                
        return max_sum
                     
    
    
nums = [-2,1,-3,4,-1,2,1,-5,4]
# nums = [5, 4, -1, 7, 8]
# nums = [-2, 1]
# nums = [8, -19, 5, -4, 20]
sol = Solution()
print(sol.maxSubArray(nums))