class Solution:
    def rearrange(self,arr):
        # code here
        pos = []
        neg = []
        
        for ele in arr:
            if ele < 0:
                neg.append(ele)
            
            else:
                pos.append(ele)
        
        arr.clear()
        while pos and neg:
            arr.append(pos[0])
            arr.append(neg[0])
            pos.pop(0)
            neg.pop(0)
            
        
        if pos:
            arr.extend(pos)
        
        else:
            arr.extend(neg)
        
        return arr
        
arr = [9, 4, -2, -1, 5, 0, -5, -3, 2]
# arr = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
sol = Solution()
print(sol.rearrange(arr))