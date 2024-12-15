
class Solution:   
    def peakElement(self,arr):
        # Code here
        return arr.index(max(arr))
    
    
arr = [1, 2, 4, 5, 7, 8, 3]
sol = Solution()
print(sol.peakElement(arr)) # 6