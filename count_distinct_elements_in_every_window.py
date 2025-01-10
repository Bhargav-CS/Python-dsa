class Solution:
    def countDistinct(self, arr, k):
        # Code here
        i = 0
        output = []
        
        while i + k -1 < len(arr):
            output.append(len(set(arr[i:i+k])))
            i = i + 1
                
        return output
            
    
    
arr = [1, 2, 1, 3, 4, 2, 3]
k = 4
arr = [4, 1, 1]
k = 2
sol = Solution()
print(sol.countDistinct(arr, k))

