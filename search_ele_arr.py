class Solution:
    #Complete the below function
    def search(self,arr, N, X):
        #Your code here
        for i in range(N):
            if arr[i] == X:
                return i
        return -1


N = 4
arr = [1, 2, 3, 4]
X = 3

sol = Solution()
print(sol.search(arr, N, X))