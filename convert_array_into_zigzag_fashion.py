from typing import List


class Solution:
    def zigZag(self, n : int, arr : List[int]) -> None:
        # code here
        for i in range(0, n, 2):
         
            # If current even element is greater than previous
            if (i> 0 and arr[i] > arr[i-1]):
                arr[i],arr[i-1] = arr[i-1],arr[i]
            
            # If current even element is greater than next
            if (i < n-1 and arr[i] > arr[i+1]):
                arr[i],arr[i+1] = arr[i+1],arr[i]
        
        return arr
        
        
    
n = 7
arr = [4, 3, 7, 8, 6, 2, 1]
# arr = [10, 90, 49, 2, 1, 5, 23]
sol = Solution()
print(sol.zigZag(n, arr))
