class Solution:
    def swapElements(self, arr, n):
        for i in range(n):
            if i+2<n:
                arr[i], arr[i+2] = arr[i+2], arr[i]
        return arr
    
    
n = 5
arr = [1, 2, 3, 4, 5]

sol = Solution()
# print(sol.swapElements(arr, n))
print(sol.swapElements(arr, n))