class Solution:
    def merge(self, nums1, m, nums2, n):
        pass
    
    
nums1 = [0]
m = 0
nums2 = [1]
n = 1
sol = Solution()
print(sol.merge(nums1, m, nums2, n))

for i in range(n):
    nums1.remove(0)
    
nums1.extend(nums2)
print(nums1)