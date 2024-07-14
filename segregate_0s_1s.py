class Solution:
    def segregate0and1(self, arr:list):
        count0 = arr.count(0)
        count1 = arr.count(1)
        
        if count0 == len(arr) or count1 == len(arr):
            return arr
        
        for i in range(len(arr)):
            if i < count0:
                arr[i] = 0
                
            else:
                arr[i] = 1
                
        return arr
    
arr = [0, 0, 1, 1, 0]
sol = Solution()
print(sol.segregate0and1(arr))