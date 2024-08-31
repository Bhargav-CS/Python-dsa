class Solution:
    def find3Numbers(self, arr):
        # Code Here
        n = len(arr) 
        ans = []    
        
        for i in range(n-2): 
            for j in range(i+1 , n-1): 
                for k in range(j+1 , n): 
                    if arr[i] < arr[j] and arr[j] < arr[k]:
                        ans = [arr[i] , arr[j] , arr[k]]
                        return ans 
        return ans 
        


    
    
arr = [1, 2, 1, 1, 3]
sol = Solution()
print(sol.find3Numbers) # Expected output: 1
