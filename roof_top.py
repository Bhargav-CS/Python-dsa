class Solution:
    
    #Function to find maximum number of consecutive steps 
    #to gain an increase in altitude with each step.
    def maxStep(self, arr):
        #Your code here
        
        steps = 0
        curr = 0
        for i in range(len(arr) - 1):
            if arr[i] < arr[i+1]:
                curr += 1
                steps = max(steps, curr)
            else:
                curr = 0   
                
        return steps         
                    
    
arr = [1, 2, 2, 3, 2]
arr = [1, 2, 3, 4]
sol = Solution()
print(sol.maxStep(arr))