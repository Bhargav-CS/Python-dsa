class Solution:
    def maxWater(self, arr):
        # code here
        start = 0
        end = len(arr) - 1
        max_area = 0
        
        while start < end:
            area = min(arr[start], arr[end]) * (end - start)
            max_area = max(max_area, area)
            
            if arr[start] < arr[end]:
                start += 1
            
            else:
                end -= 1
                
        return max_area
    
arr = [1, 5, 4, 3]
sol = Solution()
print(sol.maxWater(arr))