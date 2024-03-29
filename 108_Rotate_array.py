class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])
        return nums

nums = [1,2,3,4,5,6,7]
k = 3

sol = Solution()
print(sol.rotate(nums, k))
nums.insert(0, nums.pop())