class Solution:
    ##Complete this function
    def searchInSorted(self,arr, N, K):
        #Your code here
        if K in arr:
            return 1
        else:
            return -1


N = 5
K = 6
arr = [1, 2, 3, 4, 6]
sol = Solution()
print(sol.searchInSorted(arr, N, K)) # 1