class Solution:	
	def binarysearch(self, arr, n, k):
		low = 0
		high = n - 1
		while low <= high:
			mid = low + (high - low) // 2
			if arr[mid] == k:
				return mid
			elif arr[mid] < k:
				low = mid + 1
			else:
				high = mid - 1
		return -1


		
		

n = 5
arr = [1, 2, 3, 4, 5]
k = 4
sol = Solution()
print(sol.binarysearch(arr, n, k)) # Output: 3