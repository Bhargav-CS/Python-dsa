class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        return candidate if nums.count(candidate) > len(nums) // 2 else -1
    
N = [1,2,3]
sol = Solution()
print(sol.majorityElement(N)) # -1