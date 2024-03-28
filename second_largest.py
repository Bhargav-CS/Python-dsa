class Solution:
    def print2largest(self,arr, n):
        if n < 2:
            return -1
        
        arr.sort()
        for i in range(n-2, -1, -1):
            print(arr[i], arr[n-1])
            if arr[i] != arr[n-1]:
                return arr[i]
        return -1


arr = [10, 5, 10]
N = 3
sol = Solution()
print(sol.print2largest(arr, N)) # 34