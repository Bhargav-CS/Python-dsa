import heapq

class Solution:
    def alternateSort(self,arr):
        # Your code goes here
        arr.sort()
        b = arr[::-1]
        ac = []
        for i in range(len(arr)):
            if i%2==0:
                ac.append(b[i//2])
            else:
                ac.append(arr[i//2])
        return ac
        
        
                
    
# arr = [7, 1, 2, 3, 4, 5, 6]
arr = [1, 6, 9, 4, 3, 7, 8, 2]
sol = Solution()
print(sol.alternateSort(arr))