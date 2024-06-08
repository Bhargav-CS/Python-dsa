class Solution:
    def findExtra(self, n, a, b):
        left = 0
        right = n - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if mid >= len(b) or a[mid] != b[mid]:
                right = mid - 1
            else:
                left = mid + 1
        
        return left

n = 2
a = [11, 22]
b = [11]
sol = Solution()
print(sol.findExtra(n, a, b))
