class Solution:	
    #Function to reverse every sub-array group of size k.
	def reverseInGroups(self, arr, N, K):
		for i in range(0, N, K):
			arr[i:i+K] = arr[i:i+K][::-1]
			

arr = [1, 2, 3, 4, 5]
n = 5
k = 3
sol = Solution()
print(sol.reverseInGroups(arr, n, k)) # [3, 2, 1, 5, 4]