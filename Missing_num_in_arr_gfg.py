class Solution:
    def missingNumber(self, array, n):
        num_set = set(array)
        for i in range(1, n+1):
            if i not in num_set:
                return i


arr = [6,1,2,8,3,4,7,10,5]
n = 10
sol = Solution()
print(sol.missingNumber(arr, n))