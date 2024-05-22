class Solution:
    def arraySortedOrNot(self, arr, n):
        # code here
        for i in range(1, n):
            if arr[i] < arr[i-1]:
                return False
        return True
    
    
n = 5
arr = [10, 20, 30, 40, 50]
sol = Solution()
print(sol.arraySortedOrNot(arr, n)) # True