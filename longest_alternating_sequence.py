class Solution:
    def alternatingMaxLength(self, arr):
        if len(arr) < 2:
            return len(arr)  
        
        cb = 1
        bc = 1
        
        for i in range(1, len(arr)):
            if arr[i] > arr[i-1]:
                cb = 1 + bc
            
            elif arr[i] < arr[i-1]:
                bc = 1 + cb
        
        return max(cb, bc)
                            
# arr = [1, 5, 4]
arr = [1, 17, 5, 10, 13, 15, 10, 5, 16, 8]
sol = Solution()
print(sol.alternatingMaxLength(arr))