class Solution:
    def canSplit(self, arr):
        #code here
        n = len(arr)
        sum_arr = sum(arr) 
        
        if sum_arr % 2 != 0:
            return False
        
        sum_arr = sum_arr // 2
        
        for ele in arr:
            sum_arr -= ele
            
            if sum_arr == 0:
                return True
            
        return False
            
        
    
    
# arr = [1, 2, 3, 4, 5, 5]
arr =  [4, 3, 2, 1]
sol = Solution()
print(sol.canSplit(arr))