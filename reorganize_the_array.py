class Solution:
    def rearrange(self, arr):
        n = len(arr)
        element_dict = {}
        
        for i in range(n):
            if arr[i] not in element_dict:
                element_dict[arr[i]] = i
        
        for i in range(n):
            if i in element_dict:
                print(i, end=" ")
            else:
                print(-1, end=" ")
                
        return ""    
        
arr = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]
sol = Solution()
print(sol.rearrange(arr))
