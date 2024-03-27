class Solution(object):
    def removeDuplicates(self, nums):
        i = 0
        for n in nums:
            if i < 2 or n > nums[i-2]:
                nums[i] = n
                i += 1
        return i
    

nums = [1, 1, 1, 2, 2, 3]
sol = Solution()
print(sol.removeDuplicates(nums)) # Output: 5
