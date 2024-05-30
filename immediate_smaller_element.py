class Solution:
    def immediateSmaller(self, arr, n):
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                arr[i] = arr[i+1]
            else:
                arr[i] = -1
        arr[n-1] = -1
        return arr
    
n = 6
arr = [5, 6, 2, 3, 1, 7]
sol = Solution()
print(sol.immediateSmaller(arr, n)) # [2, 1, -1, 3, -1]