class Solution:   
    def peakElement(self,arr, n):
        # Code here
        low = 0
        high = n - 1
        while low <= high:
            mid = low + (high - low) // 2
            if (mid == 0 or arr[mid - 1] <= arr[mid]) and (mid == n - 1 or arr[mid + 1] <= arr[mid]):
                return mid
            if mid > 0 and arr[mid - 1] >= arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return -1
    
    
    
    
n = 3
arr = [1, 2, 3]
sol = Solution()
print(sol.peakElement(arr, n)) # 1
