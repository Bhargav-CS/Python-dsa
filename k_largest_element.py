import heapq

class Solution:
    def kLargest(self, arr, k):
        a = heapq.nlargest(k, arr)
        return a
    
    
arr = [12, 5, 787, 1, 23]
k = 2
sol = Solution()
print(sol.kLargest(arr, k))