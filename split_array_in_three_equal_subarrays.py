class Solution:
    def findSplit(self, arr):
        arr_sum = sum(arr)
        
        if arr_sum == 0:
            return True
        
        if arr_sum/3 != arr_sum//3:
            return False
        
        
        curr_sum = 0
        count = 3
        for i in range(len(arr)):
            curr_sum += arr[i]
            # print("curr sum is", curr_sum)
            if curr_sum == arr_sum/3:
                count -= 1
                curr_sum = 0
        
        if count == 0:
            return True
        else:
            return [-1, -1]
            
            
    
    

# arr =  [1, 3, 4, 0, 4]
# arr = [0, 1 ,1]
# arr = [2, 3, 4]
arr = [1, 1, 0]
# arr = [0, 0, 0, 0]
sol = Solution()
print(sol.findSplit(arr))