class Solution:
    def transitionPoint(self, arr, n): 
        # Code here
        for i in range(n):
            if arr[i] == 1:
                return i
        return -1
    
n = 5
arr = [0, 0, 0, 1, 1]
sol = Solution()
print(sol.transitionPoint(arr, n)) # 3